"""
Problem 01 - Merge Two Sorted Lists
====================================

Implement `merge(left, right)`: given two lists, each sorted in non-decreasing
order, return a single NEW sorted list containing exactly the elements of both
(the multiset union). Use the two-pointer technique -- repeatedly compare the
front elements and append the smaller -- then append any remaining tail. Do NOT
call sorted() on the concatenation.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into one sorted list."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert merge([], [1, 2, 3]) == [1, 2, 3]
        assert merge([1, 2, 3], []) == [1, 2, 3]
        assert merge([], []) == []
        assert merge([1, 1, 1], [1, 1]) == [1, 1, 1, 1, 1]
        assert merge([1, 4, 7], [2, 3, 8, 9]) == [1, 2, 3, 4, 7, 8, 9]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
