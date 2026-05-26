# Week 12 Exercises — Advanced Topics I: Network Flow & String Matching

## Conceptual Questions

**Exercise 12.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 12.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 12.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 12.1** `ford_fulkerson(list,int,int -> int)`
Ford-Fulkerson max flow. graph=capacity matrix, source, sink. Return max flow.

Analyse the time and space complexity of your solution.

**Exercise 12.2** `kmp_search(str,str -> list)`
KMP pattern matching. Return list of start indices where pattern found.

Analyse the time and space complexity of your solution.

**Exercise 12.3** `build_failure_function(str -> list)`
Build KMP failure function (prefix function) for pattern.

Analyse the time and space complexity of your solution.

**Exercise 12.4** `bipartite_matching(dict,set,set -> int)`
Max bipartite matching using augmenting paths. Return matching size.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 12.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 12.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 12.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 12.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
