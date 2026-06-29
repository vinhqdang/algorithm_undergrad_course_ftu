"""
Problem 03 - Weighted Interval Scheduling: Reconstruct the Optimal Set
======================================================================

Computing the optimal VALUE (Problem 2) is not enough -- we usually want the
actual set of intervals achieving it. Standard trick: after filling the DP
table M, TRACE BACK from M[n]. At step j (1-based), we know

    M[j] = max( M[j-1], weight_{j-1} + M[p(j-1)+1] ).

So interval j-1 is in the optimum iff the "take" branch was (at least) as good:

    weight_{j-1} + M[p(j-1)+1] >= M[j-1].

If we take it, jump to j = p(j-1)+1; otherwise move to j = j-1.

Implement `weighted_interval_scheduling_solution(intervals)` returning
`(optimal_value, chosen_intervals)` with `chosen_intervals` sorted by finish
time. The chosen set must be feasible and its weights must sum to the value.

See practical_exercises.pdf, Problem 3.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem01 import compute_p  # noqa: F401

WeightedInterval = Tuple[float, float, float]


def weighted_interval_scheduling_solution(
    intervals: List[WeightedInterval],
) -> Tuple[float, List[WeightedInterval]]:
    """Return (optimal_value, chosen_intervals) for Weighted Interval Scheduling."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        val, sel = weighted_interval_scheduling_solution([(0, 2, 3), (2, 4, 5)])
        assert val == 8.0
        assert sorted(sel) == [(0, 2, 3), (2, 4, 5)]

        val, sel = weighted_interval_scheduling_solution([(0, 3, 3), (1, 4, 5)])
        assert val == 5.0
        assert sel == [(1, 4, 5)]

        ivs = [(0, 10, 8), (0, 2, 3), (2, 4, 3), (4, 6, 3), (6, 8, 3)]
        val, sel = weighted_interval_scheduling_solution(ivs)
        assert val == 12.0
        assert len(sel) == 4

        from starter_code import generate_weighted_intervals, selection_is_feasible
        for trial in range(50):
            inst = generate_weighted_intervals(9, seed=trial)
            val, sel = weighted_interval_scheduling_solution(inst)
            assert selection_is_feasible(sel)
            assert abs(sum(w for _, _, w in sel) - val) < 1e-9

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
