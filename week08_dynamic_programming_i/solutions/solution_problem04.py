"""
Problem 04 - Memoized (Top-Down) Weighted Interval Scheduling (SOLUTION)
========================================================================
"""

import os
import sys
from functools import lru_cache
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution_problem01 import compute_p

WeightedInterval = Tuple[float, float, float]


def memoized_wis_value(intervals: List[WeightedInterval]) -> float:
    """Return the optimal weighted-interval-scheduling value via top-down
    memoized recursion.

    Define M(j) = optimum over the first j intervals (1-based), with
        M(0) = 0
        M(j) = max( M(j-1), weight_{j-1} + M(p(j-1)+1) ).
    Memoization makes each M(j) computed once, giving O(n) work.
    """
    ordered = sorted(intervals, key=lambda iv: iv[1])
    n = len(ordered)
    if n == 0:
        return 0.0
    p = compute_p(intervals)
    weights = [iv[2] for iv in ordered]

    @lru_cache(maxsize=None)
    def M(j: int) -> float:
        if j == 0:
            return 0.0
        take = weights[j - 1] + M(p[j - 1] + 1)
        skip = M(j - 1)
        return max(take, skip)

    return M(n)


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from solution_problem02 import weighted_interval_scheduling_value
    from starter_code import generate_weighted_intervals

    # Direct small checks.
    assert memoized_wis_value([(0, 2, 3), (2, 4, 5)]) == 8.0
    assert memoized_wis_value([(0, 3, 3), (1, 4, 5)]) == 5.0
    assert memoized_wis_value([]) == 0.0

    # Memoized top-down must equal bottom-up on many random instances.
    for trial in range(100):
        inst = generate_weighted_intervals(12, seed=trial)
        top_down = memoized_wis_value(inst)
        bottom_up = weighted_interval_scheduling_value(inst)
        assert abs(top_down - bottom_up) < 1e-9

    print("All tests passed!")
