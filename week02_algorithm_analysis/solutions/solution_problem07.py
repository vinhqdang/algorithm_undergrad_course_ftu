"""
Problem 07 - Binary Search (Iterative and Recursive) (SOLUTION)
==================================================================
"""

import math
from typing import List


def binary_search_iterative(arr: List[int], target: int) -> int:
    """Return the index of target in sorted arr, or -1 if not present."""
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
    """Return the index of target in sorted arr, or -1 if not present (recursive)."""
    def helper(lo: int, hi: int) -> int:
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
    """Return ceil(log2(n+1)), the worst-case number of recursive calls for size n."""
    if n <= 0:
        return 0
    return math.ceil(math.log2(n + 1))


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    for target, expected in [(1, 0), (19, 9), (7, 3), (4, -1), (20, -1), (0, -1)]:
        assert binary_search_iterative(arr, target) == expected, (target, expected)
        assert binary_search_recursive(arr, target) == expected, (target, expected)

    assert binary_search_iterative([], 5) == -1
    assert binary_search_recursive([], 5) == -1

    assert recursion_depth(1) == 1
    assert recursion_depth(3) == 2
    assert recursion_depth(7) == 3
    assert recursion_depth(15) == 4
    assert recursion_depth(1023) == 10

    print("All tests passed!")
