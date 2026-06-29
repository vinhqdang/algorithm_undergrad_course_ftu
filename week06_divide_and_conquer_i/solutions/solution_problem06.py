"""
Problem 06 - Binary Search (Recursive) (SOLUTION)
==================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List

from starter_code import generate_sorted_array


def binary_search(arr: List[int], target: int) -> int:
    """Return an index of `target` in sorted `arr`, or -1 if absent."""

    def _search(lo: int, hi: int) -> int:
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return _search(lo, mid - 1)
        else:
            return _search(mid + 1, hi)

    return _search(0, len(arr) - 1)


if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([], 1) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1

    for seed in range(30):
        a = generate_sorted_array(60, seed=seed, lo=0, hi=200)
        for x in (a[0], a[-1], a[len(a) // 2], -1, 999):
            idx = binary_search(a, x)
            if idx == -1:
                assert x not in a
            else:
                assert a[idx] == x

    print("All tests passed!")
