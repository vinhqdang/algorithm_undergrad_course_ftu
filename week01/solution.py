"""
Week 1 — SOLUTION Code (Instructor Copy)
=========================================
Do NOT distribute to students before the deadline.
"""

import math

# ── Problem 1: Linear Search ──────────────────────────────────────────────────

def linear_search(arr: list, target) -> int:
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1
# O(n) time, O(1) space

# ── Problem 2: Binary Search ──────────────────────────────────────────────────

def binary_search(arr: list, target) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# O(log n) time, O(1) space

# ── Problem 3: Min/Max with ~3n/2 comparisons ─────────────────────────────────

def find_min_max(arr: list) -> tuple:
    n = len(arr)
    if n == 0:
        raise ValueError("Empty array")
    if n == 1:
        return arr[0], arr[0]

    # Initialise from first pair
    if arr[0] < arr[1]:
        cur_min, cur_max = arr[0], arr[1]
    else:
        cur_min, cur_max = arr[1], arr[0]

    # Process remaining elements in pairs
    i = 2
    while i + 1 < n:
        if arr[i] < arr[i + 1]:
            small, large = arr[i], arr[i + 1]
        else:
            small, large = arr[i + 1], arr[i]
        if small < cur_min:
            cur_min = small
        if large > cur_max:
            cur_max = large
        i += 2

    # If odd number of elements, handle last element
    if i < n:
        if arr[i] < cur_min:
            cur_min = arr[i]
        if arr[i] > cur_max:
            cur_max = arr[i]

    return cur_min, cur_max
# O(n) time, O(1) space, ≤ ceil(3n/2) - 2 comparisons

# ── Problem 4: Insertion Sort (stable, returns new list) ──────────────────────

def insertion_sort(arr: list) -> list:
    result = list(arr)           # copy to avoid mutating input
    for j in range(1, len(result)):
        key = result[j]
        i = j - 1
        while i >= 0 and result[i] > key:   # strict > preserves stability
            result[i + 1] = result[i]
            i -= 1
        result[i + 1] = key
    return result
# O(n²) worst case, O(n) best case (already sorted), stable, in-place on copy

# ── Problem 5: Count Operations ───────────────────────────────────────────────

def count_operations(n: int) -> dict:
    """
    Inner loop runs from j = i+1 to n-1.
    Total iterations = sum_{i=0}^{n-1} (n - i - 1)
                     = (n-1) + (n-2) + ... + 1 + 0
                     = n*(n-1)/2
    """
    count = n * (n - 1) // 2
    return {'count': count, 'formula': 'n*(n-1)/2'}
# Θ(n²) growth

# ── Self-check ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Quick smoke test
    assert linear_search([3,1,4,1,5], 4) == 2
    assert binary_search(list(range(0,100,2)), 50) == 25
    assert find_min_max([3,1,4,1,5,9]) == (1, 9)
    assert insertion_sort([5,2,4,6,1,3]) == [1,2,3,4,5,6]
    assert count_operations(4) == {'count': 6, 'formula': 'n*(n-1)/2'}
    print("All solution checks passed.")
