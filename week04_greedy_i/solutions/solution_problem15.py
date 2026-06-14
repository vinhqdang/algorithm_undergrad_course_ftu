"""
Problem 15 - Exchange Argument Practice: Inversions and Idle Time (SOLUTION)
================================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem11 import earliest_deadline_first

Job = Tuple[float, float]


def count_inversions(jobs: List[Job], order: List[int]) -> int:
    """Return the number of inversions (earlier job has a strictly later deadline) in `order`."""
    n = len(order)
    inversions = 0
    for a in range(n):
        for b in range(a + 1, n):
            if jobs[order[a]][0] > jobs[order[b]][0]:
                inversions += 1
    return inversions


def has_idle_time(jobs: List[Job], order: List[int]) -> bool:
    """Return True iff `order` is not a valid permutation of range(len(jobs))."""
    return sorted(order) != list(range(len(jobs)))


if __name__ == "__main__":
    jobs = [(2, 1), (4, 2), (6, 3), (8, 4), (9, 3), (15, 2)]

    edf_order, _ = earliest_deadline_first(jobs)
    assert count_inversions(jobs, edf_order) == 0
    assert has_idle_time(jobs, edf_order) is False

    reversed_order = list(reversed(edf_order))
    assert count_inversions(jobs, reversed_order) == 15

    swapped = edf_order.copy()
    swapped[0], swapped[1] = swapped[1], swapped[0]
    assert count_inversions(jobs, swapped) == 1

    assert has_idle_time(jobs, [0, 0, 1, 2, 3, 4]) is True

    print("All tests passed!")
