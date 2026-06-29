"""
Problem 11 - Median of Two Sorted Arrays in O(log(m+n)) (SOLUTION)
=================================================================
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def median_two_sorted(a: List[int], b: List[int]) -> float:
    """Median of two sorted arrays in O(log(min(m, n))).

    Binary-searches a partition of the shorter array so that everything on the
    left of the combined partition is <= everything on the right.
    """
    # Ensure `a` is the shorter array.
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    if m + n == 0:
        raise ValueError("at least one array must be non-empty")

    total_left = (m + n + 1) // 2
    lo, hi = 0, m
    inf = float("inf")
    while lo <= hi:
        i = (lo + hi) // 2          # elements of `a` on the left
        j = total_left - i          # elements of `b` on the left

        a_left = a[i - 1] if i > 0 else -inf
        a_right = a[i] if i < m else inf
        b_left = b[j - 1] if j > 0 else -inf
        b_right = b[j] if j < n else inf

        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2 == 1:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
        elif a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    raise RuntimeError("inputs were not sorted")


def median_by_merge(a: List[int], b: List[int]) -> float:
    """Reference median by fully merging the two arrays (O(m+n))."""
    merged = sorted(a + b)
    k = len(merged)
    if k == 0:
        raise ValueError("at least one array must be non-empty")
    if k % 2 == 1:
        return float(merged[k // 2])
    return (merged[k // 2 - 1] + merged[k // 2]) / 2.0


if __name__ == "__main__":
    assert median_two_sorted([1, 3], [2]) == 2.0
    assert median_two_sorted([1, 2], [3, 4]) == 2.5
    assert median_two_sorted([], [1]) == 1.0
    assert median_two_sorted([5], []) == 5.0

    rng = random.Random(2718)
    for _ in range(2000):
        m = rng.randint(0, 8)
        n = rng.randint(0, 8)
        if m + n == 0:
            continue
        a = sorted(rng.randint(-20, 20) for _ in range(m))
        b = sorted(rng.randint(-20, 20) for _ in range(n))
        assert median_two_sorted(a, b) == median_by_merge(a, b), (a, b)

    print("All tests passed!")
