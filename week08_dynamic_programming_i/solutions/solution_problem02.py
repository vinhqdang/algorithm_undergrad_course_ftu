"""
Problem 02 - Weighted Interval Scheduling: Optimal Value (Bottom-Up DP) (SOLUTION)
==================================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution_problem01 import compute_p

WeightedInterval = Tuple[float, float, float]


def weighted_interval_scheduling_value(intervals: List[WeightedInterval]) -> float:
    """Return the maximum total weight of a compatible subset of `intervals`.

    Bottom-up DP over intervals sorted by finish time:
        M[0] = 0
        M[j] = max( M[j-1],                              # skip interval j-1
                    weight_j + M[p(j-1) + 1] )           # take interval j-1
    (using 1-based M with M[j] = best over first j intervals).
    """
    ordered = sorted(intervals, key=lambda iv: iv[1])
    n = len(ordered)
    if n == 0:
        return 0.0
    p = compute_p(intervals)  # p indexed by finish-sorted position
    weights = [iv[2] for iv in ordered]

    # M[j] = optimum considering the first j intervals (0-based intervals 0..j-1).
    M = [0.0] * (n + 1)
    for j in range(1, n + 1):
        take = weights[j - 1] + M[p[j - 1] + 1]
        skip = M[j - 1]
        M[j] = max(take, skip)
    return M[n]


if __name__ == "__main__":
    # Two compatible intervals -> sum of weights.
    assert weighted_interval_scheduling_value([(0, 2, 3), (2, 4, 5)]) == 8.0

    # Two overlapping intervals -> pick the heavier one.
    assert weighted_interval_scheduling_value([(0, 3, 3), (1, 4, 5)]) == 5.0

    # Classic instance: a long heavy interval vs several light ones.
    ivs = [(0, 10, 8), (0, 2, 3), (2, 4, 3), (4, 6, 3), (6, 8, 3)]
    # Best is the four light ones (3*4 = 12) > the single heavy (8).
    assert weighted_interval_scheduling_value(ivs) == 12.0

    # A single heavy interval beats two light overlapping ones.
    assert weighted_interval_scheduling_value([(0, 5, 10), (0, 2, 1), (1, 5, 1)]) == 10.0

    assert weighted_interval_scheduling_value([]) == 0.0
    assert weighted_interval_scheduling_value([(0, 1, 7)]) == 7.0

    print("All tests passed!")
