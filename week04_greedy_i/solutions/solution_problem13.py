"""
Problem 13 - Verifying Optimality of Earliest-Deadline-First (SOLUTION)
===========================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem11 import earliest_deadline_first
from solution_problem12 import brute_force_min_lateness
from starter_code import generate_jobs


def verify_edf_optimal(num_trials: int = 30, n: int = 6, seed: int = 0) -> bool:
    """Return True iff EDF's max lateness equals the brute-force optimum, for every trial."""
    for trial in range(num_trials):
        jobs = generate_jobs(n, seed=seed + trial)
        _, edf_lateness = earliest_deadline_first(jobs)
        optimal_lateness = brute_force_min_lateness(jobs)
        if abs(edf_lateness - optimal_lateness) >= 1e-9:
            return False
    return True


if __name__ == "__main__":
    assert verify_edf_optimal(num_trials=30, n=6, seed=0) is True
    assert verify_edf_optimal(num_trials=10, n=7, seed=100) is True

    print("All tests passed!")
