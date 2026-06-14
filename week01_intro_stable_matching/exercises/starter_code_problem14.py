"""
Problem 14 - Insertion Sort with Comparison Counter
=====================================================

Implement `insertion_sort(arr)` that returns a NEW sorted list (do not mutate
the input) using the standard insertion sort algorithm, together with the
total number of element COMPARISONS performed, as a tuple `(sorted_list, comparisons)`.

Verify empirically that:
  - On an already-sorted list of length n, insertion sort makes exactly n-1
    comparisons (best case, O(n)).
  - On a reverse-sorted list of length n, it makes exactly n(n-1)/2
    comparisons (worst case, O(n^2)).

See practical_exercises.pdf, Problem 14.
"""

from typing import List, Tuple


def insertion_sort(arr: List[int]) -> Tuple[List[int], int]:
    """Return (sorted_copy, number_of_comparisons)."""
    # TODO: implement. Do not mutate `arr`.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        n = 10
        sorted_input = list(range(n))
        reverse_input = list(range(n, 0, -1))

        sorted_result, sorted_cmps = insertion_sort(sorted_input)
        assert sorted_result == sorted(sorted_input)
        assert sorted_cmps == n - 1, sorted_cmps

        reverse_result, reverse_cmps = insertion_sort(reverse_input)
        assert reverse_result == sorted(reverse_input)
        assert reverse_cmps == n * (n - 1) // 2, reverse_cmps

        # Original input must not be mutated.
        assert reverse_input == list(range(n, 0, -1))

        # Correctness on a generic unsorted list.
        unsorted = [5, 2, 9, 1, 5, 6]
        result, _ = insertion_sort(unsorted)
        assert result == sorted(unsorted)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
