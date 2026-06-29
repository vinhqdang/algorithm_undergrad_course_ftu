"""
Problem 04 - Memoized (Top-Down) Weighted Interval Scheduling
=============================================================

The same recurrence as Problem 2 can be solved TOP-DOWN with memoization
instead of filling a table bottom-up. Without memoization, the naive recursion

    M(j) = max( M(j-1), weight_{j-1} + M(p(j-1)+1) )

re-computes the same subproblems exponentially many times. Caching each M(j)
(e.g. with functools.lru_cache or a dict) makes each subproblem solved once,
giving O(n) total work.

Implement `memoized_wis_value(intervals)` using top-down memoized recursion.
The final test verifies it returns EXACTLY the bottom-up value (Problem 2) on
many random instances.

See practical_exercises.pdf, Problem 4.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem01 import compute_p  # noqa: F401

WeightedInterval = Tuple[float, float, float]


def memoized_wis_value(intervals: List[WeightedInterval]) -> float:
    """Return the optimal WIS value via top-down memoized recursion."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        from solution_problem02 import weighted_interval_scheduling_value
        from starter_code import generate_weighted_intervals

        assert memoized_wis_value([(0, 2, 3), (2, 4, 5)]) == 8.0
        assert memoized_wis_value([(0, 3, 3), (1, 4, 5)]) == 5.0
        assert memoized_wis_value([]) == 0.0

        for trial in range(100):
            inst = generate_weighted_intervals(12, seed=trial)
            assert abs(memoized_wis_value(inst)
                       - weighted_interval_scheduling_value(inst)) < 1e-9

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
