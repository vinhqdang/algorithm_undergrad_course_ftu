# Week 6 Exercises — Greedy Algorithms II: Graph Applications & Correctness

## Conceptual Questions

**Exercise 6.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 6.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 6.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 6.1** `kruskal_mst(list,int -> list)`
Kruskal's MST. Graph as edge list [(u,v,weight)], n nodes. Return MST edges.

Analyse the time and space complexity of your solution.

**Exercise 6.2** `dijkstra(dict,int -> dict)`
Dijkstra's algorithm. graph=adj dict, source=int. Return dist dict.

Analyse the time and space complexity of your solution.

**Exercise 6.3** `union_find_with_rank(class with find/union methods)`
Union-Find with union-by-rank and path compression.

Analyse the time and space complexity of your solution.

**Exercise 6.4** `job_scheduling(list -> int)`
Schedule jobs to maximise profit. jobs=[(deadline,profit)]. Return max profit.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 6.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 6.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 6.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 6.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
