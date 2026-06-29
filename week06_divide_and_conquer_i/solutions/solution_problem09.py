"""
Problem 09 - Quickselect: k-th Smallest Element (SOLUTION)
==========================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import generate_array


def quickselect(arr: List[int], k: int) -> int:
    """Return the k-th smallest element of `arr` (0-indexed)."""
    if not 0 <= k < len(arr):
        raise IndexError("k out of range")

    def _select(items: List[int], rank: int) -> int:
        # Deterministic pivot: the middle element.
        pivot = items[len(items) // 2]
        less = [x for x in items if x < pivot]
        equal = [x for x in items if x == pivot]
        greater = [x for x in items if x > pivot]
        if rank < len(less):
            return _select(less, rank)
        elif rank < len(less) + len(equal):
            return pivot
        else:
            return _select(greater, rank - len(less) - len(equal))

    return _select(list(arr), k)


if __name__ == "__main__":
    a = [7, 2, 1, 6, 8, 5, 3, 4]
    assert quickselect(a, 0) == 1
    assert quickselect(a, 3) == 4
    assert quickselect(a, 7) == 8
    assert a == [7, 2, 1, 6, 8, 5, 3, 4]

    assert quickselect([42], 0) == 42
    assert quickselect([5, 5, 5, 5], 2) == 5

    for seed in range(40):
        arr = generate_array(50, seed=seed, lo=0, hi=100)
        expected = sorted(arr)
        for k in (0, 1, 25, 49):
            assert quickselect(arr, k) == expected[k]

    print("All tests passed!")
