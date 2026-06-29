# LeetCode Practice Problems

**TOAE209/TOAH209 — Design and Analysis of Algorithms**
*Foreign Trade University · Department of Technology & Data Science*

This file maps each week of the course onto a curated set of [LeetCode](https://leetcode.com)
problems so you can practise the week's techniques on real interview-style problems.

**How to use it.** After you finish a week's `notes/`, `theory/`, and `exercises/`,
work through that week's LeetCode list below. Each problem links directly to LeetCode.
Difficulty is LeetCode's own label (🟢 Easy, 🟡 Medium, 🔴 Hard). Start with the Easy/Medium
ones; the Hard problems are stretch goals that combine several ideas.

> The same lists are reproduced inside each week's `exercises/practical_exercises.tex`
> (section "LeetCode Practice"), so they are available both on GitHub and in the compiled PDF.

---

## Week 1 — Introduction, Stable Matching & Data Structures

Stable matching itself is not on LeetCode, so this list drills the supporting data
structures (stacks, queues, heaps, linked lists) and warm-up tools (binary search, recursion).

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟢 Easy | Stack |
| [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium | Stack |
| [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | 🟢 Easy | Stack / Queue |
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟢 Easy | Linked list |
| [Binary Search](https://leetcode.com/problems/binary-search/) | 🟢 Easy | Binary search |
| [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | 🟢 Easy | Recursion / memoization |
| [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | 🟢 Easy | Binary heap |
| [Sort an Array](https://leetcode.com/problems/sort-an-array/) | 🟡 Medium | Heapsort / sorting |

---

## Week 2 — Algorithm Analysis & Asymptotics (Binary Search)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | 🟢 Easy | Binary search |
| [First Bad Version](https://leetcode.com/problems/first-bad-version/) | 🟢 Easy | Binary search on answer |
| [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | 🟢 Easy | Binary search |
| [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 🟡 Medium | Binary search (bounds) |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟡 Medium | Binary search |
| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟡 Medium | Binary search |
| [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟡 Medium | Two pointers |
| [Majority Element](https://leetcode.com/problems/majority-element/) | 🟢 Easy | Boyer–Moore / counting |

---

## Week 3 — Graphs, BFS/DFS & Union-Find

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | BFS / DFS |
| [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium | BFS / DFS |
| [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 🟡 Medium | Multi-source BFS |
| [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | Topological sort |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium | Topological sort |
| [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | 🟡 Medium | Union-Find |
| [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | 🟡 Medium | Union-Find |
| [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟡 Medium | Union-Find |
| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | 🟡 Medium | Union-Find |
| [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟡 Medium | DFS / BFS |

---

## Week 4 — Greedy Algorithms I (Interval Scheduling & Partitioning)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | 🟡 Medium | Earliest-finish-time greedy |
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟡 Medium | Sort + sweep |
| [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | 🟢 Easy | Interval overlap |
| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | 🟡 Medium | Interval partitioning |
| [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | 🟡 Medium | Interval greedy |
| [Jump Game](https://leetcode.com/problems/jump-game/) | 🟡 Medium | Greedy reachability |
| [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | 🟡 Medium | Greedy / BFS |
| [Gas Station](https://leetcode.com/problems/gas-station/) | 🟡 Medium | Greedy |
| [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | 🟡 Medium | Greedy + counting |
| [Partition Labels](https://leetcode.com/problems/partition-labels/) | 🟡 Medium | Greedy intervals |

---

## Week 5 — Greedy Algorithms II (Dijkstra & Minimum Spanning Trees)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium | Dijkstra |
| [Path with Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | 🟡 Medium | Dijkstra / binary search |
| [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium | Dijkstra / Bellman–Ford |
| [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | 🔴 Hard | Dijkstra / union-find |
| [Path With Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | 🟡 Medium | Dijkstra variant |
| [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 🟡 Medium | MST (Prim / Kruskal) |
| [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) | 🟡 Medium | MST (Kruskal) |
| [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 🟡 Medium | Shortest paths |
| [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | 🔴 Hard | Greedy / Hierholzer |

---

## Week 6 — Divide & Conquer I (Merge Sort & Recurrences)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Sort an Array](https://leetcode.com/problems/sort-an-array/) | 🟡 Medium | Merge sort / quicksort |
| [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | 🟢 Easy | Merge |
| [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard | Divide & conquer merge |
| [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | 🔴 Hard | Merge sort (inversions) |
| [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | 🔴 Hard | Merge sort (inversions) |
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟡 Medium | Divide & conquer |
| [Pow(x, n)](https://leetcode.com/problems/powx-n/) | 🟡 Medium | Fast exponentiation |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | Quickselect |
| [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) | 🟡 Medium | Divide & conquer |

---

## Week 7 — Divide & Conquer II (Closest Pair, FFT & Big-Integer Multiplication)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | Binary search D&C |
| [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | 🟡 Medium | Divide & conquer |
| [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | 🟡 Medium | Binary search on answer |
| [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) | 🔴 Hard | Binary search + sorting |
| [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | 🔴 Hard | Divide & conquer |
| [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) | 🔴 Hard | Merge sort |
| [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | 🟡 Medium | Big-integer multiplication |
| [Super Pow](https://leetcode.com/problems/super-pow/) | 🟡 Medium | Fast exponentiation |

---

## Week 8 — Dynamic Programming I (Weighted Interval Scheduling & Knapsack)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 Easy | 1-D DP |
| [House Robber](https://leetcode.com/problems/house-robber/) | 🟡 Medium | 1-D DP |
| [House Robber II](https://leetcode.com/problems/house-robber-ii/) | 🟡 Medium | 1-D DP |
| [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 Medium | Unbounded knapsack |
| [Coin Change II](https://leetcode.com/problems/coin-change-2/) | 🟡 Medium | Counting knapsack |
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 🟡 Medium | 0/1 knapsack |
| [Target Sum](https://leetcode.com/problems/target-sum/) | 🟡 Medium | 0/1 knapsack |
| [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | 🟡 Medium | 2-D knapsack |
| [Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) | 🔴 Hard | Weighted interval scheduling |
| [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 🟡 Medium | State-machine DP |

---

## Week 9 — Dynamic Programming II (Sequence Alignment & Shortest Paths)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 🟡 Medium | 2-D DP |
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🟡 Medium | Sequence alignment |
| [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | 🟡 Medium | LCS variant |
| [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | 🟡 Medium | Sequence alignment |
| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | 🔴 Hard | 2-D DP |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟡 Medium | DP / patience sorting |
| [Unique Paths](https://leetcode.com/problems/unique-paths/) | 🟡 Medium | Grid DP |
| [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | 🟡 Medium | Grid DP |
| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard | 2-D DP |
| [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium | Bellman–Ford DP |

---

## Week 10 — Network Flow I (Max-Flow / Min-Cut)

Pure max-flow problems are uncommon on LeetCode; these are problems that are naturally
modelled as flow, min-cut, or bipartite matching.

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Maximum Bipartite Matching → Maximum Number of Achievable Transfer Requests](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/) | 🔴 Hard | Flow / enumeration |
| [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/) | 🔴 Hard | Matching / bitmask |
| [Minimum Cost to Connect Two Groups of Points](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/) | 🔴 Hard | Assignment / min-cost matching |
| [Campus Bikes II](https://leetcode.com/problems/campus-bikes-ii/) | 🟡 Medium | Assignment (min-cost matching) |
| [Pizza With 3n Slices](https://leetcode.com/problems/pizza-with-3n-slices/) | 🔴 Hard | Matching-style DP |
| [Escape the Spreading Fire](https://leetcode.com/problems/escape-the-spreading-fire/) | 🔴 Hard | BFS + min-cut intuition |

---

## Week 11 — Network Flow II/III (Bipartite Matching & Flow Applications)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | 🟡 Medium | Bipartite check |
| [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) | 🟡 Medium | Bipartite check |
| [Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) | 🟡 Medium | Bipartite matching |
| [Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/) | 🔴 Hard | Flow / search |
| [Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) | 🟡 Medium | Graph application |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium | DAG application |

---

## Week 12 — Intractability (NP-Completeness, Reductions & Backtracking)

NP-complete problems are attacked here with exponential backtracking/branch-and-bound.

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Subsets](https://leetcode.com/problems/subsets/) | 🟡 Medium | Backtracking |
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟡 Medium | Backtracking |
| [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | 🟡 Medium | Backtracking |
| [Word Search](https://leetcode.com/problems/word-search/) | 🟡 Medium | Backtracking |
| [N-Queens](https://leetcode.com/problems/n-queens/) | 🔴 Hard | Backtracking |
| [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | 🔴 Hard | Constraint backtracking |
| [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | 🟡 Medium | NP-hard (subset-sum) |
| [Flower Planting With No Adjacent](https://leetcode.com/problems/flower-planting-with-no-adjacent/) | 🟡 Medium | Graph coloring |
| [Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/) | 🔴 Hard | TSP / bitmask DP |

---

## Week 13 — PSPACE & Extending Tractability (FPT, Game Search, Branch & Bound)

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🔴 Hard | State-space BFS |
| [Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/) | 🔴 Hard | State-space search |
| [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/) | 🔴 Hard | Set cover (FPT / bitmask) |
| [Stone Game](https://leetcode.com/problems/stone-game/) | 🟡 Medium | Game / minimax DP |
| [Stone Game II](https://leetcode.com/problems/stone-game-ii/) | 🟡 Medium | Game / minimax DP |
| [Can I Win](https://leetcode.com/problems/can-i-win/) | 🟡 Medium | Game search + memo |
| [Cat and Mouse](https://leetcode.com/problems/cat-and-mouse/) | 🔴 Hard | PSPACE game (BFS on states) |
| [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/) | 🔴 Hard | Bitmask FPT |

---

## Week 14 — Approximation & Local Search

Optimization problems attacked via greedy approximation, binary-search-on-the-answer,
and local-search heuristics.

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 🟡 Medium | Binary search on answer |
| [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | 🟡 Medium | Binary search on answer |
| [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | 🔴 Hard | Binary search on answer |
| [Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) | 🔴 Hard | Binary search on answer |
| [Minimize the Maximum Difference of Pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/) | 🟡 Medium | Binary search + greedy |
| [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) | 🔴 Hard | Greedy + heap |
| [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/) | 🔴 Hard | Set cover approximation |
| [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | 🟡 Medium | Greedy cover |

---

## Week 15 — Randomized Algorithms

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) | 🟡 Medium | Fisher–Yates shuffle |
| [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | 🟡 Medium | Prefix sums + binary search |
| [Random Pick Index](https://leetcode.com/problems/random-pick-index/) | 🟡 Medium | Reservoir sampling |
| [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) | 🟡 Medium | Reservoir sampling |
| [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | 🟡 Medium | Randomized data structure |
| [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/) | 🟡 Medium | Rejection sampling |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | Randomized quickselect |
| [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | 🟡 Medium | Weighted random sampling |

---

*Difficulty labels follow LeetCode at the time of writing and may change. Some problems
require a LeetCode subscription. Last updated for the 2025–2026 academic year.*
