"""
Problem 14 - Counter-Example: Shortest-Job-First Is Not Optimal for Lateness (SOLUTION)
===========================================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem11 import earliest_deadline_first
from starter_code import schedule_lateness

Job = Tuple[float, float]


def shortest_job_first(jobs: List[Job]) -> Tuple[List[int], float]:
    """Return (order, max_lateness) for the shortest-job-first schedule."""
    order = sorted(range(len(jobs)), key=lambda i: jobs[i][1])
    _, max_lateness = schedule_lateness(jobs, order)
    return order, max_lateness


def counter_example_instance() -> List[Job]:
    """Return an instance where shortest_job_first is strictly worse than EDF."""
    # Job 0: deadline 1, length 2 (urgent but long).
    # Job 1: deadline 10, length 1 (not urgent, but short).
    # SJF runs job 1 first (finishes at 1, on time), then job 0 (finishes at
    # 3, late by 2) -> max lateness 2.
    # EDF runs job 0 first (finishes at 2, late by 1), then job 1 (finishes
    # at 3, on time) -> max lateness 1.
    return [(1, 2), (10, 1)]


if __name__ == "__main__":
    instance = counter_example_instance()
    _, sjf_lateness = shortest_job_first(instance)
    _, edf_lateness = earliest_deadline_first(instance)

    assert sjf_lateness > edf_lateness, (
        f"shortest-job-first lateness = {sjf_lateness}, "
        f"earliest-deadline-first lateness = {edf_lateness}"
    )

    print(f"shortest-job-first max lateness = {sjf_lateness}; "
          f"EDF max lateness = {edf_lateness}.")
    print("All tests passed!")
