"""
Problem 04 - Brute-Force Optimal Interval Scheduling
=======================================================

For small `n`, implement `brute_force_max_independent_set(intervals)` that
returns the LARGEST feasible (non-overlapping) subset of `intervals`, by
trying all 2^n subsets and keeping the largest one that is feasible
(`is_feasible` from starter_code.py). If there are ties, return any one of
the largest feasible subsets.

This is exponential and only intended for small n (say n <= 15); it exists
so we can empirically verify that the greedy earliest-finish-time-first
algorithm (Problem 3) is optimal (Problem 5).

See practical_exercises.pdf, Problem 4.
"""

import os
import sys
from itertools import combinations
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import is_feasible

Interval = Tuple[float, float]


def brute_force_max_independent_set(intervals: List[Interval]) -> List[Interval]:
    """Return a largest feasible subset of `intervals` (by brute force over all subsets)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        intervals = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
        best = brute_force_max_independent_set(intervals)
        assert is_feasible(best)
        # The optimal selection has size 3 for this classic instance.
        assert len(best) == 3

        # Empty input
        assert brute_force_max_independent_set([]) == []

        # All overlapping -> best is size 1
        all_overlap = [(0, 5), (1, 5), (2, 5)]
        best2 = brute_force_max_independent_set(all_overlap)
        assert len(best2) == 1
        assert is_feasible(best2)

        # All disjoint -> best is everything
        disjoint = [(0, 1), (1, 2), (2, 3)]
        best3 = brute_force_max_independent_set(disjoint)
        assert len(best3) == 3

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
