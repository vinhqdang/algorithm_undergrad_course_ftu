"""
Problem 09 - Quickselect: k-th Smallest Element
================================================

Implement `quickselect(arr, k)`: return the k-th smallest element of `arr`
(0-indexed, so k == 0 is the minimum), using the partition-and-recurse
divide-and-conquer method. A deterministic pivot (e.g. the last or middle
element) is acceptable. Do NOT mutate the caller's list. Verify against
sorted(arr)[k].

See practical_exercises.pdf, Problem 9.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import generate_array


def quickselect(arr: List[int], k: int) -> int:
    """Return the k-th smallest element of `arr` (0-indexed)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        a = [7, 2, 1, 6, 8, 5, 3, 4]
        assert quickselect(a, 0) == 1
        assert quickselect(a, 3) == 4
        assert quickselect(a, 7) == 8
        assert a == [7, 2, 1, 6, 8, 5, 3, 4]  # not mutated

        assert quickselect([42], 0) == 42
        assert quickselect([5, 5, 5, 5], 2) == 5

        for seed in range(40):
            arr = generate_array(50, seed=seed, lo=0, hi=100)
            expected = sorted(arr)
            for k in (0, 1, 25, 49):
                assert quickselect(arr, k) == expected[k]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
