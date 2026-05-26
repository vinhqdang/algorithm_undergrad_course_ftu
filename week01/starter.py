"""
Week 1 — Starter Code with Auto-Grader
=======================================
Instructions:
  1. Implement each function marked with  # TODO
  2. Do NOT modify the grading section at the bottom.
  3. Run this file:  python week01_starter.py
  4. You will see a score out of 100.
"""

import time, random, math

# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 1 (20 pts): Linear Search
# ═══════════════════════════════════════════════════════════════════════════════

def linear_search(arr: list, target) -> int:
    """
    Search for `target` in unsorted list `arr`.
    Return the index of target if found, else return -1.
    Time complexity must be O(n).
    """
    # TODO: implement linear search
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 2 (20 pts): Binary Search
# ═══════════════════════════════════════════════════════════════════════════════

def binary_search(arr: list, target) -> int:
    """
    Search for `target` in SORTED list `arr`.
    Return the index of target if found, else return -1.
    Time complexity must be O(log n). Use iteration, not recursion.
    """
    # TODO: implement binary search
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 3 (20 pts): Find Maximum and Minimum
# ═══════════════════════════════════════════════════════════════════════════════

def find_min_max(arr: list) -> tuple:
    """
    Return (minimum, maximum) of arr using at most ceil(3n/2) - 2 comparisons.
    Hint: process elements in pairs.
    Do NOT use Python built-ins min() or max().
    """
    # TODO: implement efficient min-max finding
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 4 (20 pts): Insertion Sort
# ═══════════════════════════════════════════════════════════════════════════════

def insertion_sort(arr: list) -> list:
    """
    Sort the list in ascending order using insertion sort.
    Return a NEW sorted list (do not modify the input).
    Time complexity: O(n²). Must be stable (equal elements keep original order).
    """
    # TODO: implement insertion sort
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 5 (20 pts): Count Operations
# ═══════════════════════════════════════════════════════════════════════════════

def count_operations(n: int) -> dict:
    """
    For the nested loop below, count the EXACT number of times
    'inner_count' is incremented as a function of n.
    Return a dict: {'count': <integer>, 'formula': '<string describing formula>'}

    The loop:
        inner_count = 0
        for i in range(n):
            for j in range(i+1, n):
                inner_count += 1

    Example: count_operations(4) -> {'count': 6, 'formula': 'n*(n-1)/2'}
    """
    # TODO: compute the count and provide the formula
    # Hint: verify with a loop, then derive the closed form
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# ─────────────────────── AUTO-GRADER ─────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════════════════

