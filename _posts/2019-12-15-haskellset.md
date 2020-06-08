---
title:  "Haskell Concepts with Sets"
tags: math set_theory
---
In this post we'll explore some Haskell and functional programming concepts with set theory. Our goal here is to implement a type that represents a set, and build the Von Neumann universe up to \\(V_{\omega}\\). 

## Haskell
You can follow the examples in this post here (you can open it in a bigger window by clicking the top right). To play around with it, you can type `:l main` in the ghci prompt, which will load the code.

<iframe height="800px" width="100%" src="https://repl.it/@HarrySha/haskellSetTheory?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

## Recursive data types
You can define data types in Haskell using the `data` keyword. For example. `data Bool = True | False`. In our case, we want to define a type for Sets. For our purposes, we can think of a set as a collection of other sets. So one possible declaration for a our type would be 

<pre><code class="language-haskell">
data Set = Elems [Set]
</code></pre>

This defines `Set` recursively as a list of `Set`, and we can create sets using the `Elems`. For example `emptyset = Elems []`.

## Typeclasses
A typeclass in Haskell is like an adjective describing the type. Common typeclasses are `Ord` (can be ordered), `Eq` (can be equated), `Show` (can be converted to string). More precisely, a typeclass defines a set of functions that instances implement, somewhat like an interface. To save some work, we can often use the deriving keyword when defining our data type. For example we might do 
`data Set = Elems [Set] deriving (Eq, Show)`. These will use the default implementations which are often sufficient. Loading this up in ghci we get

<pre><code class="language-haskell">
> data Set = Elems [Set] deriving (Eq, Show)
> emptySet = Elems []
> emptySet
Elems []
> emptySet == emptySet
True
> a = Elems [Elems [], Elems []]
> a 
Elems [Elems [], Elems []]
> b = Elems [Elems []] 
> a == b
False 
</code></pre>

There are a couple of problems with this. We should have had `a == b` is True, as sets are unordered and don't care about duplicates. Also, the default implementation of show prints sets in a kind of clunky way. Luckily, we can solve these problems by providing our own implementation for the `Eq` and `Show` typeclasses.

### Equality (any and all)
A good definition for set equality is \\(a = b \iff a \subseteq b \land b \subseteq a\\). We can implement the type class as follows.

<pre><code class="language-haskell">
subset (Elems x) (Elems y) = all (\a -> (any (\b -> a == b) y)) x 
instance Eq Set where
    a == b = (subset a b) && (subset b a)
</code></pre>

Something I find pretty cool is that the implementation for subset translates almost directly from the first order logic definition 

$$a \subseteq b \iff \forall a \in x. \exists b \in y. (a = b)$$

To see how this works we can examine the type of `any` and `all`:

<pre><code class="language-haskell">
any :: Foldable t => (a -> Bool) -> t a -> Bool 
</code></pre>

Think of `t` as a list for now. `any` takes as input a predicate and a list, and returns true if any item in the list makes the predicate true. and `all` works analogously. Thus `any (\a -> p a) x` translates to \\(\exists a \in x. p(a)\\), and `all (\a -> p a) x` translates to \\(\forall a \in x. p(a)\\). As a result of this definition, we have:

<pre><code class="language-haskell">
> Elems [Elems []] == Elems [Elems [], Elems []] 
True -- don't care about repetition
> Elems [Elems [Elems []], Elems []] == Elems [Elems [], Elems [Elems []]]
True -- unordered
</code></pre>

Another interesting thing is that one might think that there is a problem with circular definitions here. We are using `subset` to define `==`, but also `==` in the definition of `subset`. Turns out this is ok as it is in fact a pairwise recursive definition.

### Show
Printing is still ugly, so let's implement our own show function!

<pre><code class="language-haskell">
instance Show Set where
    show (Elems x) =
        let nodup = Data.List.nub x in -- Remove duplicates 
        "["
        ++ (Data.List.intercalate ", " [show a | a <- nodup])
        ++ "]"
</code></pre>

The first step is to remove duplicates. Notice that we didn't have to write our own remove duplicates function because Data.List.nub does that, and it has type

