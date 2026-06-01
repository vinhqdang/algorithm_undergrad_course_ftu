# Week 5 Exercises — Greedy Algorithms I: Principles & Classic Examples

This week's exercises cover the greedy algorithmic paradigm and 5 classic greedy algorithms derived from the Princeton (Kleinberg-Tardos) curriculum.

---

## Conceptual Questions

**Exercise 5.C1: Greedy Strategy & Counter-examples**
For the **Interval Scheduling** problem, we greedily sorted intervals by earliest *finish time* and obtained an optimal solution. Consider the following alternate greedy strategies. Construct a small counter-example (using 3 or 4 intervals) for each strategy to prove it does not always produce the maximum size subset of compatible intervals:
- **Strategy A:** Select the interval that starts earliest (Earliest Start Time First).
- **Strategy B:** Select the interval with the shortest duration ($f_i - s_i$ is minimized).
- **Strategy C:** Select the interval with the fewest conflicts (overlaps with the fewest other remaining intervals).

**Exercise 5.C2: Coin Changing Optimality**
The greedy coin-changing algorithm is optimal for the US coin system ($25, 10, 5, 1$) and Euro systems.
- Explain why the greedy algorithm fails to find the minimum number of coins for the coin system $C = \{4, 3, 1\}$ when changing the amount $A = 6$.
- What is the optimal selection of coins for $A = 6$ under $C$, and what does greedy return?

**Exercise 5.C3: Interval Partitioning Depth & Lower Bound**
In **Interval Partitioning**, the goal is to schedule all intervals using the minimum number of classrooms/rooms such that no two overlapping intervals are in the same classroom.
- Define what is meant by the **depth** of a set of intervals.
- Explain why the depth of a set of intervals represents a mathematical *lower bound* on the number of classrooms any valid schedule must use.

**Exercise 5.C4: Furthest-in-Future (FIF) Optimal Caching**
- Describe the Furthest-in-Future (FIF) cache replacement policy in your own words.
- Why is FIF considered an *offline* caching policy rather than an *online* caching policy? Can a real operating system or web browser use FIF directly? Why or why not?

---

## Programming Problems

Implement the following functions in `starter.py` and run the file to verify correctness.

### Exercise 5.1: Greedy Coin Changing
* **Function:** `coin_changing_greedy(amount: int, coins: list) -> list`
* **Input:** A non-negative integer `amount` and a list of positive integers `coins` representing coin denominations.
* **Output:** A list of coins selected to sum exactly to `amount`, sorted in descending order.
* **Requirements:** At each step, greedily select the largest coin denomination less than or equal to the remaining amount. Raise a `ValueError` if the amount cannot be made.

### Exercise 5.2: Interval Scheduling
* **Function:** `interval_scheduling(intervals: list) -> list`
* **Input:** A list of intervals represented as tuples `(start, end)`.
* **Output:** A list of indices of the selected intervals in their original input order (e.g. `[0, 3, 7]`).
* **Complexity:** Time complexity must be $\mathcal{O}(n \log n)$ and extra space complexity must be $\mathcal{O}(n)$.

### Exercise 5.3: Interval Partitioning
* **Function:** `interval_partitioning(intervals: list) -> tuple`
* **Input:** A list of intervals represented as tuples `(start, end)`.
* **Output:** A tuple `(num_rooms, assignment)` where `num_rooms` is the minimum classrooms needed, and `assignment` is a list of room IDs (0-indexed) allocated to each interval matching the input order.
* **Hint:** Sort intervals by start time. Use a min-heap to keep track of the earliest finishing time in each active classroom.

### Exercise 5.4: Scheduling to Minimize Lateness
* **Function:** `minimize_lateness(jobs: list) -> tuple`
* **Input:** A list of jobs represented as tuples `(duration, deadline)`.
* **Output:** A tuple `(max_lateness, schedule)` where `max_lateness` is the maximum lateness achieved, and `schedule` is a list of tuples `(orig_idx, start_time, finish_time)` representing the optimal order of execution.
* **Rule:** Sort by deadline (Earliest Deadline First).

### Exercise 5.5: Optimal Offline Caching (Furthest-in-Future)
* **Function:** `optimal_caching(requests: list, cache_size: int) -> int`
* **Input:** A list of requested page IDs (can be strings or numbers) and the integer `cache_size`.
* **Output:** The total number of cache misses under the optimal Furthest-in-Future replacement policy.

---

## Proof & Analysis Problems

**Exercise 5.A1: "Greedy Stays Ahead" Proof for Interval Scheduling**
Prove the optimality of the earliest finish-time first strategy for Interval Scheduling.
- Let $A = \{i_1, i_2, \ldots, i_k\}$ be the set of intervals selected by the greedy algorithm.
- Let $O = \{j_1, j_2, \ldots, j_m\}$ be the set of intervals selected by an optimal solution.
- Prove by induction that for all $r \le k$, the finish time of the $r$-th greedy interval is less than or equal to the finish time of the $r$-th optimal interval:
  $$f(i_r) \le f(j_r)$$
- Conclude that $k = m$ (greedy selects the maximum number of intervals).

**Exercise 5.A2: Inversion / Exchange Argument for Minimizing Lateness**
In the Scheduling to Minimize Lateness problem:
- Define an **inversion** in a schedule as a pair of jobs $i$ and $j$ such that job $i$ is scheduled *before* job $j$, but job $j$ has an earlier deadline ($d_j < d_i$).
- Show that any schedule with an inversion can be transformed by swapping adjacent inverted jobs without increasing the maximum lateness.
- Explain how this exchange argument proves that the Earliest Deadline First (EDF) greedy order is optimal.

---

## Challenge Problems ★

**Exercise 5.★1: General Optimal Coin Changing (Dynamic Programming)**
Since the greedy coin-changing algorithm is not optimal for arbitrary coin systems (like $C = \{4, 3, 1\}$), design an algorithm using **Dynamic Programming** that solves the optimal coin changing problem (minimizing total coins used) for *any* set of coin denominations and any amount.
- State the recurrence relation.
- What is the time complexity of the dynamic programming solution compared to the greedy version?

**Exercise 5.★2: Online Cache Competitive Ratios**
In practice, caching is an *online* problem where requests arrive one-by-one and the future is unknown.
- Read about the Least Recently Used (LRU) and First-In First-Out (FIFO) replacement algorithms.
- Explain the concept of a **competitive ratio** in online algorithms.
- Why can no deterministic online caching algorithm have a competitive ratio better than $k$ (where $k$ is the cache size) against an offline adversary that knows the future (and uses Furthest-in-Future)?
