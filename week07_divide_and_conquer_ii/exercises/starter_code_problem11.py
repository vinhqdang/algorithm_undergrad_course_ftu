"""
Problem 11 - Median of Two Sorted Arrays in O(log(m+n))
=======================================================

Given two sorted arrays ``a`` and ``b`` (at least one non-empty), return the
median of their combined elements in O(log(min(m, n))) time, using a binary
search for the correct partition of the shorter array.

Implement `median_two_sorted(a, b)`. Binary-search the number i of elements of
the shorter array placed on the "left" side; set j so that the left side holds
exactly (m+n+1)//2 elements; the partition is correct when
``a_left <= b_right and b_left <= a_right`` (using +/-infinity sentinels at the
ends). A merge-based reference `median_by_merge` is provided for verification.

See practical_exercises.pdf, Problem 11.
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def median_by_merge(a: List[int], b: List[int]) -> float:
    """Reference median by fully merging the two arrays (O(m+n))."""
    merged = sorted(a + b)
    k = len(merged)
    if k == 0:
        raise ValueError("at least one array must be non-empty")
    if k % 2 == 1:
        return float(merged[k // 2])
    return (merged[k // 2 - 1] + merged[k // 2]) / 2.0


def median_two_sorted(a: List[int], b: List[int]) -> float:
    """Median of two sorted arrays in O(log(min(m, n)))."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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
    except NotImplementedError:
        print("TODO: implement the functions above.")
