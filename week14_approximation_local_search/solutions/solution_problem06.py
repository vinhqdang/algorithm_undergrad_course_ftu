"""
Problem 06 - Longest-Processing-Time (LPT) Scheduling (SOLUTION)
================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_jobs  # noqa: E402
from solution_problem05 import greedy_list_scheduling  # noqa: E402


def lpt_scheduling(times: List[float], m: int) -> Tuple[List[float], float]:
    """Sort jobs in decreasing order, then run greedy list scheduling."""
    sorted_times = sorted(times, reverse=True)
    return greedy_list_scheduling(sorted_times, m)


def _lower_bound(times: List[float], m: int) -> float:
    if not times:
        return 0.0
    return max(max(times), sum(times) / m)


def verify_lpt_makespan(num_trials: int, n: int, m: int, seed: int) -> bool:
    """Check LPT makespan <= (4/3) * lower_bound on random instances."""
    for trial in range(num_trials):
        times = generate_jobs(n, seed=seed + trial)
        _, makespan = lpt_scheduling(times, m)
        lb = _lower_bound(times, m)
        if makespan > (4.0 / 3.0) * lb + 1e-9:
            return False
    return True


if __name__ == "__main__":
    # LPT on three equal jobs / three machines.
    _, mk = lpt_scheduling([3.0, 3.0, 3.0], 3)
    assert abs(mk - 3.0) < 1e-9

    # LPT is at least as good as the lower bound, and usually beats plain greedy.
    times = [5.0, 4.0, 3.0, 2.0, 1.0]
    _, mk_lpt = lpt_scheduling(times, 2)
    assert mk_lpt >= _lower_bound(times, 2) - 1e-9

    # Classic instance: [3,3,2,2,2] on 3 machines. LB = max(3, 12/3) = 4; LPT must
    # stay within (4/3)*4 = 16/3 of it.
    _, mk = lpt_scheduling([3, 3, 2, 2, 2], 3)
    assert mk <= (4.0 / 3.0) * 4 + 1e-9

    # Random verification of the 4/3 guarantee.
    assert verify_lpt_makespan(num_trials=200, n=20, m=3, seed=7) is True
    assert verify_lpt_makespan(num_trials=200, n=30, m=5, seed=42) is True

    print("All tests passed!")
