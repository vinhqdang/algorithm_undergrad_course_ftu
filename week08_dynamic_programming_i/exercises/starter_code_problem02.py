"""
Problem 02 - Weighted Interval Scheduling: Optimal Value (Bottom-Up DP)
========================================================================

In Weighted Interval Scheduling each interval has a weight (value), and we want
the maximum total weight of a set of mutually compatible intervals (unlike
unweighted scheduling, maximizing the COUNT is no longer correct).

Sort the n intervals by finish time and let p(j) be as in Problem 1. Let M[j]
be the optimum over the first j intervals. The Bellman recurrence is:

    M[0] = 0
    M[j] = max( M[j-1],                          # do not take interval j
                weight_j + M[p(j) + 1] )         # take interval j

Implement `weighted_interval_scheduling_value(intervals)` by filling M
bottom-up (no recursion). Return the optimal total weight (a float).

You may import `compute_p` from `solution_problem01` (or re-derive p here).

See practical_exercises.pdf, Problem 2.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem01 import compute_p  # noqa: F401  (available helper)

WeightedInterval = Tuple[float, float, float]


def weighted_interval_scheduling_value(intervals: List[WeightedInterval]) -> float:
    """Return the maximum total weight of a compatible subset of `intervals`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert weighted_interval_scheduling_value([(0, 2, 3), (2, 4, 5)]) == 8.0
        assert weighted_interval_scheduling_value([(0, 3, 3), (1, 4, 5)]) == 5.0
        ivs = [(0, 10, 8), (0, 2, 3), (2, 4, 3), (4, 6, 3), (6, 8, 3)]
        assert weighted_interval_scheduling_value(ivs) == 12.0
        assert weighted_interval_scheduling_value([(0, 5, 10), (0, 2, 1), (1, 5, 1)]) == 10.0
        assert weighted_interval_scheduling_value([]) == 0.0
        assert weighted_interval_scheduling_value([(0, 1, 7)]) == 7.0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
