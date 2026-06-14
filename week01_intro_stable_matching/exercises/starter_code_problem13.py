"""
Problem 13 - Binary Search (Iterative and Recursive)
=======================================================

Implement two versions of binary search over a sorted list `arr`:

  - `binary_search_iterative(arr, target)`: returns the index of `target` in
    `arr`, or -1 if not present. Use a `while` loop.
  - `binary_search_recursive(arr, target)`: same behaviour, but implemented
    recursively (helper with `lo`/`hi` bounds is fine).

Also implement `recursion_depth(n)`, returning the number of recursive calls
`binary_search_recursive` would make in the WORST CASE on a sorted array of
length `n` (i.e. ceil(log2(n+1)), the number of halvings until the search
range is empty).

See practical_exercises.pdf, Problem 13.
"""

import math
from typing import List


def binary_search_iterative(arr: List[int], target: int) -> int:
    # TODO: implement.
    raise NotImplementedError


def binary_search_recursive(arr: List[int], target: int) -> int:
    # TODO: implement.
    raise NotImplementedError


def recursion_depth(n: int) -> int:
    """Worst-case number of recursive calls for binary search on n elements."""
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]

        for target in [0, 2, 50, 98, 100]:
            expected = arr.index(target) if target in arr else -1
            assert binary_search_iterative(arr, target) == expected
            assert binary_search_recursive(arr, target) == expected

        assert recursion_depth(1) == 1
        assert recursion_depth(7) == 3   # log2(8) = 3
        assert recursion_depth(8) == 4   # log2(9) ~ 3.17 -> ceil = 4
        assert recursion_depth(1023) == 10  # log2(1024) = 10

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
