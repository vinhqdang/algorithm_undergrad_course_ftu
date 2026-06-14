"""
Problem 05 - Verifying Optimality of Earliest-Finish-Time-First (SOLUTION)
=============================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem03 import earliest_finish_time_first
from solution_problem04 import brute_force_max_independent_set
from starter_code import generate_intervals


def verify_eft_optimal(num_trials: int = 30, n: int = 8, seed: int = 0) -> bool:
    """Return True iff EFT matches the brute-force optimum size on every trial."""
    for trial in range(num_trials):
        intervals = generate_intervals(n, seed=seed + trial)
        greedy = earliest_finish_time_first(intervals)
        optimal = brute_force_max_independent_set(intervals)
        if len(greedy) != len(optimal):
            return False
    return True


if __name__ == "__main__":
    assert verify_eft_optimal(num_trials=30, n=8, seed=0) is True
    assert verify_eft_optimal(num_trials=10, n=10, seed=100) is True

    print("All tests passed!")
