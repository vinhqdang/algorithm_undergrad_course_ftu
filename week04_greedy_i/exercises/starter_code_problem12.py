"""
Problem 12 - Brute-Force Optimal Schedule for Minimizing Lateness
====================================================================

For small `n`, implement `brute_force_min_lateness(jobs)` that tries ALL
`n!` orderings (via `itertools.permutations`) of `jobs` (a list of
`(deadline, length)` tuples), computes the max lateness of each using
`schedule_lateness` from starter_code.py, and returns the MINIMUM possible
max lateness over all orderings, as a float.

This is factorial-time and only intended for small n (say n <= 8); it exists
so we can empirically verify that earliest-deadline-first (Problem 11) is
optimal (Problem 13).

See practical_exercises.pdf, Problem 12.
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
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # On the classic textbook example, EDF achieves max lateness 4, and it
        # is optimal -- brute force should also find 4.
        jobs = [(2, 1), (4, 2), (6, 3), (8, 4), (9, 3), (15, 2)]
        assert brute_force_min_lateness(jobs) == 4

        # Single job: only one ordering possible.
        single = [(5, 10)]
        assert brute_force_min_lateness(single) == 5

        # Two jobs where order matters:
        # Job A: deadline 1, length 2. Job B: deadline 10, length 1.
        # Order A,B: A finishes at 2 (late by 1), B finishes at 3 (on time) -> max lateness 1.
        # Order B,A: B finishes at 1 (on time), A finishes at 3 (late by 2) -> max lateness 2.
        # Optimal is 1.
        two_jobs = [(1, 2), (10, 1)]
        assert brute_force_min_lateness(two_jobs) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
