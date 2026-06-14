"""
Problem 15 - Exchange Argument Practice: Inversions and Idle Time
====================================================================

The exchange-argument proof that earliest-deadline-first (EDF) is optimal for
minimizing lateness (Kleinberg & Tardos, Ch 4.2) relies on two structural
facts about an optimal schedule:

  1. It has NO IDLE TIME: since all jobs are available at time 0 and the
     resource processes one job at a time without preemption, an optimal
     schedule never leaves the resource idle while a job remains to be
     processed (idle time can always be removed without increasing any
     finish time).

  2. It has NO INVERSIONS: an "inversion" is a pair of jobs (i, j) such that
     `i` is scheduled before `j` but `deadline[i] > deadline[j]` (i.e. the
     later-deadline job is scheduled first). EDF produces a schedule with NO
     inversions and NO idle time, and the exchange argument shows that
     "swapping" any inverted adjacent pair never increases the max lateness.

Implement two functions, both taking `jobs` (a list of `(deadline, length)`)
and `order` (a list of original indices, e.g. as returned by Problem 11):

  - `count_inversions(jobs, order)`: return the number of pairs `(a, b)` with
    `a < b` (positions in `order`) such that
    `jobs[order[a]][0] > jobs[order[b]][0]` (the job scheduled earlier has a
    STRICTLY LATER deadline than the job scheduled after it).

  - `has_idle_time(jobs, order)`: in this simplified model (all jobs
    available at time 0, processed back-to-back), idle time is never
    introduced by construction, so this should always return False for any
    `order` that is a permutation of `range(len(jobs))`. Implement it anyway
    as a basic sanity check: return True iff `sorted(order) !=
    list(range(len(jobs)))` (i.e. `order` is not a valid permutation, which
    would indicate a malformed schedule).

See practical_exercises.pdf, Problem 15.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem11 import earliest_deadline_first

Job = Tuple[float, float]


def count_inversions(jobs: List[Job], order: List[int]) -> int:
    """Return the number of inversions (earlier job has a strictly later deadline) in `order`."""
    # TODO: implement this function.
    raise NotImplementedError


def has_idle_time(jobs: List[Job], order: List[int]) -> bool:
    """Return True iff `order` is not a valid permutation of range(len(jobs))."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        jobs = [(2, 1), (4, 2), (6, 3), (8, 4), (9, 3), (15, 2)]

        # EDF order is sorted by deadline -> zero inversions.
        edf_order, _ = earliest_deadline_first(jobs)
        assert count_inversions(jobs, edf_order) == 0
        assert has_idle_time(jobs, edf_order) is False

        # Reversed order has the maximum number of inversions: C(6,2) = 15.
        reversed_order = list(reversed(edf_order))
        assert count_inversions(jobs, reversed_order) == 15

        # A single adjacent swap of two jobs with different deadlines
        # introduces exactly one inversion.
        swapped = edf_order.copy()
        swapped[0], swapped[1] = swapped[1], swapped[0]
        assert count_inversions(jobs, swapped) == 1

        # A malformed "order" (not a permutation) should be flagged.
        assert has_idle_time(jobs, [0, 0, 1, 2, 3, 4]) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
