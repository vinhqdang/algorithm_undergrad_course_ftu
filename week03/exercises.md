# Week 3 Exercises — Divide and Conquer I: Merge Sort, Quick Sort, Recursion

## Conceptual Questions

**Exercise 3.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 3.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 3.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 3.1** `merge_sort(list -> list)`
Sort a list using merge sort. Return new sorted list. O(n log n).

Analyse the time and space complexity of your solution.

**Exercise 3.2** `count_inversions(list -> int)`
Count inversions in array (pairs i<j where A[i]>A[j]) using merge sort. O(n log n).

Analyse the time and space complexity of your solution.

**Exercise 3.3** `binary_search_recursive(list,int -> int)`
Recursive binary search. Return index or -1.

Analyse the time and space complexity of your solution.

**Exercise 3.4** `max_subarray_dc(list -> int)`
Find max subarray sum using divide and conquer (Kadane's variant). O(n log n).

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 3.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 3.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 3.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 3.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
