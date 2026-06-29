"""
Problem 07 - Maximum Subarray Sum (Divide and Conquer) (SOLUTION)
=================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import generate_array


def max_subarray(arr: List[int]) -> int:
    """Return the maximum contiguous subarray sum of (non-empty) `arr`."""

    def _solve(lo: int, hi: int) -> int:
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        left = _solve(lo, mid)
        right = _solve(mid + 1, hi)

        # Best suffix of left half ending at mid.
        best_suffix = arr[mid]
        running = 0
        for i in range(mid, lo - 1, -1):
            running += arr[i]
            best_suffix = max(best_suffix, running)

        # Best prefix of right half starting at mid + 1.
        best_prefix = arr[mid + 1]
        running = 0
        for i in range(mid + 1, hi + 1):
            running += arr[i]
            best_prefix = max(best_prefix, running)

        cross = best_suffix + best_prefix
        return max(left, right, cross)

    return _solve(0, len(arr) - 1)


def _brute_force_max_subarray(arr: List[int]) -> int:
    best = arr[0]
    for i in range(len(arr)):
        running = 0
        for j in range(i, len(arr)):
            running += arr[j]
            best = max(best, running)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-3]) == -3
    assert max_subarray([-1, -2, -3]) == -1
    assert max_subarray([5, 4, -1, 7, 8]) == 23

    for seed in range(40):
        a = generate_array(30, seed=seed, lo=-50, hi=50)
        assert max_subarray(a) == _brute_force_max_subarray(a)

    print("All tests passed!")
