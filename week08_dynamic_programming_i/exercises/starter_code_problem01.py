"""
Problem 01 - Compute p(j) for Weighted Interval Scheduling
============================================================

In Weighted Interval Scheduling we first sort the n intervals by finish time,
so that f_0 <= f_1 <= ... <= f_{n-1}. For each interval j we need

    p(j) = the index of the latest interval i < j that is COMPATIBLE with j
           (i.e. finishes at or before j starts), or -1 if no such interval.

Implement `compute_p(intervals)`: sort `intervals` (each a tuple
(start, finish, weight)) by finish time, then for each j use BINARY SEARCH
(see the `bisect` module) over the finish times to find p(j) in O(log n).
Return the list p indexed by position in the finish-sorted order.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

from typing import List, Tuple

WeightedInterval = Tuple[float, float, float]


def compute_p(intervals: List[WeightedInterval]) -> List[int]:
    """Return the p-array (indexed by finish-sorted position) via binary search."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        ivs = [(0, 3, 1), (1, 4, 1), (3, 5, 1), (5, 7, 1)]
        assert compute_p(ivs) == [-1, -1, 0, 2]

        chain = [(0, 1, 5), (1, 2, 5), (2, 3, 5), (3, 4, 5)]
        assert compute_p(chain) == [-1, 0, 1, 2]

        overlap = [(0, 10, 1), (0, 11, 1), (0, 12, 1)]
        assert compute_p(overlap) == [-1, -1, -1]

        assert compute_p([(0, 5, 3)]) == [-1]
        assert compute_p([]) == []

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
