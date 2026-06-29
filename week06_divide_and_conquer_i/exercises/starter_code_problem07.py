"""
Problem 07 - Maximum Subarray Sum (Divide and Conquer)
=======================================================

Implement `max_subarray(arr)`: return the maximum sum of any CONTIGUOUS
non-empty subarray of `arr` (which may contain negative numbers), using divide
and conquer. Split at the midpoint; the answer is the max of
  (i)  the best subarray in the left half,
  (ii) the best subarray in the right half,
  (iii) the best subarray CROSSING the midpoint (best suffix of the left half
        joined to best prefix of the right half).
Recurrence: T(n) = 2 T(n/2) + Theta(n) = Theta(n log n).

See practical_exercises.pdf, Problem 7.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import generate_array


def max_subarray(arr: List[int]) -> int:
    """Return the maximum contiguous subarray sum of (non-empty) `arr`."""
    # TODO: implement this function.
    raise NotImplementedError


def _brute_force_max_subarray(arr: List[int]) -> int:
    best = arr[0]
    for i in range(len(arr)):
        running = 0
        for j in range(i, len(arr)):
            running += arr[j]
            best = max(best, running)
    return best


if __name__ == "__main__":
    try:
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert max_subarray([1]) == 1
        assert max_subarray([-3]) == -3
        assert max_subarray([-1, -2, -3]) == -1
        assert max_subarray([5, 4, -1, 7, 8]) == 23

        for seed in range(40):
            a = generate_array(30, seed=seed, lo=-50, hi=50)
            assert max_subarray(a) == _brute_force_max_subarray(a)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
