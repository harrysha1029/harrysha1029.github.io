---
title:  "Song Order - Guitar Tunings and the Travelling Salesperson"
tags: guitar math
---

I play gigs with my acoustic guitar every now and then, and a lot of the pieces I play feature **weird** tunings. So here's the problem: tuning from one tuning to another very different tuning not only takes a long time it makes the guitar go out of tune more quickly and also increases the risk of broken strings. Thus I want to order my songs such that each jump between tunings isn't that large!

## Definitions
Let's start with some definitions! First in math, then in code. 
* Associate each key on the piano with an integer starting with A0 = 0, Bb0 = 1... and so on.
* Define a tuning to be a vector a 6 pitches.
* For any tunings x, y define their distance to be the *'manhattan distance'* or \\(L_1\\) distance:

$$d\_{tuning}(x, y) = \sum\_{i=1}^6 |x\_i - y\_i|.$$

Here it is in the rust language.

<pre><code class='language-rust'>
enum Note {A, Bb, B, C, Db, D, Eb, E, F, Gb, G, Ab}

struct Pitch(Note, i32); // Note, Octave

type Tuning = [Pitch; 6];
</code></pre>

So to start, we have the `Notes` type which can take on one of 12 values. Then, we have the `Pitch` type which is represented as a tuple containing a `Note` and an octave, e.g. A4. A *Tuning* is then a list of 6 *Pitches* (one for each string on the guitar). We associate `Pitch` values with integers, and define distances as follows.

<pre><code class='language-rust'>
fn note2num(note: &Note) -> i32 {
    match note {
        Note::A => 0,
        Note::Bb => 1,
        Note::B => 2,
        ...
        Note::Ab => 11,
    }
}

impl Pitch {
    fn num(&self) -> i32 {
        note2num(&self.0) + (self.1 * 12)
    }
}

fn pitch_dist(p1: &Pitch, p2: &Pitch) -> i32 {
    (p1.num() - p2.num()).abs()
}

fn tuning_dist(p1: &Tuning, p2: &Tuning) -> i32 {
    p1.iter()
        .zip(p2)
        .map(|(a, b)| pitch_dist(a, b))
        .sum::< i32>()
}
</code></pre>

## The Problem

Let's view this as a graph problem. Let the nodes in the graph be the tunings, and have an edge between each node, with the cost of the edge being the distance between the two tunings. Then **we want to find the 'shortest' path that passes through all the nodes**. Not only that, because we want to start and end up in standard tuning, we want to find the 'shortest' cycle that passes through all the nodes. **Turns out, this is a famous problem known as the travelling salesperson problem (TSP)**! And it's pretty hard to solve (NP-Hard). Here is the list of tunings we are working with (there are 14 of them).

<pre><code class='language-rust'>
[E2, A3, D3, G3, B3, E4]
[D2, A3, D3, G3, A3, D4]
[D2, A3, D3, Gb3, A3, D4]
[B2, E2, D3, Gb3, A3, D4]
[E2, B3, D3, G3, B3, D4]
[E2, B3, D3, G3, B3, E4]
[B2, Gb2, Db3, Gb3, B3, Gb4]
[E2, C3, D3, G3, A3, D4]
[D2, A3, D3, G3, C3, E4]
[C2, G2, D3, F3, Bb3, D4]
[Gb2, A3, B3, E3, Ab2, B4]
[Db2, Ab2, E3, Gb3, B3, Eb4]
[D2, A3, E3, F3, C3, E4]
[D2, G2, D3, G3, B3, E4]
</code></pre>

## Brute Force Search
There are some really [cool algorithms for TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem#Computing_a_solution). But for my case, the simplest one - brute force - will suffice. This approach is to simply try every single cycle. We have 14 tunings, so how many cycles are there? Well because it's a cycle, it doesn't matter with which element it starts/ends with. So fix one, and then pick the order of the remaining 13 tunings (actually there are even fewer because the 'reverse cycle' has the same cost but I'll just ignore this). Thus we have \\(13! = 6,227,020,800\\) tunings cycles to look through! The brute force search algorithm is implemented here.

<pre><code class='language-rust'>
fn brute_force(tunings: &Vec<Tuning>) -> (i32, Vec<usize>) {
    let len = tunings.len();
    let first = &tunings[0];
    (1..len)
        .into_iter()
        .permutations(len - 1)
        .progress_count(fact((len as i32) - 1)) // Loading bar
        .map(|ord| (tuning_seq_dist_ord(tunings, &first, &ord), ord))
        .min_by_key(|x| x.0)
        .unwrap()
}
</code></pre>

After running this, we found that the following cycle was optimal with weight 84 :)

<pre><code class='language-rust'>
[E2, A3, D3, G3, B3, E4]
[E2, B3, D3, G3, B3, E4]
[E2, B3, D3, G3, B3, D4]
[E2, C3, D3, G3, A3, D4]
[D2, A3, D3, G3, A3, D4]
[D2, A3, D3, Gb3, A3, D4]
[Gb2, A3, B3, E3, Ab2, B4]
[C2, G2, D3, F3, Bb3, D4]
[B2, E2, D3, Gb3, A3, D4]
[B2, Gb2, Db3, Gb3, B3, Gb4]
[Db2, Ab2, E3, Gb3, B3, Eb4]
[D2, A3, E3, F3, C3, E4]
[D2, A3, D3, G3, C3, E4]
[D2, G2, D3, G3, B3, E4]
[E2, A3, D3, G3, B3, E4]
</code></pre>

Yay.