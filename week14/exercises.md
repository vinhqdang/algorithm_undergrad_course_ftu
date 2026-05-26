# Week 14 Exercises — Randomised Algorithms: Las Vegas & Monte Carlo

## Conceptual Questions

**Exercise 14.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 14.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 14.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 14.1** `randomised_quicksort(list -> list)`
Quicksort with random pivot. Must run in O(n log n) expected.

Analyse the time and space complexity of your solution.

**Exercise 14.2** `quickselect(list,int -> int)`
Find k-th smallest element in O(n) expected using QuickSelect.

Analyse the time and space complexity of your solution.

**Exercise 14.3** `monte_carlo_pi(int -> float)`
Estimate π using Monte Carlo simulation with n samples.

Analyse the time and space complexity of your solution.

**Exercise 14.4** `randomised_primality(int,int -> bool)`
Miller-Rabin primality test (randomised). Return True if probably prime.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 14.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 14.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 14.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 14.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
