# Week 11 Exercises — Graph Algorithms II: MST, Topological Sort & SCC

## Conceptual Questions

**Exercise 11.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 11.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 11.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 11.1** `prim_mst(dict -> int)`
Prim's MST using min-heap. graph=adj dict {u:[(v,w)]}. Return total weight.

Analyse the time and space complexity of your solution.

**Exercise 11.2** `topological_sort(dict -> list)`
Topological sort of DAG using DFS. Return sorted node list.

Analyse the time and space complexity of your solution.

**Exercise 11.3** `scc_kosaraju(dict -> int)`
Count SCCs using Kosaraju's algorithm.

Analyse the time and space complexity of your solution.

**Exercise 11.4** `bridges(dict -> list)`
Find all bridges (cut edges) in undirected graph.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 11.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 11.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 11.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 11.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
