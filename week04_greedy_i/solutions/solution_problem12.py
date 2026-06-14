"""
Problem 12 - Brute-Force Optimal Schedule for Minimizing Lateness (SOLUTION)
================================================================================
"""

import os
import sys
from itertools import permutations
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import schedule_lateness

Job = Tuple[float, float]


def brute_force_min_lateness(jobs: List[Job]) -> float:
    """Return the minimum possible max-lateness over all orderings of `jobs`."""
    best = float("inf")
    for order in permutations(range(len(jobs))):
        _, max_lateness = schedule_lateness(jobs, list(order))
        best = min(best, max_lateness)
    return best


if __name__ == "__main__":
    jobs = [(2, 1), (4, 2), (6, 3), (8, 4), (9, 3), (15, 2)]
    assert brute_force_min_lateness(jobs) == 4

    single = [(5, 10)]
    assert brute_force_min_lateness(single) == 5

    two_jobs = [(1, 2), (10, 1)]
    assert brute_force_min_lateness(two_jobs) == 1

    print("All tests passed!")
