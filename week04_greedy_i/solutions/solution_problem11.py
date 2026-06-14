"""
Problem 11 - Earliest-Deadline-First Scheduling (Minimizing Lateness) (SOLUTION)
====================================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import schedule_lateness

Job = Tuple[float, float]


def earliest_deadline_first(jobs: List[Job]) -> Tuple[List[int], float]:
    """Return (order, max_lateness) for the earliest-deadline-first schedule."""
    order = sorted(range(len(jobs)), key=lambda i: jobs[i][0])
    _, max_lateness = schedule_lateness(jobs, order)
    return order, max_lateness


if __name__ == "__main__":
    jobs = [
        (2, 1),
        (4, 2),
        (6, 3),
        (8, 4),
        (9, 3),
        (15, 2),
    ]
    order, max_lateness = earliest_deadline_first(jobs)

    assert order == [0, 1, 2, 3, 4, 5]
    assert max_lateness == 4

    single = [(5, 10)]
    order2, lateness2 = earliest_deadline_first(single)
    assert order2 == [0]
    assert lateness2 == 5

    print("All tests passed!")
