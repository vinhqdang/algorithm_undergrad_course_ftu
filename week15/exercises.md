# Week 15 Exercises — Heuristics: Genetic Algorithms & Simulated Annealing

## Conceptual Questions

**Exercise 15.C1** Describe the main algorithmic ideas covered this week in your own words.
What are the key invariants or properties that make each algorithm correct?

**Exercise 15.C2** Compare the algorithms from this week:
- When would you choose one over another?
- What are the trade-offs in time complexity, space complexity, and implementation complexity?

**Exercise 15.C3** Trace through each algorithm by hand on a small example (n ≤ 8).
Draw the state at each step.

## Programming Problems

**Exercise 15.1** `simulated_annealing_tsp(list -> float)`
SA for TSP. cities=list of (x,y). Return best tour length found.

Analyse the time and space complexity of your solution.

**Exercise 15.2** `genetic_algorithm_onemax(int -> int)`
GA to maximise number of 1s in bitstring (OneMax). Return best fitness.

Analyse the time and space complexity of your solution.

**Exercise 15.3** `hill_climbing(callable,float -> float)`
Hill climbing for function maximisation. f=callable, x0=start. Return best x.

Analyse the time and space complexity of your solution.

**Exercise 15.4** `ant_colony_demo(list,list -> list)`
Simulate one iteration of ACO pheromone update on TSP. Return updated pheromone matrix.

Analyse the time and space complexity of your solution.


## Analysis Problems

**Exercise 15.A1** For each algorithm covered this week:
- (a) Prove correctness using a loop invariant or inductive argument
- (b) Derive the exact recurrence relation (if applicable)
- (c) Solve the recurrence to get the closed-form complexity

**Exercise 15.A2** Construct a worst-case input for each algorithm. What is the worst-case
complexity? Is there a gap between best and worst case?

## Challenge Problems ★

**Exercise 15.★1** Optimise one of the algorithms to reduce its space complexity.
Can you achieve in-place operation?

**Exercise 15.★2** Research a practical application where the algorithms from this week
are used in production systems. Describe how they are adapted.
