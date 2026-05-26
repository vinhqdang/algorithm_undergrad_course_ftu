# Week 10 Exercises — Graph Algorithms I: Traversals & Shortest Paths

## Conceptual Questions

**Exercise 10.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 10.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 10.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 10.1** `bfs(dict,int -> list)`
BFS traversal. graph=adj dict, start=int. Return visited order.

Analyse the time and space complexity of your solution.

**Exercise 10.2** `dfs(dict,int -> list)`
DFS traversal (iterative). graph=adj dict, start=int. Return visited order.

Analyse the time and space complexity of your solution.

**Exercise 10.3** `bellman_ford(list,int,int -> dict|str)`
Bellman-Ford. graph=edge list [(u,v,w)], n=nodes, src. Return dist or 'NEGATIVE CYCLE'.

Analyse the time and space complexity of your solution.

**Exercise 10.4** `has_cycle_directed(dict -> bool)`
Detect cycle in directed graph using DFS. Return bool.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 10.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 10.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 10.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 10.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
