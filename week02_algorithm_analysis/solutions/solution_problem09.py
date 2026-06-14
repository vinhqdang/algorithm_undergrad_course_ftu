"""
Problem 09 - Search in a Rotated Sorted Array (SOLUTION)
============================================================
"""

from typing import List


def search_rotated(arr: List[int], target: int) -> int:
    """Return the index of target in a rotated sorted array of distinct ints, or -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid

        if arr[lo] <= arr[mid]:
            # Left half [lo..mid] is normally sorted.
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # Right half [mid..hi] is normally sorted.
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    for target, expected in [(0, 4), (4, 0), (2, 6), (7, 3), (3, -1), (5, 1)]:
        assert search_rotated(arr, target) == expected, (target, expected)

    arr2 = [1, 2, 3, 4, 5]
    for target, expected in [(1, 0), (5, 4), (3, 2), (6, -1)]:
        assert search_rotated(arr2, target) == expected, (target, expected)

    assert search_rotated([1], 1) == 0
    assert search_rotated([1], 2) == -1

    assert search_rotated([], 1) == -1

    arr3 = [2, 1]
    assert search_rotated(arr3, 1) == 1
    assert search_rotated(arr3, 2) == 0

    print("All tests passed!")
