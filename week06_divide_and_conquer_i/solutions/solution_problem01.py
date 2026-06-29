"""
Problem 01 - Merge Two Sorted Lists (SOLUTION)
================================================
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into one sorted list."""
    merged: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([], [1, 2, 3]) == [1, 2, 3]
    assert merge([1, 2, 3], []) == [1, 2, 3]
    assert merge([], []) == []
    assert merge([1, 1, 1], [1, 1]) == [1, 1, 1, 1, 1]
    assert merge([1, 4, 7], [2, 3, 8, 9]) == [1, 2, 3, 4, 7, 8, 9]

    print("All tests passed!")
