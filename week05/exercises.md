# Week 5 Exercises — Greedy Algorithms I: Principles & Classic Examples

## Conceptual Questions

**Exercise 5.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 5.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 5.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 5.1** `activity_selection(list -> list)`
Select maximum non-overlapping activities. Input: list of (start,end). Return selected indices.

Analyse the time and space complexity of your solution.

**Exercise 5.2** `fractional_knapsack(list,int -> float)`
Solve fractional knapsack. items=[(weight,value)], capacity=int. Return max value.

Analyse the time and space complexity of your solution.

**Exercise 5.3** `coin_change_greedy(int,list -> list)`
Greedy coin change (works for canonical systems). Return min coins list.

Analyse the time and space complexity of your solution.

**Exercise 5.4** `min_platforms(list,list -> int)`
Find minimum train platforms needed. Input: arrivals,departures lists. Return int.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 5.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 5.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 5.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 5.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
