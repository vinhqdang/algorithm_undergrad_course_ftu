"""
Problem 03 - Randomized Quickselect
====================================

Implement `randomized_quickselect(arr, k, seed)` returning the k-th smallest
element (1-indexed) using random pivots (seeded), recursing into only the
relevant side.

See practical_exercises.pdf, Problem 3.
"""

import os
import random
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def randomized_quickselect(arr: List, k: int, seed: int):
    """Return the k-th smallest element (1-indexed) using random pivots."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        from starter_code import generate_array, generate_distinct_array

        for trial in range(60):
            arr = generate_array(35, seed=2000 + trial)
            srt = sorted(arr)
            for k in range(1, len(arr) + 1):
                assert randomized_quickselect(arr, k, seed=trial) == srt[k - 1], (trial, k)

        for trial in range(40):
            arr = generate_distinct_array(30, seed=3000 + trial)
            srt = sorted(arr)
            for k in (1, 5, 15, 30):
                assert randomized_quickselect(arr, k, seed=trial) == srt[k - 1]

        assert randomized_quickselect([42], 1, seed=0) == 42

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
