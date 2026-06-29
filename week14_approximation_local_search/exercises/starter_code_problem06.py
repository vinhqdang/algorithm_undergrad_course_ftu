"""
Problem 06 - Longest-Processing-Time (LPT) Scheduling
======================================================

Implement `lpt_scheduling(times, m)`: sort jobs in DECREASING order, then run
greedy list scheduling (Problem 5). Return (loads, makespan). Then implement
`verify_lpt_makespan(num_trials, n, m, seed)`: check that the LPT makespan is
<= (4/3) * max(max_j t_j, (1/m) sum_j t_j) on every random instance.

You may reuse `greedy_list_scheduling` from Problem 5 (re-implemented here).

See practical_exercises.pdf, Problem 6.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_jobs  # noqa: E402


def greedy_list_scheduling(times: List[float], m: int) -> Tuple[List[float], float]:
    """Greedy list scheduling (copied from Problem 5)."""
    loads = [0.0] * m
    for t in times:
        k = min(range(m), key=lambda i: loads[i])
        loads[k] += t
    return loads, max(loads)


def lpt_scheduling(times: List[float], m: int) -> Tuple[List[float], float]:
    """Sort jobs in decreasing order, then run greedy list scheduling."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_lpt_makespan(num_trials: int, n: int, m: int, seed: int) -> bool:
    """Return True iff LPT makespan <= (4/3) * lower_bound on every trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        _, mk = lpt_scheduling([3.0, 3.0, 3.0], 3)
        assert abs(mk - 3.0) < 1e-9

        times = [5.0, 4.0, 3.0, 2.0, 1.0]
        _, mk_lpt = lpt_scheduling(times, 2)
        lb = max(max(times), sum(times) / 2)
        assert mk_lpt >= lb - 1e-9

        _, mk = lpt_scheduling([3, 3, 2, 2, 2], 3)
        assert mk <= (4.0 / 3.0) * 4 + 1e-9

        assert verify_lpt_makespan(num_trials=200, n=20, m=3, seed=7) is True
        assert verify_lpt_makespan(num_trials=200, n=30, m=5, seed=42) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
