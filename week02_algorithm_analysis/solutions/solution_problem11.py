"""
Problem 11 - Median via Sorting vs. Quickselect (SOLUTION)
=============================================================
"""

import math
from typing import List


def median_via_sort(arr: List[int]) -> int:
    """Return sorted(arr)[(len(arr)-1)//2]."""
    return sorted(arr)[(len(arr) - 1) // 2]


def quickselect(arr: List[int], k: int) -> int:
    """Return the k-th smallest element (0-indexed) of arr via Quickselect."""
    if len(arr) == 1:
        return arr[0]

    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    if k < len(less):
        return quickselect(less, k)
    elif k < len(less) + len(equal):
        return pivot
    else:
        return quickselect(greater, k - len(less) - len(equal))


def median_via_quickselect(arr: List[int]) -> int:
    """Return the median of arr using quickselect."""
    return quickselect(arr, (len(arr) - 1) // 2)


def count_comparisons_sort(n: int) -> int:
    """Return ceil(n * log2(n)) for n > 1, else 0 -- a rough comparison-sort estimate."""
    if n <= 1:
        return 0
    return math.ceil(n * math.log2(n))


if __name__ == "__main__":
    arr = [9, 3, 7, 1, 8, 2, 5]
    assert median_via_sort(arr) == 5
    assert median_via_quickselect(arr) == 5

    arr2 = [4, 2, 1, 3]
    assert median_via_sort(arr2) == 2
    assert median_via_quickselect(arr2) == 2

    for k in range(len(arr)):
        assert quickselect(arr, k) == sorted(arr)[k]

    assert quickselect([42], 0) == 42

    assert count_comparisons_sort(1) == 0
    assert count_comparisons_sort(8) == math.ceil(8 * math.log2(8))

    print("All tests passed!")
