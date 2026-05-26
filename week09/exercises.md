# Week 9 Exercises — Dynamic Programming III: Tabulation & Advanced Techniques

## Conceptual Questions

**Exercise 9.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 9.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 9.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 9.1** `longest_palindromic_subsequence(str -> int)`
Length of longest palindromic subsequence.

Analyse the time and space complexity of your solution.

**Exercise 9.2** `word_break(str,list -> bool)`
Can string s be segmented using words from wordDict? Return bool.

Analyse the time and space complexity of your solution.

**Exercise 9.3** `max_profit_stock(list,int -> int)`
Best time to buy/sell stock k times. Return max profit.

Analyse the time and space complexity of your solution.

**Exercise 9.4** `unique_paths(int,int -> int)`
Count unique paths in m×n grid (can only move right or down).

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 9.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 9.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 9.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 9.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
