# Week 7 Exercises — Dynamic Programming I: Introduction & Classic Problems

## Conceptual Questions

**Exercise 7.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 7.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 7.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 7.1** `fibonacci_dp(int -> int)`
Compute fib(n) using memoisation. O(n) time and space.

Analyse the time and space complexity of your solution.

**Exercise 7.2** `knapsack_01(list,list,int -> int)`
0/1 knapsack. weights,values lists, capacity. Return max value.

Analyse the time and space complexity of your solution.

**Exercise 7.3** `lcs_length(str,str -> int)`
Length of Longest Common Subsequence of two strings.

Analyse the time and space complexity of your solution.

**Exercise 7.4** `lcs_string(str,str -> str)`
Return the actual LCS string (not just length).

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 7.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 7.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 7.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 7.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
