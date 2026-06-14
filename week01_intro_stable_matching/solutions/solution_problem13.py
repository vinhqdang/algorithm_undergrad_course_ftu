"""
Problem 13 - Binary Search (Iterative and Recursive) (SOLUTION)
==================================================================
"""

import math
from typing import List


def binary_search_iterative(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(arr: List[int], target: int) -> int:
    def helper(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, hi)
        else:
            return helper(lo, mid - 1)

    return helper(0, len(arr) - 1)


def recursion_depth(n: int) -> int:
    """Worst-case number of recursive calls for binary search on n elements."""
    if n <= 0:
        return 0
    return math.ceil(math.log2(n + 1))


if __name__ == "__main__":
    arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]

    for target in [0, 2, 50, 98, 100]:
        expected = arr.index(target) if target in arr else -1
        assert binary_search_iterative(arr, target) == expected
        assert binary_search_recursive(arr, target) == expected

    assert recursion_depth(1) == 1
    assert recursion_depth(7) == 3
    assert recursion_depth(8) == 4
    assert recursion_depth(1023) == 10

    print("All tests passed!")
