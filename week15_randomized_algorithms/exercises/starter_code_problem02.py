"""
Problem 02 - Randomized QuickSort
==================================

Implement `randomized_quicksort(arr, seed)` returning a sorted copy, choosing each
pivot uniformly at random (seeded). Also implement `quicksort_with_comparisons(
arr, seed)` returning (sorted_copy, number_of_element_comparisons).

See practical_exercises.pdf, Problem 2.
"""

import math
import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def randomized_quicksort(arr: List, seed: int) -> List:
    """Return a sorted copy of `arr` using randomized (seeded) pivots."""
    # TODO: implement this function.
    raise NotImplementedError


def quicksort_with_comparisons(arr: List, seed: int) -> Tuple[List, int]:
    """Return (sorted_copy, number_of_element_comparisons)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        from starter_code import generate_array

        for trial in range(100):
            arr = generate_array(40, seed=1000 + trial)
            assert randomized_quicksort(arr, seed=trial) == sorted(arr)

        assert randomized_quicksort([], seed=0) == []
        assert randomized_quicksort([5], seed=0) == [5]
        assert randomized_quicksort([3, 1, 2, 1], seed=0) == [1, 1, 2, 3]

        n = 200
        total = 0
        num_trials = 40
        for trial in range(num_trials):
            arr = generate_array(n, seed=5000 + trial)
            srt, comps = quicksort_with_comparisons(arr, seed=trial)
            assert srt == sorted(arr)
            total += comps
        avg = total / num_trials
        bound = 10 * n * math.log2(n)
        assert avg <= bound, (avg, bound)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
