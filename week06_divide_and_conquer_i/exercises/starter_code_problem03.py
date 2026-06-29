"""
Problem 03 - Count Inversions in O(n log n)
============================================

Implement `count_inversions(arr)`: return the number of inversions (pairs of
indices i < j with arr[i] > arr[j]) in O(n log n) time, by modifying mergesort.
During each merge, when an element of the RIGHT half is emitted before the LEFT
half is exhausted, add the number of remaining left-half elements to the count.

Verify against `count_inversions_brute` (starter_code.py).

See practical_exercises.pdf, Problem 3.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import count_inversions_brute, generate_array


def count_inversions(arr: List[int]) -> int:
    """Return the number of inversions in `arr` in O(n log n)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert count_inversions([2, 4, 1, 3, 5]) == 3
        assert count_inversions([1, 2, 3, 4]) == 0
        assert count_inversions([4, 3, 2, 1]) == 6  # C(4,2) = 6
        assert count_inversions([]) == 0
        assert count_inversions([1]) == 0

        for seed in range(30):
            a = generate_array(40, seed=seed, lo=0, hi=20)
            assert count_inversions(a) == count_inversions_brute(a)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
