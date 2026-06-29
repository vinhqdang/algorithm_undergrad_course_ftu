"""
Problem 10 - Majority Element (Divide and Conquer) (SOLUTION)
=============================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import Counter as CollCounter
from typing import List, Optional

from starter_code import generate_array


def majority_element(arr: List[int]) -> Optional[int]:
    """Return the strict majority element of `arr`, or None if none exists."""

    def _count(lo: int, hi: int, value: int) -> int:
        return sum(1 for i in range(lo, hi + 1) if arr[i] == value)

    def _majority(lo: int, hi: int) -> Optional[int]:
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        left = _majority(lo, mid)
        right = _majority(mid + 1, hi)
        length = hi - lo + 1
        if left is not None and _count(lo, hi, left) > length // 2:
            return left
        if right is not None and _count(lo, hi, right) > length // 2:
            return right
        return None

    if not arr:
        return None
    return _majority(0, len(arr) - 1)


def _brute_force_majority(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    value, count = CollCounter(arr).most_common(1)[0]
    return value if count > len(arr) // 2 else None


if __name__ == "__main__":
    assert majority_element([3, 3, 4, 2, 3, 3, 3]) == 3
    assert majority_element([1, 2, 3, 4]) is None
    assert majority_element([7]) == 7
    assert majority_element([]) is None
    assert majority_element([2, 2, 2, 2]) == 2
    assert majority_element([1, 1, 2, 2]) is None

    for seed in range(50):
        arr = generate_array(31, seed=seed, lo=0, hi=3)
        assert majority_element(arr) == _brute_force_majority(arr)

    print("All tests passed!")
