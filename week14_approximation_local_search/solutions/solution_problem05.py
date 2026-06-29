"""
Problem 05 - Load Balancing: Greedy List Scheduling (SOLUTION)
==============================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_jobs  # noqa: E402


def greedy_list_scheduling(times: List[float], m: int) -> Tuple[List[float], float]:
    """Assign each job (in order) to a currently least-loaded machine.

    Returns (loads, makespan).
    """
    loads = [0.0] * m
    for t in times:
        k = min(range(m), key=lambda i: loads[i])
        loads[k] += t
    return loads, max(loads)


def _lower_bound(times: List[float], m: int) -> float:
    if not times:
        return 0.0
    return max(max(times), sum(times) / m)


def verify_greedy_makespan(num_trials: int, n: int, m: int, seed: int) -> bool:
    """Check greedy makespan <= 2 * lower_bound on random instances."""
    for trial in range(num_trials):
        times = generate_jobs(n, seed=seed + trial)
        _, makespan = greedy_list_scheduling(times, m)
        lb = _lower_bound(times, m)
        if makespan > 2 * lb + 1e-9:
            return False
    return True


if __name__ == "__main__":
    # Three equal jobs on three machines: makespan = one job.
    loads, mk = greedy_list_scheduling([3.0, 3.0, 3.0], 3)
    assert abs(mk - 3.0) < 1e-9

    # All work on too few machines.
    loads, mk = greedy_list_scheduling([1.0, 1.0, 1.0, 1.0], 2)
    assert abs(mk - 2.0) < 1e-9
    assert abs(sum(loads) - 4.0) < 1e-9

    # Makespan always at least the lower bound.
    times = [5.0, 4.0, 3.0, 2.0, 1.0]
    _, mk = greedy_list_scheduling(times, 2)
    assert mk >= _lower_bound(times, 2) - 1e-9

    # Random verification of the 2-approximation guarantee.
    assert verify_greedy_makespan(num_trials=200, n=20, m=3, seed=7) is True
    assert verify_greedy_makespan(num_trials=200, n=30, m=5, seed=42) is True

    print("All tests passed!")
