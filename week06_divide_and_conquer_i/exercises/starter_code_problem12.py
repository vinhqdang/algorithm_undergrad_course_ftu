"""
Problem 12 - Peak Finding in 1-D (O(log n))
============================================

Implement `find_peak(arr)`: return the INDEX of any peak element -- an index i
such that arr[i] >= both its neighbours (out-of-bounds neighbours count as
-infinity) -- in O(log n) via divide and conquer. Look at the middle element;
if its RIGHT neighbour is larger, a peak must lie to the right (recurse right);
else if its LEFT neighbour is larger, recurse left; otherwise the middle is a
peak. Assume `arr` is non-empty.

See practical_exercises.pdf, Problem 12.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import generate_array


def find_peak(arr: List[int]) -> int:
    """Return the index of a peak element in `arr` (O(log n))."""
    # TODO: implement this function.
    raise NotImplementedError


def _is_peak(arr: List[int], i: int) -> bool:
    n = len(arr)
    left_ok = (i == 0) or arr[i] >= arr[i - 1]
    right_ok = (i == n - 1) or arr[i] >= arr[i + 1]
    return left_ok and right_ok


if __name__ == "__main__":
    try:
        assert find_peak([1, 3, 20, 4, 1, 0]) == 2
        assert find_peak([1]) == 0
        # Strictly increasing: last index is the peak.
        assert find_peak([1, 2, 3, 4, 5]) == 4
        # Strictly decreasing: first index is the peak.
        assert find_peak([5, 4, 3, 2, 1]) == 0

        for seed in range(50):
            arr = generate_array(40, seed=seed, lo=0, hi=100)
            idx = find_peak(arr)
            assert 0 <= idx < len(arr)
            assert _is_peak(arr, idx), (arr, idx)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
