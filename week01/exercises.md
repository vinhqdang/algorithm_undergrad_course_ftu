# Week 1 Exercises — Introduction to Algorithms & Efficiency

## Conceptual Questions

**Exercise 1.1** Define the term "algorithm." List and explain the five properties an algorithm must satisfy. Give one example from everyday life that can be described as an algorithm.

**Exercise 1.2** For each of the following tasks, estimate the input size $n$ and describe an algorithm:
- (a) Sorting a deck of 52 playing cards
- (b) Looking up a word in a dictionary
- (c) Finding the cheapest flight from Hanoi to Ho Chi Minh City

**Exercise 1.3** What is the difference between:
- (a) Time complexity and space complexity
- (b) Worst-case and average-case complexity
- (c) An algorithm and a program

---

## Complexity Analysis

**Exercise 1.4** Count the exact number of basic operations in the following code snippets, then express using $\Theta$ notation:

```python
# (a)
total = 0
for i in range(n):
    total += i

# (b)
total = 0
for i in range(n):
    for j in range(n):
        total += i * j

# (c)
total = 0
for i in range(n):
    for j in range(i, n):
        total += 1

# (d)
i = n
while i > 1:
    i = i // 2
```

**Exercise 1.5** For each function below, determine the tightest $\Theta$ bound:
- (a) $f(n) = 5n^3 + 100n^2 + n + 1000$
- (b) $f(n) = n \log n + 3n$
- (c) $f(n) = 2^{n+3} + n^5$
- (d) $f(n) = \log(n^{10}) + \sqrt{n}$
- (e) $f(n) = (n+1)(n+2)/2$

**Exercise 1.6 (Loop Invariant)** The following algorithm computes $a^n$ for integer $a > 0$, $n \geq 0$:

```python
def power(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result
```

- (a) State a loop invariant for the `for` loop.
- (b) Prove the three properties: Initialisation, Maintenance, Termination.
- (c) What is the time complexity? Space complexity?

---

## Algorithm Design

**Exercise 1.7** Given an unsorted array of $n$ integers, write an algorithm to find:
- (a) The maximum element — analyse its time complexity
- (b) Both the maximum and minimum simultaneously — can you do it in fewer than $2(n-1)$ comparisons?
- (c) The $k$-th largest element (for now, any correct algorithm is fine)

**Exercise 1.8 (Insertion Sort Analysis)**
- (a) Trace insertion sort on the array `[5, 2, 4, 6, 1, 3]`. Show each step.
- (b) How many comparisons does insertion sort make in the worst case? Best case?
- (c) Is insertion sort in-place? Is it stable? Define both terms.

**Exercise 1.9** Consider the following two algorithms to compute the $n$-th Fibonacci number:

```python
# Algorithm A (recursive)
def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Algorithm B (iterative)
def fib_iterative(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
```

- (a) What is the time complexity of Algorithm A? Algorithm B?
- (b) What is the space complexity of each?
- (c) Run both for $n = 40$ and compare execution time.

---

## Challenge Problems

**Exercise 1.10 ★** Prove or disprove: If $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$, then $f(n) = \Theta(g(n))$.

**Exercise 1.11 ★★** Binary search runs in $O(\log n)$. If we have a sorted array of $10^9$ elements, what is the maximum number of comparisons needed? If we run $10^6$ binary searches per second, how long does it take to process $10^{12}$ queries?

**Exercise 1.12 ★★** Design an algorithm that, given a sorted array and a target sum $S$, finds two elements in the array whose sum equals $S$. Aim for $O(n)$ time. Prove its correctness and analyse its complexity.
