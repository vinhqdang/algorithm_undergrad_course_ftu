"""
Week 3 Starter Code — Divide and Conquer Algorithms
===================================================
Instructions:
  1. Implement each function marked with # TODO.
  2. Do NOT modify the auto-grader section at the bottom.
  3. Run this file: python starter.py
  4. You will see a score out of 100.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 1 (20 pts): Merge Sort
# ═══════════════════════════════════════════════════════════════════════════════

def merge_sort(arr: list) -> list:
    """
    Sorts a list in ascending order using Merge Sort.
    Input:
      arr: list of numbers
    Returns:
      a NEW sorted list (do not mutate the input array).
    """
    # TODO: implement recursive Merge Sort (preserving stability)
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 2 (20 pts): Quick Sort (In-Place)
# ═══════════════════════════════════════════════════════════════════════════════

def quicksort(arr: list, lo: int = 0, hi: int = None) -> list:
    """
    Sorts a list in ascending order in-place using Quick Sort.
    Input:
      arr: list of elements to be sorted (must be mutated in-place)
      lo: starting index (default: 0)
      hi: ending index (default: len(arr) - 1)
    Returns:
      the sorted list reference.
    """
    # TODO: implement recursive in-place Quick Sort (Lomuto or Hoare partitioning)
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 3 (20 pts): Inversion Counting
# ═══════════════════════════════════════════════════════════════════════════════

def count_inversions(arr: list) -> int:
    """
    Counts the number of inversions in an array.
    An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].
    Complexity: Must run in O(n log n) time.
    
    Input:
      arr: list of numbers
    Returns:
      integer count of inversions.
    """
    # TODO: implement modified Merge Sort to count crossing inversions in O(n log n)
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 4 (20 pts): Recursive Binary Search
# ═══════════════════════════════════════════════════════════════════════════════

def binary_search_rec(arr: list, target, lo: int = 0, hi: int = None) -> int:
    """
    Recursively searches for a target in a sorted list.
    
    Input:
      arr: sorted list of numbers
      target: the number to search for
      lo: lower index bound (default: 0)
      hi: upper index bound (default: len(arr) - 1)
    Returns:
      the 0-indexed position of target if found, else -1.
    """
    # TODO: implement recursive Binary Search in O(log n)
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 5 (20 pts): Maximum Subarray Sum
# ═══════════════════════════════════════════════════════════════════════════════

def max_subarray_dc(arr: list) -> int:
    """
    Finds the contiguous subarray within arr which has the largest sum.
    Complexity: Must run in O(n log n) time.
    
    Input:
      arr: list of numbers
    Returns:
      integer max subarray sum. Returns 0 if arr is empty.
    """
    # TODO: implement Divide and Conquer Maximum Subarray Sum in O(n log n)
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# ─────────────────────── AUTO-GRADER ─────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════════════════

def _run_tests():
    score = 0
    total = 100
    results = []

    # ── Problem 1: Merge Sort ────────────────────────────────────────────────
    p1 = 0
    try:
        orig = [5, 2, 4, 6, 1, 3]
        res1 = merge_sort(orig)
        assert res1 == [1, 2, 3, 4, 5, 6], "incorrect sorting result"
        assert orig == [5, 2, 4, 6, 1, 3], "merge_sort modified the input array!"
        assert merge_sort([]) == [], "empty list handling"
        assert merge_sort([42]) == [42], "single element handling"
        # Stability check
        stable_data = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
        # Sorted by number, stable should keep 'a' before 'c', and 'b' before 'd'
        sorted_stable = merge_sort(stable_data)
        assert sorted_stable == [(1, 'b'), (1, 'd'), (2, 'a'), (2, 'c')], "sort is not stable"
        p1 = 20
        results.append(("Problem 1 - Merge Sort", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 1 - Merge Sort", f"FAIL: {e}", 0, 20))
    score += p1

    # ── Problem 2: Quick Sort ────────────────────────────────────────────────
    p2 = 0
    try:
        orig2 = [5, 2, 4, 6, 1, 3]
        res2 = quicksort(orig2)
        assert res2 == [1, 2, 3, 4, 5, 6], "incorrect sorting result"
        assert orig2 == [1, 2, 3, 4, 5, 6], "quicksort failed to sort in-place!"
        assert quicksort([]) == [], "empty list handling"
        assert quicksort([42]) == [42], "single element handling"
        p2 = 20
        results.append(("Problem 2 - Quick Sort", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 2 - Quick Sort", f"FAIL: {e}", 0, 20))
    score += p2

    # ── Problem 3: Inversion Counting ────────────────────────────────────────
    p3 = 0
    try:
        assert count_inversions([2, 1, 3]) == 1, "basic swap"
        assert count_inversions([3, 2, 1]) == 3, "reverse sorted"
        assert count_inversions([1, 2, 3]) == 0, "already sorted"
        assert count_inversions([1, 3, 5, 2, 4, 6]) == 3, "partial overlaps"
        assert count_inversions([]) == 0, "empty list"
        p3 = 20
        results.append(("Problem 3 - Inversion Counting", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 3 - Inversion Counting", f"FAIL: {e}", 0, 20))
    score += p3

    # ── Problem 4: Recursive Binary Search ───────────────────────────────────
    p4 = 0
    try:
        arr = [1, 2, 3, 4, 5]
        assert binary_search_rec(arr, 3) == 2, "found in middle"
        assert binary_search_rec(arr, 6) == -1, "not found (larger)"
        assert binary_search_rec(arr, 0) == -1, "not found (smaller)"
        assert binary_search_rec(arr, 1) == 0, "found at start"
        assert binary_search_rec(arr, 5) == 4, "found at end"
        assert binary_search_rec([], 10) == -1, "empty list"
        p4 = 20
        results.append(("Problem 4 - Binary Search", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 4 - Binary Search", f"FAIL: {e}", 0, 20))
    score += p4

    # ── Problem 5: Maximum Subarray Sum ──────────────────────────────────────
    p5 = 0
    try:
        assert max_subarray_dc([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "standard mixed array"
        assert max_subarray_dc([5, 4, -1, 7, 8]) == 23, "all positive"
        assert max_subarray_dc([-1, -2, -3]) == -1, "all negative"
        assert max_subarray_dc([]) == 0, "empty list"
        p5 = 20
        results.append(("Problem 5 - Max Subarray Sum", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 5 - Max Subarray Sum", f"FAIL: {e}", 0, 20))
    score += p5

    # ── Report ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 62)
    print("  WEEK 3 AUTO-GRADER RESULTS")
    print("=" * 62)
    for name, status, pts, max_pts in results:
        mark = "[PASS]" if "PASS" in status else "[FAIL]"
        print(f"  {mark} {name:<35} {pts:>3}/{max_pts}")
        if "FAIL" in status:
            print(f"      -> {status[5:]}")
    print("-" * 62)
    print(f"  TOTAL SCORE: {score}/{total}  ({score}%)")
    if score == total:
        print("  Perfect score! Excellent work!")
    elif score >= 80:
        print("  Good job! Review the failed tests.")
    else:
        print("  Keep practicing. Re-read the lecture notes.")
    print("=" * 62 + "\n")
    return score


if __name__ == "__main__":
    _run_tests()
