# Week 1 Exercises - Introduction to Algorithms and Efficiency

These exercises are designed for a 3-hour first lecture plus homework. The goal is not only to compute Big-O answers, but also to build intuition from practical examples and timing experiments.

## Required Reading

Read before Week 2:

- CLRS, 4th ed., Chapter 1: The Role of Algorithms in Computing.
- CLRS, 4th ed., Section 2.1: Insertion sort.
- CLRS, 4th ed., Section 2.2: Analyzing algorithms.
- CLRS, 4th ed., beginning of Chapter 3: growth of functions.

Supplementary:

- Jeff Erickson, *Algorithms*, Chapter 0: Introduction.
- MIT OCW 6.006 introductory materials on algorithmic thinking.
- Python documentation for `time.perf_counter`.
- VisuAlgo visualizations for searching and sorting.

---

## Part A - Quick Quizzes

**Quiz 1.1 - Algorithms in daily life**

For each system, name one algorithmic problem and a reasonable input size `n`.

1. Google Maps or Grab route planning.
2. YouTube or Netflix video streaming.
3. Phone camera night mode.
4. Shopee, Lazada, or Tiki search.
5. Bank fraud detection.

**Quiz 1.2 - Algorithm or not?**

For each description, decide whether it is a well-defined algorithm. If not, explain what is missing.

1. "Find a good restaurant near campus."
2. "Sort these exam scores from highest to lowest by repeatedly selecting the largest remaining score."
3. "Keep improving the answer until it looks nice."
4. "Given a sorted list and a target, repeatedly compare the target with the middle item and discard half of the list."
5. "Try random passwords until the account opens."

**Quiz 1.3 - Growth-rate intuition**

Classify each task as closest to `O(1)`, `O(log n)`, `O(n)`, `O(n^2)`, or exponential.

1. Read the first element of a list.
2. Search for a name in an unsorted list.
3. Binary search in a sorted list.
4. Compare every pair of students in a class.
5. Try all binary strings of length `n`.
6. Repeatedly divide `n` by 2 until it becomes 1.

---

## Part B - Conceptual Questions

**Exercise 1.1** Define the term "algorithm." List and explain the properties an algorithm should satisfy: input, output, definiteness, correctness, finiteness, and effectiveness.

**Exercise 1.2** Explain the difference between:

1. a problem and an algorithm;
2. an algorithm and a program;
3. an implementation and a timing experiment;
4. worst-case and average-case running time;
5. time complexity and space complexity.

**Exercise 1.3** For each task, estimate the input size `n` and describe one possible algorithm.

1. Looking up a student ID in a sorted list.
2. Finding duplicate student IDs in a class list.
3. Compressing one image from a phone camera.
4. Processing one second of 4K video at 60 frames per second.
5. Multiplying two 1000-digit integers.
6. Finding the cheapest flight route from Hanoi to Paris.

**Exercise 1.4 - Why scale changes everything**

Assume a computer performs `10^8` simple operations per second. Estimate the running time for:

1. `n` operations when `n = 10^8`;
2. `n^2` operations when `n = 10^6`;
3. `2^n` operations when `n = 60`;
4. `n!` operations when `n = 15`.

Which of these are realistic for an interactive application?

---

## Part C - Measuring Running Time

Use Python's `time.perf_counter()` for these exercises. Run each measurement at least 5 times and report minimum, average, and maximum time.

**Exercise 1.5 - Linear search timing**

Run this experiment:

```python
import time

def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

def measure(n):
    arr = list(range(n))
    target = n + 1       # absent target: worst case
    t0 = time.perf_counter()
    linear_search(arr, target)
    return time.perf_counter() - t0

for n in [1000, 10000, 100000, 1000000]:
    times = [measure(n) for _ in range(10)]
    print(n, min(times), sum(times) / len(times), max(times))
```

Answer:

1. Does time grow roughly linearly with `n`?
2. Are all 10 runs exactly the same? Why or why not?
3. Why is the absent target a worst-case input?
4. Why might `n = 1000` be too small to show a stable trend?

**Exercise 1.6 - Best case vs worst case**

Modify the previous experiment to measure:

1. target at the first position;
2. target at the last position;
3. target absent.

Use `n = 1_000_000`. Explain the difference.

**Exercise 1.7 - Binary search timing**

Implement binary search and compare it with linear search on sorted arrays:

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

Measure both algorithms for `n = 10^3, 10^4, 10^5, 10^6`. Use an absent target. Report:

