"""
Problem 05 - Load Balancing: Greedy List Scheduling
====================================================

Implement `greedy_list_scheduling(times, m)`: assign each job (in the given
order) to a machine of currently MINIMUM load. Return (loads, makespan). Then
implement `verify_greedy_makespan(num_trials, n, m, seed)`: check that the
makespan is <= 2 * max(max_j t_j, (1/m) sum_j t_j) on every random instance.

See practical_exercises.pdf, Problem 5.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_jobs  # noqa: E402


def greedy_list_scheduling(times: List[float], m: int) -> Tuple[List[float], float]:
    """Assign each job (in order) to a least-loaded machine. Return (loads, makespan)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_greedy_makespan(num_trials: int, n: int, m: int, seed: int) -> bool:
    """Return True iff greedy makespan <= 2 * lower_bound on every trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        loads, mk = greedy_list_scheduling([3.0, 3.0, 3.0], 3)
        assert abs(mk - 3.0) < 1e-9

        loads, mk = greedy_list_scheduling([1.0, 1.0, 1.0, 1.0], 2)
        assert abs(mk - 2.0) < 1e-9
        assert abs(sum(loads) - 4.0) < 1e-9

        times = [5.0, 4.0, 3.0, 2.0, 1.0]
        _, mk = greedy_list_scheduling(times, 2)
        lb = max(max(times), sum(times) / 2)
        assert mk >= lb - 1e-9

        assert verify_greedy_makespan(num_trials=200, n=20, m=3, seed=7) is True
        assert verify_greedy_makespan(num_trials=200, n=30, m=5, seed=42) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
