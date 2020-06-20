---
title: "Complexity Theory Notes"
tags: cs math notes
---

<script src ="/load_mathjax_complexity.js"></script>

## Intro
I like taking notes in markdown and this website is an easy way to render markdown :).

Sources:
* Wikipedia
* Arora-Barak
* CS 254


## Big O
### Definition Big/Little-O
$$f \in O(g) \text{ if } \exists c (f(n) \leq cg(n)) \text{ for sufficiently large } n$$
$$f \in o(g) \text{ if } \forall \varepsilon (f(n) \leq \varepsilon g(n)) \text{ for sufficiently large } n$$
$$f \in \Omega(g) \text{ if } g \in O(f)$$
$$f \in \omega(g) \text{ if } g \in o(f)$$

## Turing Machines
### Definition of a TM
Described by $(\Gamma, Q, \delta)$. There is a read only input tape and k-1 work tapes, the last of which is the output tape.

* $\Gamma$ is the alphabet (containing at least 0, 1, $\square$, $\triangleright$)
* $Q$ is a set of states, and 
* $\delta : Q \times \Gamma^{k-1} \to Q \times \Gamma^{k-1} \times \{L, S, R\}^k $ is a transition function. 

### Efficient Universal Turing Machine

There is a TM $\U$ s.t. $\forall x, \alpha \in \OO^*, \U(x, a) = M\_\alpha(x)$. Furthermore if $M\_\alpha$ halts on an input $x$ within $T$ stapes, then $\U(x, \alpha)$ halts within $CT\log T$ steps, where $C$ is a constant independent of $|x|$.

## P, NP, CoNP

### Defintions 
A non-deterministic TM (NDTM) is the same as a regular TM except it has two transition function that which can be used arbitrariliy, furthermore, there is an accept state. **A NDTM $N$ runs in time $T(n)$ if for every input $x \in \OO^*$ and every sequence of non-deterministic choices, $M$ reaches either the halting state or the accepting state within $T(|x|)$ steps.**

Complexity Classes:
* $\P = \bigcup_c \DTIME(n^c)$
* $L \in \NP$ iff $\exists$ polynomial $p$, and polytime TM $M$ st. $\forall x$:
$$x \in L \iff \exists u \in \OO^{p|x|} \st M(x, u) = 1$$
* Alternatively: $\NP = \bigcup_c \NTIME(n^c)$
* $L \in \coNP$ iff $\exists$ polynomial $p$, and polytime TM $M$ st. $\forall x$:
$$x \in L \iff \forall u \in \OO^{p|x|} \st M(x, u) = 1$$
* Alternatively: $\coNP = \\{L | \neg L \in \NP\\}$

### Hierarchy Theorems
* If $f, g$ are such that $f(n) \log f(n) = o(g(n))$, then 
$$ \DTIME(f(n)) \subsetneq \DTIME(g(n))$$
* If $f, g$ are such that $f(n) = o(g(n))$, then 
$$ \SPACE(f(n)) \subsetneq \SPACE(g(n)) $$
* If $f, g$ are such that $f(n+1) = o(g(n))$, then 
$$ \NTIME(f(n)) \subsetneq \NTIME(g(n))$$

Prove all of these using diagonalization.

### Cook Levin Theorem
$$\SAT \text{ is } \NP \text{ Complete }$$

**Lemma**: For any Boolean function $f : \OO^l \to \OO$, there is a boolean formula $\varphi$ of size $l2^l$ such that $\varphi(u) = f(u)$ for all $u$. Note that the 'size' of a boolean formula is the number of $\lor/\land$ it contains. Note that for each $u \in \OO^l$ there is some clause $C\_u$ such that $C\_u(x) = 0 \iff x = u$. For example for u=0110 take $x\_1 \lor \neg x\_2 \lor \neg x\_3 \lor x\_4$. Then let $\phi$ be the $\bigwedge\_{u, \st f(u)=0}C\_u$.


