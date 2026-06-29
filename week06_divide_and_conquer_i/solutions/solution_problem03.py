"""
Problem 03 - Count Inversions in O(n log n) (SOLUTION)
=======================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List, Tuple

from starter_code import count_inversions_brute, generate_array


def _sort_and_count(arr: List[int]) -> Tuple[List[int], int]:
    if len(arr) <= 1:
        return list(arr), 0
    mid = len(arr) // 2
    left, inv_l = _sort_and_count(arr[:mid])
    right, inv_r = _sort_and_count(arr[mid:])

    merged: List[int] = []
    i = j = 0
    cross = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            cross += len(left) - i  # remaining left elements all > right[j]
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_l + inv_r + cross


def count_inversions(arr: List[int]) -> int:
    """Return the number of inversions in `arr` in O(n log n)."""
    _, inv = _sort_and_count(arr)
    return inv


if __name__ == "__main__":
    assert count_inversions([2, 4, 1, 3, 5]) == 3
    assert count_inversions([1, 2, 3, 4]) == 0
    assert count_inversions([4, 3, 2, 1]) == 6
    assert count_inversions([]) == 0
    assert count_inversions([1]) == 0

    for seed in range(30):
        a = generate_array(40, seed=seed, lo=0, hi=20)
        assert count_inversions(a) == count_inversions_brute(a)

    print("All tests passed!")
