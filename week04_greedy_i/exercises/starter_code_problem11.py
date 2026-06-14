"""
Problem 11 - Earliest-Deadline-First Scheduling (Minimizing Lateness)
========================================================================

In the Minimizing Lateness problem, a single resource (e.g. a machine) must
process `n` jobs, where job `i` has a processing time (length) `t_i` and a
deadline `d_i`. All jobs are available at time 0 and must be processed
without preemption, one at a time. If job `i` finishes at time `f_i`, its
LATENESS is `max(0, f_i - d_i)`. The goal is to minimize the MAXIMUM lateness
over all jobs.

Implement `earliest_deadline_first(jobs)`:
    Sort jobs by deadline, ascending (ties broken arbitrarily), and schedule
    them back-to-back in that order starting at time 0.

`jobs` is a list of `(deadline, length)` tuples (matching the `Job` type in
starter_code.py). Return a tuple `(order, max_lateness)` where `order` is the
list of ORIGINAL INDICES into `jobs` in the order they are scheduled, and
`max_lateness` is the resulting maximum lateness (use `schedule_lateness`
from starter_code.py to compute it).

See practical_exercises.pdf, Problem 11.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import schedule_lateness

Job = Tuple[float, float]


def earliest_deadline_first(jobs: List[Job]) -> Tuple[List[int], float]:
    """Return (order, max_lateness) for the earliest-deadline-first schedule."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Classic textbook example (Kleinberg & Tardos, Ch 4.2, Table 4.2):
        # jobs indexed 0..5 with (deadline, length):
        jobs = [
            (2, 1),   # job 0: length 1, deadline 2
            (4, 2),   # job 1: length 2, deadline 4
            (6, 3),   # job 2: length 3, deadline 6
            (8, 4),   # job 3: length 4, deadline 8
            (9, 3),   # job 4: length 3, deadline 9
            (15, 2),  # job 5: length 2, deadline 15
        ]
        order, max_lateness = earliest_deadline_first(jobs)

        # EDF order should be by increasing deadline: 0,1,2,3,4,5
        assert order == [0, 1, 2, 3, 4, 5]
        # Finish times are 1,3,6,10,13,15 and deadlines are 2,4,6,8,9,15, so
        # the maximum lateness is max(0,-1,0,0,2,4,0) = 4 (job 4).
        assert max_lateness == 4

        # A single job is always feasible: lateness = max(0, length - deadline).
        single = [(5, 10)]
        order2, lateness2 = earliest_deadline_first(single)
        assert order2 == [0]
        assert lateness2 == 5  # finishes at time 10, deadline 5 -> lateness 5

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
