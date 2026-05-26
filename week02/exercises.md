# Week 2 Exercises — Asymptotic Notation & Complexity Classes

## Big-O / Theta / Omega Proofs

**Exercise 2.1** For each pair, prove or disprove using the formal definition:
- (a) $5n^2 + 3n = O(n^2)$
- (b) $n^2/4 = \Omega(n)$  
- (c) $3n\log n + n = \Theta(n\log n)$
- (d) $n! = O(2^n)$
- (e) $\log_2 n = \Theta(\log_{10} n)$

**Exercise 2.2** Rank the following functions from slowest to fastest growing:
$$n^2,\quad 2^n,\quad n\log n,\quad \sqrt{n},\quad n!,\quad \log^2 n,\quad n^{1.5},\quad 3^n,\quad n\sqrt{n}$$

**Exercise 2.3** For each function, give the tightest asymptotic bound:
- (a) $T(n) = \sum_{i=1}^{n} i^2$
- (b) $T(n) = \sum_{i=1}^{\log n} n$
- (c) $T(n) = \sum_{i=0}^{n} 2^i$
- (d) $T(n) = n^2 \cdot 2^n + n^{100}$

**Exercise 2.4** Prove or disprove:
- (a) $f(n) = O(g(n)) \Rightarrow g(n) = \Omega(f(n))$
- (b) $f(n) + g(n) = \Theta(\max(f(n), g(n)))$
- (c) If $f(n) = O(g(n))$ and $g(n) = O(h(n))$, then $f(n) \cdot g(n) = O(h(n)^2)$

## Complexity Analysis Practice

**Exercise 2.5** Determine the time complexity of each algorithm:
```python
# (a)
for i in range(n):
    j = 1
    while j < n:
        j *= 2

# (b) 
def mystery(n):
    if n <= 1: return 1
    return mystery(n//2) + mystery(n//2) + n

# (c)
for i in range(n):
    for j in range(1, n, i+1):
        pass
```

**Exercise 2.6** Space complexity:
- (a) What is the space complexity of recursive factorial?
- (b) What is the space complexity of iterative factorial?
- (c) Consider: recursive binary search vs iterative binary search — compare both time and space.

## Complexity Classes

**Exercise 2.7** Classify each problem as P, NP-complete, or NP-hard (justify briefly):
- (a) Sorting a list of $n$ integers
- (b) 3-SAT (given a boolean formula in 3-CNF, is it satisfiable?)
- (c) Finding the shortest path in a weighted graph
- (d) Graph colouring with 2 colours (is the graph bipartite?)
- (e) Graph colouring with 3 colours
- (f) Finding a Hamiltonian cycle in a graph
- (g) Finding an Eulerian circuit in a graph

**Exercise 2.8** The Halting Problem:
- (a) State the Halting Problem formally
- (b) Outline Turing's proof by contradiction (diagonalisation)
- (c) Why does this matter for software testing?

**Exercise 2.9 ★** NP-completeness by reduction: Explain in your own words what it means to "reduce" problem A to problem B, and why if A is NP-complete and A reduces to B in polynomial time, then B is NP-hard.

## Challenge Problems

**Exercise 2.10 ★★** Show that $\sum_{k=1}^{n} k = \Theta(n^2)$ using the formal definition. Find explicit constants $c_1, c_2, n_0$.

**Exercise 2.11 ★★** Prove that if $f(n) = o(g(n))$, then $f(n) = O(g(n))$ but $f(n) \ne \Theta(g(n))$.

**Exercise 2.12 ★★★** [Research question] The algorithm for sorting integers in $O(n\log\log n)$ time using van Emde Boas trees assumes integers are in range $[0, U]$. How does $U$ factor into the complexity? When does this beat comparison-based $\Omega(n\log n)$?
