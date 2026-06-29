"""
Problem 03 - Weighted Interval Scheduling: Reconstruct the Optimal Set (SOLUTION)
=================================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution_problem01 import compute_p

WeightedInterval = Tuple[float, float, float]


def weighted_interval_scheduling_solution(
    intervals: List[WeightedInterval],
) -> Tuple[float, List[WeightedInterval]]:
    """Return (optimal_value, chosen_intervals) for Weighted Interval Scheduling.

    Fills the DP table M, then traces back: at interval j-1 (1-based j), we took
    interval j-1 iff weight + M[p(j-1)+1] >= M[j-1]. Chosen intervals are
    returned sorted by finish time.
    """
    ordered = sorted(intervals, key=lambda iv: iv[1])
    n = len(ordered)
    if n == 0:
        return 0.0, []
    p = compute_p(intervals)
    weights = [iv[2] for iv in ordered]

    M = [0.0] * (n + 1)
    for j in range(1, n + 1):
        take = weights[j - 1] + M[p[j - 1] + 1]
        skip = M[j - 1]
        M[j] = max(take, skip)

    # Traceback.
    chosen: List[WeightedInterval] = []
    j = n
    while j >= 1:
        take = weights[j - 1] + M[p[j - 1] + 1]
        skip = M[j - 1]
        if take >= skip:
            chosen.append(ordered[j - 1])
            j = p[j - 1] + 1  # jump to the last compatible interval (1-based)
        else:
            j = j - 1
    chosen.reverse()
    return M[n], chosen


if __name__ == "__main__":
    from solution_problem02 import weighted_interval_scheduling_value

    # Two compatible intervals: both chosen.
    val, sel = weighted_interval_scheduling_solution([(0, 2, 3), (2, 4, 5)])
    assert val == 8.0
    assert sorted(sel) == [(0, 2, 3), (2, 4, 5)]

    # Two overlapping: only the heavier chosen.
    val, sel = weighted_interval_scheduling_solution([(0, 3, 3), (1, 4, 5)])
    assert val == 5.0
    assert sel == [(1, 4, 5)]

    # Four light beat one heavy.
    ivs = [(0, 10, 8), (0, 2, 3), (2, 4, 3), (4, 6, 3), (6, 8, 3)]
    val, sel = weighted_interval_scheduling_solution(ivs)
    assert val == 12.0
    assert len(sel) == 4

    # The reconstructed set must be feasible and its weight must equal the value,
    # cross-checked against the value-only routine on random instances.
    import sys as _sys
    _sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from starter_code import generate_weighted_intervals, selection_is_feasible

    for trial in range(50):
        inst = generate_weighted_intervals(9, seed=trial)
        val, sel = weighted_interval_scheduling_solution(inst)
        assert selection_is_feasible(sel)
        assert abs(sum(w for _, _, w in sel) - val) < 1e-9
        assert abs(val - weighted_interval_scheduling_value(inst)) < 1e-9

    print("All tests passed!")
