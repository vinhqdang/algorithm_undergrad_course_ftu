# Week 3 Exercises — Divide and Conquer Algorithms

This week's exercises cover the Divide and Conquer (D&C) paradigm, classical sorting algorithms (Merge Sort, Quick Sort), recurrence relations, and key applications.

---

## Conceptual Questions

**Exercise 3.C1: The Divide & Conquer Core Steps**
Briefly describe the three steps of the Divide and Conquer paradigm. For each of the following algorithms, identify what work is done in the **Divide** step and what work is done in the **Combine** step:
- (a) **Merge Sort**
- (b) **Quick Sort**
- (c) **Binary Search**

**Exercise 3.C2: Sorting Algorithmic Trade-Offs**
Compare **Merge Sort** and **Quick Sort** across the following dimensions. Explain the trade-offs:
- Time Complexity (best, average, worst case)
- Space Complexity (in-place vs. auxiliary allocation)
- Algorithmic Stability (stable vs. unstable)
- Cache Locality (locality of reference)

**Exercise 3.C3: Quick Sort Worst-Case Inputs**
Explain why Quicksort with a **Lomuto partition** using the last element as the pivot exhibits a $\Theta(n^2)$ worst-case runtime when given an array that is **already sorted** or **reverse sorted**.
- Draw the partition tree for the array `[1, 2, 3, 4]`.
- How does choosing a **random pivot** mitigate this problem?

**Exercise 3.C4: Recurrence Complexity Classes**
Contrast the following recurrence relations and rank their growth classes from slowest to fastest:
1. $T(n) = T(n/2) + \mathcal{O}(1)$
2. $T(n) = 2T(n/2) + \mathcal{O}(1)$
3. $T(n) = 2T(n/2) + \mathcal{O}(n)$
4. $T(n) = 3T(n/2) + \mathcal{O}(n)$
5. $T(n) = 4T(n/2) + \mathcal{O}(n^2)$

---

## Programming Problems

Implement the following functions in `starter.py` and run the file to verify correctness.

### Exercise 3.1: Merge Sort
* **Function:** `merge_sort(arr: list) -> list`
* **Input:** A list of numbers.
* **Output:** A **NEW** sorted list in ascending order.
* **Constraints:** Must not mutate the original list. The sorting must be **stable** (equal elements keep their relative order).

### Exercise 3.2: Quick Sort (In-Place)
* **Function:** `quicksort(arr: list, lo: int, hi: int) -> list`
* **Input:** A list of numbers `arr`, and optional bounds `lo` and `hi`.
* **Output:** The **same** array `arr`, sorted in-place in ascending order.
* **Requirements:** Sort the array in-place. The function should mutate the input array directly. Use Lomuto or Hoare partitioning.

### Exercise 3.3: Inversion Counting
* **Function:** `count_inversions(arr: list) -> int`
* **Input:** A list of numbers.
* **Output:** An integer count of the total number of inversions in the array (pairs $i < j$ such that $arr[i] > arr[j]$).
* **Constraints:** Must run in $\mathcal{O}(n \log n)$ time using a modified Merge Sort combine step.

### Exercise 3.4: Recursive Binary Search
* **Function:** `binary_search_rec(arr: list, target, lo: int, hi: int) -> int`
* **Input:** A sorted list of numbers `arr`, and the search `target`.
* **Output:** The 0-indexed position of `target` if found, else `-1`.
* **Constraints:** Must be implemented recursively in $\mathcal{O}(\log n)$ time.

### Exercise 3.5: Maximum Subarray Sum
* **Function:** `max_subarray_dc(arr: list) -> int`
* **Input:** A list of numbers (mixed positive and negative).
* **Output:** The contiguous subarray sum which has the largest sum.
* **Constraints:** Solve using a Divide and Conquer approach in $\Theta(n \log n)$ time.

---

## Proof & Analysis Problems

**Exercise 3.A1: Mathematical Induction for Merge Sort Correctness**
State the induction hypothesis and prove that `merge_sort` correctly sorts an array of size $n$:
- **Base Case:** Prove correctness for $n \le 1$.
- **Inductive Step:** Assuming `merge_sort` correctly sorts arrays of size $k < n$, prove it correctly sorts an array of size $n$ using the correctness of the linear `merge` combine operation.

**Exercise 3.A2: Recurrence Solving via Master Theorem**
State the Master Theorem and use it to find the tight asymptotic bound ($\Theta$) for the following recurrences. Identify which Case (1, 2, or 3) applies:
- (a) $T(n) = 3T(n/2) + \Theta(n)$
- (b) $T(n) = 4T(n/2) + \Theta(n^2)$
- (c) $T(n) = 2T(n/4) + \Theta(1)$
- (d) $T(n) = 8T(n/2) + \Theta(n^3)$

---

## Challenge Problems ★

**Exercise 3.★1: Quickselect Expected Linear Selection**
The **Quickselect** algorithm is a Divide & Conquer variant of Quicksort used to find the $k$-th smallest element in an unsorted list.
- Implement `quickselect(arr, k)` in Python.
- Why is the expected runtime of Quickselect $\mathcal{O}(n)$ rather than $\mathcal{O}(n \log n)$?
- State its recurrence relation for the expected best-case split and solve it.

**Exercise 3.★2: Karatsuba Integer Multiplication**
Standard grade-school multiplication of two $n$-digit numbers costs $\mathcal{O}(n^2)$ single-digit multiplications.
- Read about **Karatsuba's algorithm** which divides each number into two halves of $n/2$ digits and expresses the product using only **three** recursive multiplications of size $n/2$ instead of four.
- Write down Karatsuba's recurrence relation:
  $$T(n) = 3T(n/2) + \Theta(n)$$
- Solve this recurrence via the Master Theorem to show that it runs in $\Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$ time.
