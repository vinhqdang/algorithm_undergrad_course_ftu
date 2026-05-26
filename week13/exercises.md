# Week 13 Exercises — Advanced Topics II: More String Matching & NP-Completeness

## Conceptual Questions

**Exercise 13.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 13.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 13.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 13.1** `rabin_karp(str,str -> list)`
Rabin-Karp pattern matching using rolling hash. Return list of indices.

Analyse the time and space complexity of your solution.

**Exercise 13.2** `vertex_cover_approx(dict -> set)`
2-approximation for vertex cover. graph=adj set. Return cover set.

Analyse the time and space complexity of your solution.

**Exercise 13.3** `tsp_approx(list -> float)`
TSP approximation (nearest neighbor heuristic). Return tour length.

Analyse the time and space complexity of your solution.

**Exercise 13.4** `z_function(str -> list)`
Compute Z-function for string matching. Return Z array.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 13.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 13.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 13.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 13.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
