"""
Problem 09 - Search in a Rotated Sorted Array
================================================

An array `arr` of distinct integers, originally sorted in increasing order,
has been "rotated" at some unknown pivot, e.g.
    [4, 5, 6, 7, 0, 1, 2]   (originally [0,1,2,4,5,6,7], rotated by 4)

Implement `search_rotated(arr, target)` that returns the index of `target` in
`arr`, or -1 if not present, in O(log n) time.

Hint: at any point during binary search, at least one of the two halves
[lo..mid] or [mid..hi] is "normally sorted" (its first element <= its last
element). Determine which half is sorted, then check whether `target` could
lie in that half's range to decide which half to recurse/iterate into.

See practical_exercises.pdf, Problem 9.
"""

from typing import List


def search_rotated(arr: List[int], target: int) -> int:
    """Return the index of target in a rotated sorted array of distinct ints, or -1."""
    # TODO: implement this function (O(log n)).
    raise NotImplementedError


if __name__ == "__main__":
    try:
        arr = [4, 5, 6, 7, 0, 1, 2]
        for target, expected in [(0, 4), (4, 0), (2, 6), (7, 3), (3, -1), (5, 1)]:
            assert search_rotated(arr, target) == expected, (target, expected)

        # Not rotated at all.
        arr2 = [1, 2, 3, 4, 5]
        for target, expected in [(1, 0), (5, 4), (3, 2), (6, -1)]:
            assert search_rotated(arr2, target) == expected, (target, expected)

        # Single element.
        assert search_rotated([1], 1) == 0
        assert search_rotated([1], 2) == -1

        # Empty array.
        assert search_rotated([], 1) == -1

        # Rotated by 1.
        arr3 = [2, 1]
        assert search_rotated(arr3, 1) == 1
        assert search_rotated(arr3, 2) == 0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
