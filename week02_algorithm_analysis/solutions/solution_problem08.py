"""
Problem 08 - First and Last Occurrence (Binary Search Variant) (SOLUTION)
=============================================================================
"""

from typing import List


def find_first(arr: List[int], target: int) -> int:
    """Return the smallest index i with arr[i] == target, or -1."""
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1  # keep searching to the left for an earlier match
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def find_last(arr: List[int], target: int) -> int:
    """Return the largest index i with arr[i] == target, or -1."""
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1  # keep searching to the right for a later match
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def count_occurrences(arr: List[int], target: int) -> int:
    """Return the number of times target appears in arr."""
    first = find_first(arr, target)
    if first == -1:
        return 0
    last = find_last(arr, target)
    return last - first + 1


if __name__ == "__main__":
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