**Proof**. Let $L \in \NP$, and $M$ be the polytime verifier for $L$. Assume that $M$ only has 2 tapes and is 'oblivious' in the sense that the head movement depends only on the length of the input. This transformation may incur at most a polynomial increase in runtime. This allows us to know exactly where the tape head is going to be at any step in the execution. Define a snapshot of the execution at step $i$, $z\_i = \ab{a, b, q}$, say it takes $c$ bits to encode a snapshot. Then to figure out $z\_i$, we just need to know the previous state $z\_{i-1}$, and the bits on the input tape and the work tape.

For any $x$, $x \in L \iff \exists u (M(x, u=1))$. Equivalently, $x \in L \iff \exists y$ (intuitively $xu$), and $z_i,...,z_T \in \OO^c$ for which the following conditions hold.
* The first $n$ bits of $y$ are equal to $x$.
* $z_1$ encodes the initial snapshot
* $z\_{i+1}$ follows for $z\_i$ encodes the initial snapshot
* $z\_{T}$ is a snapshot for which the machine accepts.

Condition 1 is a CNF of size $4n$, conditions 2 and 4 depend on at most $c$ variables so require a CNF of size at most $c2^{c}$. Finally condition $3$ is the AND of polynomially many CNFs each of at most $3c+1$ variables so takes a CNF of at most $T(3c+1)2^{3c+1}$. Summing these we get a formula of size $d(n+T)$. Where $d$ is some constant that depends only on $c$, a constant depending only on the alphabet/states of $M$.

### Ladner's Theorem
If $\P \neq \NP$, there there exists a language $L \in \NP \setminus \P$ that is not $\NP$-complete.

### Baker, Gill, Solovay Theorem
There exists oracles $A, B$ such that $\P^A = \NP^A$, and $\P^B \neq \NP^B$. 

## Space Complexity
Space can be reused but time cannot. Define space complexity by the total number of work tape locations that are at one point not blank.

$$\DTIME(S(n)) \subseteq \SPACE(S(n)) \subseteq \NSPACE(S(n)) \subseteq \DTIME(2^{O(S(n))})$$

### Configuration Graphs
A configuration of TM $M$ consists of the contents of all the non-blank entries of $M$ tapes along with it state and head positions at a particular point in the execution. For TM , $M$, and input $x$, the configuration graph $G\_{M, x}$ is a directed graph whose nodes correspond to the possible configurations $M$ can reach from $C\_{start}^x$. Then a configuration $C$ has an edge to $C'$ if $C'$ is reachable from $C$ using the transition function (in one step). Note that if $M$ is deterministic, then each node just has out degree 1. Also, as the TMs we are looking at always halt, we can assume the graph has no loops. 

Every vertex in $G\_{M, x}$ can be described with $cS(n)$ bits thus $G\_{M, x}$ has $2^{cS(n)}$ nodes.

### Complexity Classes
* $\PSPACE = \bigcup_c \SPACE(n^c)$
* $\NPSPACE = \bigcup_c \NSPACE(n^c)$
* $\L = \SPACE(\log(n))$
* $\NL = \NSPACE(\log(n))$

### PSPACE
Define a notion of completeness use polytime reduction. $\TQBF$ is the language containing all quantified boolean formula that are true. Then $\TQBF$ is $\PSPACE$-Complete, and $\NPSPACE$-Complete. 


### Savitch's Theorem
For any $S(n) \geq \log (n)$, $\NSPACE(S(n)) \subseteq \SPACE(S(n)^2)$. 

**Lemma**. We can solve $\STCON$ on a graph with $n$ vertices using $O((\log n)^2)$ space.

```python 
def reach(s, t, k) -> bool:
    if k == 0:
        return s == t
    if k == 1:
        return s == t or (s, t) in edges
    for u in vertices:
        if k_edge_path(s, u, floor(k / 2)) and k_edge_path(u, t, ceil(k / 2)):
            return True
    return False
```
`reach(s, t, n)` will tell you if $s$ and $t$ are connected in the graph. Note that because we are halving $n$ each time, the recursion depth is $O(\log(n))$, and we store the local variables at each level which takes $O(\log(n))$. Therefore, the we use $O(\log^2(n))$ space as required.

