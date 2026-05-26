# Week 8 Exercises — Dynamic Programming II: More Problems & Midterm Review

## Conceptual Questions

**Exercise 8.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 8.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 8.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 8.1** `lis_length(list -> int)`
Length of Longest Increasing Subsequence. O(n^2) DP.

Analyse the time and space complexity of your solution.

**Exercise 8.2** `edit_distance(str,str -> int)`
Levenshtein edit distance between two strings.

Analyse the time and space complexity of your solution.

**Exercise 8.3** `coin_change_dp(list,int -> int)`
Coin change DP: min coins to make amount. Return -1 if impossible.

Analyse the time and space complexity of your solution.

**Exercise 8.4** `matrix_chain_order(list -> int)`
Matrix chain multiplication: return min scalar multiplications.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 8.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 8.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 8.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 8.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
