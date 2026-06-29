"""
Problem 12 - Peak Finding in 1-D (O(log n)) (SOLUTION)
======================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import generate_array


def find_peak(arr: List[int]) -> int:
    """Return the index of a peak element in `arr` (O(log n))."""

    def _search(lo: int, hi: int) -> int:
        mid = (lo + hi) // 2
        if mid < hi and arr[mid + 1] > arr[mid]:
            return _search(mid + 1, hi)  # peak guaranteed to the right
        elif mid > lo and arr[mid - 1] > arr[mid]:
            return _search(lo, mid - 1)  # peak guaranteed to the left
        else:
            return mid  # neither neighbour is larger -> mid is a peak

    return _search(0, len(arr) - 1)


def _is_peak(arr: List[int], i: int) -> bool:
    n = len(arr)
    left_ok = (i == 0) or arr[i] >= arr[i - 1]
    right_ok = (i == n - 1) or arr[i] >= arr[i + 1]
    return left_ok and right_ok


if __name__ == "__main__":
    assert find_peak([1, 3, 20, 4, 1, 0]) == 2
    assert find_peak([1]) == 0
    assert find_peak([1, 2, 3, 4, 5]) == 4
    assert find_peak([5, 4, 3, 2, 1]) == 0

    for seed in range(50):
        arr = generate_array(40, seed=seed, lo=0, hi=100)
        idx = find_peak(arr)
        assert 0 <= idx < len(arr)
        assert _is_peak(arr, idx), (arr, idx)

    print("All tests passed!")
