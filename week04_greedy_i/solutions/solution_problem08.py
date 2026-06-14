"""
Problem 08 - Verifying Interval Partitioning Uses the Minimum Number of Resources (SOLUTION)
================================================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem07 import interval_partitioning
from starter_code import generate_intervals, interval_depth


def verify_partitioning_optimal(num_trials: int = 30, n: int = 10, seed: int = 0) -> bool:
    """Return True iff #resources used by interval_partitioning equals interval_depth, for every trial."""
    for trial in range(num_trials):
        intervals = generate_intervals(n, seed=seed + trial)
        assignment = interval_partitioning(intervals)
        num_resources = len(set(assignment.values()))
        if num_resources != interval_depth(intervals):
            return False
    return True


if __name__ == "__main__":
    assert verify_partitioning_optimal(num_trials=30, n=10, seed=0) is True
    assert verify_partitioning_optimal(num_trials=10, n=20, seed=100) is True

    print("All tests passed!")
