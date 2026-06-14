"""
Problem 07 - Binary Search (Iterative and Recursive)
======================================================

Implement two versions of binary search over a sorted list `arr`:

  - `binary_search_iterative(arr, target)`: returns the index of `target` in
    `arr`, or -1 if not present. Use a `while` loop.

  - `binary_search_recursive(arr, target)`: same behaviour, implemented
    recursively (a helper with lo/hi bounds is fine).

Also implement `recursion_depth(n)`, returning the number of recursive calls
`binary_search_recursive` would make in the *worst case* on a sorted array of
length n, i.e. ceil(log2(n+1)) -- the number of halvings until the search
range becomes empty.

See practical_exercises.pdf, Problem 7.
"""

import math
from typing import List


def binary_search_iterative(arr: List[int], target: int) -> int:
    """Return the index of target in sorted arr, or -1 if not present."""
    # TODO: implement this function (iteratively).
    raise NotImplementedError


def binary_search_recursive(arr: List[int], target: int) -> int:
    """Return the index of target in sorted arr, or -1 if not present (recursive)."""
    # TODO: implement this function (recursively).
    raise NotImplementedError


def recursion_depth(n: int) -> int:
    """Return ceil(log2(n+1)), the worst-case number of recursive calls for size n."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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
    except NotImplementedError:
        print("TODO: implement the functions above.")
