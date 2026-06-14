"""
Problem 08 - First and Last Occurrence (Binary Search Variant)
=================================================================

Given a sorted array `arr` that may contain duplicate values, implement:

  - `find_first(arr, target)`: returns the smallest index i such that
    arr[i] == target, or -1 if target is not present.

  - `find_last(arr, target)`: returns the largest index i such that
    arr[i] == target, or -1 if target is not present.

  - `count_occurrences(arr, target)`: returns the number of times target
    appears in arr, computed as `find_last(arr, target) - find_first(arr,
    target) + 1` if target is present, else 0.

Each of `find_first` and `find_last` must run in O(log n) time: do a binary
search that, upon finding `target`, continues searching the left half (for
`find_first`) or right half (for `find_last`) instead of returning
immediately, to find the boundary.

See practical_exercises.pdf, Problem 8.
"""

from typing import List


def find_first(arr: List[int], target: int) -> int:
    """Return the smallest index i with arr[i] == target, or -1."""
    # TODO: implement this function (O(log n)).
    raise NotImplementedError


def find_last(arr: List[int], target: int) -> int:
    """Return the largest index i with arr[i] == target, or -1."""
    # TODO: implement this function (O(log n)).
    raise NotImplementedError


def count_occurrences(arr: List[int], target: int) -> int:
    """Return the number of times target appears in arr."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]

        assert find_first(arr, 2) == 1
        assert find_last(arr, 2) == 3
        assert count_occurrences(arr, 2) == 3

        assert find_first(arr, 5) == 7
        assert find_last(arr, 5) == 10
        assert count_occurrences(arr, 5) == 4

        assert find_first(arr, 1) == 0
        assert find_last(arr, 1) == 0
        assert count_occurrences(arr, 1) == 1

        assert find_first(arr, 7) == -1
        assert find_last(arr, 7) == -1
        assert count_occurrences(arr, 7) == 0

        assert find_first([], 1) == -1
        assert count_occurrences([], 1) == 0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
