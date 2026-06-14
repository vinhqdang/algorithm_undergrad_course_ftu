"""
Problem 10 - Stress-Testing Interval Partitioning on Random Instances (SOLUTION)
====================================================================================
"""

import os
import sys
from typing import Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem07 import interval_partitioning
from starter_code import generate_intervals

Interval = Tuple[float, float]


def random_partitioning_is_valid(n: int, seed: int) -> bool:
    """Return True iff a random instance's partitioning has no same-resource overlaps and contiguous ids."""
    intervals = generate_intervals(n, seed=seed)
    assignment = interval_partitioning(intervals)

    used_ids = set(assignment.values())
    if used_ids != set(range(len(used_ids))):
        return False

    for resource_id in used_ids:
        group = [iv for iv, res in assignment.items() if res == resource_id]
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                s1, f1 = group[i]
                s2, f2 = group[j]
                if s1 < f2 and s2 < f1:
                    return False
    return True


def stress_test(num_trials: int = 50, n: int = 15, seed: int = 0) -> bool:
    """Return True iff random_partitioning_is_valid holds for all of num_trials random instances."""
    for trial in range(num_trials):
        if not random_partitioning_is_valid(n, seed=seed + trial):
            return False
    return True


if __name__ == "__main__":
    assert random_partitioning_is_valid(10, seed=1) is True
    assert stress_test(num_trials=50, n=15, seed=0) is True
    assert stress_test(num_trials=20, n=30, seed=200) is True

    print("All tests passed!")