**Proof**. Let $L \in \NSPACE(S(n))$ be decided by at TM $M$. For every $x \in \OO^n$, the configuration graph $G_{M, x}$ has size at most $A = 2^{O(S(n))}$. The lemma implies that we can check whether the start config and the accept config with a deterministic alg in space $O(\log^2(A)) = O(S(n)^2)$

### NL Completeness
Logspace reductions... TODO

### NL = coNL
TODO

## The Polynomial Hierarchy
### Definitions
* $\Sigma_2$ is the set of languages $L$ for which there is a polytime TM, M and polynomial q such that 
$$ x \in L \iff \exists u \in \OO^{q(|x|)} \forall v \in \OO^{q(|x|)} M(x, u, v)=1$$
* $\Pi_2$ is the set of languages $L$ for which there is a polytime TM, M and polynomial q such that 
$$ x \in L \iff \forall u \in \OO^{q(|x|)} \exists v \in \OO^{q(|x|)} M(x, u, v)=1$$
* Get $\Sigma_k$ and $\Pi_k$ by adding more quantifies. $\Sigma_k$ always starts with $\exists$, and $\Pi_k$ always starts with $\forall$
* $\PH = \bigcup \Sigma_i$
### Theorems
* Collapse of $\PH$. If $\P = \NP$, then $\PH = \P$. (Prove by induction. In the inductive step, create a new language by stripping the left most quantifier and apply the inductive hypothesis on that.)
* $\PH \subset \PSPACE$. Just check $k$ quantified variables one at a time each taking polynomial space.
* Defining the hierarchy with oracles. for $i \geq 2$: $\Sigma\_i = \NP^{\Sigma\_{i=1}\SAT}$
* $\SAT$ cannot be solved simulatneously in linear time and sublinear space.


## Circuits
Circuits are another model of computation that is non-uniform, which means we can have a different algorithm for each input size.

A circuit can have $\land, \lor$, and $\neg$ gates, and the size of the circuit is defined to be the number of nodes in the circuit. We allow $\land$ and $\lor$ to have fan-in.

### Definitions
* A $T(n)$ sized circuit family is a sequence $\{C\_n\}\_{n\in \N}$ of boolean circuits, where $C\_n$ has $n$ inputs and a single output such that $|C_n| \leq T(n)$ for every $n$.
* $\PPOLY = \bigcup_c \SIZE(n^c)$ is the class of languages that are decidable by polynomial sized circuit families. 
* Alternatively, we can define $\PPOLY$ as Turing Machines that *'take advice'*. This means that the Turing Machine gets some poly-length string that is fixed for each input length as input. 
* A circuit family is *logspace uniform* if there is an implicitly logspace computable function mapping $1^n$ to the description of the circuit $C_n$.

### Theorems
* Karp-Lipton. If $\NP \subseteq \PPOLY$ then $\PH = \Sigma\_2$. 


## Randomness
### Definitions
* Probabilistic Turing Machines (PTMs) are defined like NDTMs except each transition function is selected with probability 0.5, and we say that the TM decides a language if it outputs the right answer with probability at least 2/3.
* $\BPTIME(T(n))$ is the set of languages decided by a PTM in time T(n)
* $\BPP = \bigcup_c \BPTIME(n^c)$.
* Alternatively, There is some deterministic polytime TM $M$, such that for every $x$,  $Pr_{r \in \OO^{p(|x|)}}[M(x, r) = L(x)] \geq 2/3$.

| Class  | Accept prob when $x\in L$  | Accept prob when $x \notin L$
| :-------------: | :-------------: | :----------------: |
| BPP  | 2/3  | 1/3 |
| RP | 2/3 | 0 |
| coRP | 1  | 1/3|
| NP | > 0  | 0 |
| P | 1 | 0 |
| ZPP (expected poly runtime) | 1 | 0 |

Alternate definition for $\ZPP$: $\ZPP = \RP \cap \coRP$
### Error reduction
TODO

### $\BPP \subset \PPOLY$
TODO
### $\BPP \subset \PH$
TODO




## Interactivity
### Definitions
TODO

## Open
* $\P \QEQ \NP$
* $\coNP \QEQ \NP$
* $\P \QEQ \NP \cap \coNP$
* $\NP \QEQ \L$
* $\L \QEQ \NL$