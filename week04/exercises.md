# Week 4 Exercises — Divide and Conquer II: Recurrence Relations & Master Theorem

## Conceptual Questions

**Exercise 4.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 4.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 4.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 4.1** `quick_sort(list -> list)`
Implement quicksort with Lomuto partition. Return new sorted list.

Analyse the time and space complexity of your solution.

**Exercise 4.2** `power_dc(int,int -> int)`
Compute a^n using divide and conquer in O(log n).

Analyse the time and space complexity of your solution.

**Exercise 4.3** `find_peak(list -> int)`
Find a peak element (element >= neighbors) in O(log n).

Analyse the time and space complexity of your solution.

**Exercise 4.4** `closest_pair_1d(list -> tuple)`
Find closest pair of numbers in sorted array. Return (x,y,distance).

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 4.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 4.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 4.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 4.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
