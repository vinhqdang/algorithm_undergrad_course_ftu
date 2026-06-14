"""
Problem 14 - Insertion Sort with Comparison Counter (SOLUTION)
=================================================================
"""

from typing import List, Tuple


def insertion_sort(arr: List[int]) -> Tuple[List[int], int]:
    """Return (sorted_copy, number_of_comparisons)."""
    a = list(arr)
    comparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comparisons


if __name__ == "__main__":
    n = 10
    sorted_input = list(range(n))
    reverse_input = list(range(n, 0, -1))

    sorted_result, sorted_cmps = insertion_sort(sorted_input)
    assert sorted_result == sorted(sorted_input)
    assert sorted_cmps == n - 1, sorted_cmps

    reverse_result, reverse_cmps = insertion_sort(reverse_input)
    assert reverse_result == sorted(reverse_input)
    assert reverse_cmps == n * (n - 1) // 2, reverse_cmps

    assert reverse_input == list(range(n, 0, -1))

    unsorted = [5, 2, 9, 1, 5, 6]
    result, _ = insertion_sort(unsorted)
    assert result == sorted(unsorted)

    print("All tests passed!")