<pre><code class="language-haskell">
nub :: Eq a => [a] -> [a]`
</code></pre>

and we have implemented `Eq` for `Set`! `show` then works by recursively showing its elements and joining them with ",". Now our elements show as follows

<pre><code class="language-haskell">
> x = Elems [ Elems [], Elems [Elems []]]
[[], [[]]]
</code></pre>

### Num
<pre><code class="language-haskell">
elem x (Elems y) = any (\a -> x == a) y
notElem x y = not (Set.elem x y)
opair x y = Elems [x, Elems [y]]
</code></pre>

While we're at it, let's make `Set` an instance of `Num`. This will let sets behave like numbers, so we can add subtract and multiply sets, which we'll take to correspond to the operations of \\( \cup, \setminus \\), and \\( \times \\).

<pre><code class="language-haskell">
elem x (Elems y) = any (\a -> x == a) y
notElem x y = not (Set.elem x y)
opair x y = Elems [x, Elems [y]]

instance Num Set where
    (+) (Elems x) (Elems y) = Elems (x ++ y) -- Union
    (-) (Elems x) y = Elems (filter (\a -> a `Set.notElem` y) x) -- Difference
    (*) (Elems x) (Elems y) = Elems $ opair <$> x <*> y -- Cartesian Prod
    fromInteger x = naturals !! (fromInteger x) -- To be explained
    abs = undefined
   signum = undefined
</code></pre>

For union, we just concatenate the lists (not worried about duplicates because of the way we define `==` and `show`). For the difference, \\(x \setminus y\\), we keep only the elements in \\(x\\) that are not in \\(y\\). Cartesian product gets a little spicy and uses `<*>` from the Applicative typeclass. `opair <$> x` partially applies opair to each element of \\(x\\), and then `<*> y`, applies each of the partially applied functions in `opair <$> x` to each element of \\(y\\), which gives us a a list of all ordered pairs \\(\langle a, b \rangle\\) where \\(a \in x\\), and \\(b \in y\\).

Once we have implemented the Num typeclass for Set we can use `+, - , *` on sets. We also get to use sets as arguments to functions that take in `Num`. For example, we get to use `^` (exponentiation) which has type signature

<pre><code class="language-haskell">
(^) :: (Num a, Integral b) => a -> b -> a 
</code></pre>

even though we didn't explicitly implement it, nice.

## \\( \omega\\), \\(V_\omega\\), and Infinite data structures
Now \\(\omega\\) and \\(V_\omega\\) are pretty big, in fact they're both infinite. So how do we can we represent these in our computers that have finite memory? Haskell has the answer, and it's lazy evaluation. The idea is that we can have a data structure that is 'infinite' because we don't actually compute it until we need it (lazy). We can then define the following

<pre><code class="language-haskell">
insert (Elems x) y = Elems (y:x)
successor x = insert x x
naturals = iterate successor (Elems [])
omega = Elems naturals

smap f (Elems x) = Elems (map f x) -- Map but for sets
-- powerset(x:xs) = all the subsets with x \cup all the subsets w/o x
powerSet (Elems []) = Elems [Elems []]
powerSet (Elems (x:xs)) = let withoutFirst = powerSet $ Elems xs in 
                          smap (\a -> insert a x) withoutFirst + withoutFirst

bigCup (Elems x) = foldl (+) (Elems []) x
vOmega = bigCup $ Elems $ iterate powerSet (Elems [])
</code></pre>

The successor function \\(S(x) = x \cup \\{x\\}\\) is defined by inserting itself into the set, and a list of natural numbers can then be defined using the `iterate` function. 

<pre><code class="language-haskell">
iterate :: (a -> a) -> a -> [a]
</code></pre>

Which takes a function, a starting point, and returns an infinite list of repeated applications of the function. So `naturals` is \\(\left[0, S(0), S(S(0)),...\right]\\), and `omega` is `Elems naturals`: the set whose elements are all the natural numbers - a.k.a \\(\omega\\). Similarly, we can define powerset, and \\(V_\omega\\)! 

## Conclusion
This was some practice for me in learning new concepts in functional programming and Haskell. It was fun, and I found it cool that you can represent infinite sets in a programming language. 

We could have used Data.Set.Set as our container instead of list. We could also extend this by making set an instance of Foldable (or I guess something like MonoFoldable). 