1. comparison counts if you can instrument the code;
2. running times;
3. the input size where the timing difference becomes obvious.

**Exercise 1.8 - Timing can mislead**

Create two functions:

```python
def slow_constant(n):
    total = 0
    for _ in range(100000):
        total += 1
    return total

def linear(n):
    total = 0
    for _ in range(n):
        total += 1
    return total
```

Measure both for `n = 10, 1000, 100000, 1000000`.

Questions:

1. Which function is faster for small `n`?
2. Which function grows with `n`?
3. Why do constants matter in practice but disappear in asymptotic analysis?

---

## Part D - Counting Operations

**Exercise 1.9** Count the exact number of times the marked statement executes, then express the result using `Theta` notation.

```python
# (a)
total = 0
for i in range(n):
    total += i          # count this

# (b)
total = 0
for i in range(n):
    for j in range(n):
        total += i * j  # count this

# (c)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        count += 1      # count this

# (d)
i = n
while i > 1:
    i = i // 2          # count this

# (e)
count = 0
for i in range(n):
    for j in range(10):
        count += 1      # count this
```

**Exercise 1.10** Determine the tightest `Theta` bound:

1. `5n^3 + 100n^2 + n + 1000`
2. `n log n + 3n`
3. `2^(n+3) + n^5`
4. `log(n^10) + sqrt(n)`
5. `(n + 1)(n + 2) / 2`
6. `1000000n + n^2`
7. `n^2 / 1000000 + 500n`

For 6 and 7, also explain why small inputs may be misleading.

**Exercise 1.11 - Loop invariant**

The following algorithm computes `a^n` for integer `a > 0`, `n >= 0`:

```python
def power(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result
```

1. State a loop invariant.
2. Prove initialization, maintenance, and termination.
3. Analyze time complexity.
4. Analyze extra space complexity.

---

## Part E - Bad Algorithms for Simple Problems

**Exercise 1.12 - Fibonacci can take forever**

Compare:

```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

Tasks:

1. Measure both functions for `n = 10, 20, 30, 35`.
2. Do not run the recursive version for very large `n` if it becomes too slow.
3. Explain why the recursive algorithm repeats work.
4. Estimate what happens at `n = 50`.
5. Give the time complexity of each algorithm.

**Exercise 1.13 - Pair sum**

Problem: given a list of integers and a target sum `S`, decide whether two different elements sum to `S`.

1. Write a naive algorithm that checks every pair.
2. Write a faster algorithm using a set.
3. Analyze both algorithms.
4. Measure both for random lists of size `1000`, `10000`, and `100000`.
5. Explain why the naive algorithm becomes impractical.

**Exercise 1.14 - Multiplication motivation**

School multiplication of two `n`-digit integers uses about `n^2` single-digit products. Karatsuba multiplication uses about `n^1.585` work.

1. For `n = 10, 100, 1000, 1000000`, compare `n^2` and `n^1.585`.
2. Why is the difference small at first but enormous later?
3. Where might huge integer multiplication appear in practice?
4. Why is Karatsuba a good example of algorithm design even before we study divide and conquer formally?

---

## Part F - Starter Code Assignment

Open `week01/starter.py` and implement:

1. `linear_search`
2. `binary_search`
3. `find_min_max`
4. `insertion_sort`
5. `count_operations`

Then run:

```bash
python week01/starter.py
```

Submit:

1. your completed `starter.py`;
2. a screenshot or copied output of the auto-grader score;
3. a short paragraph describing one timing result that surprised you.

---

## Challenge Problems

**Exercise 1.15** Binary search runs in `O(log n)`. If a sorted array has `10^9` elements:

1. What is the maximum number of comparisons needed?
2. If one server can run `10^6` binary searches per second, how long does it take to process `10^12` queries?
3. How many such servers are needed to finish in one hour?

**Exercise 1.16** Prove or disprove: if `f(n) = O(g(n))` and `f(n) = Omega(g(n))`, then `f(n) = Theta(g(n))`.

**Exercise 1.17** Design an algorithm that finds both the minimum and maximum of an array using fewer than `2(n - 1)` comparisons. Hint: compare elements in pairs first.

**Exercise 1.18** Suppose algorithm A takes `1000n` operations and algorithm B takes `n^2` operations.

1. For which values of `n` is A faster?
2. For which values of `n` is B faster?
3. What lesson does this teach about Big-O and practical performance?