def _run_tests():
    score = 0
    total = 100
    results = []

    # ── Problem 1: Linear Search ─────────────────────────────────────────────
    p1 = 0
    try:
        assert linear_search([3, 1, 4, 1, 5], 4) == 2,         "basic find"
        assert linear_search([3, 1, 4, 1, 5], 9) == -1,        "not found"
        assert linear_search([], 1) == -1,                      "empty list"
        assert linear_search([7], 7) == 0,                      "single element found"
        assert linear_search([7], 8) == -1,                     "single element not found"
        assert linear_search([1, 2, 3, 2, 1], 2) == 1,         "first occurrence"
        p1 = 20
        results.append(("Problem 1 – Linear Search",    "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 1 – Linear Search",    f"FAIL: {e}", 0, 20))
    score += p1

    # ── Problem 2: Binary Search ──────────────────────────────────────────────
    p2 = 0
    try:
        arr = list(range(0, 100, 2))          # [0, 2, 4, ..., 98]
        assert binary_search(arr, 50) == 25,               "found at mid"
        assert binary_search(arr, 0)  == 0,                "found at start"
        assert binary_search(arr, 98) == 49,               "found at end"
        assert binary_search(arr, 3)  == -1,               "not found (odd)"
        assert binary_search([], 5)   == -1,               "empty list"
        assert binary_search([5], 5)  == 0,                "single element found"
        assert binary_search([5], 6)  == -1,               "single element not found"
        # Complexity check: should use at most ceil(log2(n))+1 comparisons
        p2 = 20
        results.append(("Problem 2 – Binary Search",    "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 2 – Binary Search",    f"FAIL: {e}", 0, 20))
    score += p2

    # ── Problem 3: Min/Max ───────────────────────────────────────────────────
    p3 = 0
    try:
        assert find_min_max([3, 1, 4, 1, 5, 9, 2, 6]) == (1, 9), "basic"
        assert find_min_max([42]) == (42, 42),                     "single element"
        assert find_min_max([5, 5]) == (5, 5),                     "two equal"
        assert find_min_max([-10, 0, 10]) == (-10, 10),            "negative"
        assert find_min_max(list(range(100, 0, -1))) == (1, 100),  "reverse"
        result = find_min_max([1, 2])
        assert isinstance(result, tuple) and len(result) == 2,     "returns tuple"
        p3 = 20
        results.append(("Problem 3 – Min/Max",          "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 3 – Min/Max",          f"FAIL: {e}", 0, 20))
    score += p3

    # ── Problem 4: Insertion Sort ─────────────────────────────────────────────
    p4 = 0
    try:
        assert insertion_sort([5,2,4,6,1,3]) == [1,2,3,4,5,6],    "basic"
        assert insertion_sort([]) == [],                            "empty"
        assert insertion_sort([1]) == [1],                         "single"
        assert insertion_sort([1,2,3]) == [1,2,3],                 "already sorted"
        assert insertion_sort([3,2,1]) == [1,2,3],                 "reverse"
        # Stability: equal elements keep relative order
        # We embed extra info via tuples
        data = [(1,'a'),(2,'b'),(1,'c'),(2,'d')]
        sorted_data = insertion_sort(data)
        assert sorted_data == [(1,'a'),(1,'c'),(2,'b'),(2,'d')],   "stable sort"
        # Input not modified
        orig = [3, 1, 2]
        _ = insertion_sort(orig)
        assert orig == [3, 1, 2],                                  "input not modified"
        p4 = 20
        results.append(("Problem 4 – Insertion Sort",   "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 4 – Insertion Sort",   f"FAIL: {e}", 0, 20))
    score += p4

    # ── Problem 5: Count Operations ──────────────────────────────────────────
    p5 = 0
    try:
        for n in [1, 2, 4, 5, 10, 20]:
            expected = n * (n - 1) // 2
            res = count_operations(n)
            assert isinstance(res, dict),                          "returns dict"
            assert 'count' in res,                                 "has 'count' key"
            assert 'formula' in res,                               "has 'formula' key"
            assert res['count'] == expected, f"count for n={n}: expected {expected}, got {res['count']}"
        assert 'n' in res['formula'].lower() or '2' in res['formula'], "formula mentions n"
        p5 = 20
        results.append(("Problem 5 – Count Operations", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 5 – Count Operations", f"FAIL: {e}", 0, 20))
    score += p5

    # ── Report ───────────────────────────────────────────────────────────────
    print("\n" + "═" * 62)
    print("  WEEK 1 AUTO-GRADER RESULTS")
    print("═" * 62)
    for name, status, pts, max_pts in results:
        mark = "✓" if "PASS" in status else "✗"
        print(f"  {mark} {name:<35} {pts:>3}/{max_pts}")
        if "FAIL" in status:
            print(f"      → {status[5:]}")
    print("─" * 62)
    print(f"  TOTAL SCORE: {score}/{total}  ({score}%)")
    if score == total:
        print("  🎉 Perfect score! Great work!")
    elif score >= 80:
        print("  👍 Good job! Review the failed tests.")
    elif score >= 50:
        print("  📚 Keep going! Re-read the lecture notes.")
    else:
        print("  💪 More practice needed. Try again after re-reading.")
    print("═" * 62 + "\n")
    return score


if __name__ == "__main__":
    _run_tests()
