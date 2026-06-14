"""
Problem 03 - Earliest-Finish-Time-First Interval Scheduling
==============================================================

Implement `earliest_finish_time_first(intervals)`, the classic greedy
algorithm for the Interval Scheduling Problem:

    Sort requests by finish time. Repeatedly select the request with the
    earliest finish time among those still compatible (not overlapping any
    request already selected), and discard all requests that overlap it.

Return the selected intervals as a list, in the order they were selected
(which is also increasing order of finish time).

Use `is_feasible` from starter_code.py to sanity-check your result in the
tests below.

See practical_exercises.pdf, Problem 3.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import is_feasible

Interval = Tuple[float, float]


def earliest_finish_time_first(intervals: List[Interval]) -> List[Interval]:
    """Return a maximal feasible set of intervals chosen greedily by earliest finish time."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Classic textbook example (Kleinberg & Tardos, Ch 4, Figure 4.1):
        # 6 requests, the greedy choice picks 3 non-overlapping ones.
        intervals = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
        chosen = earliest_finish_time_first(intervals)
        assert is_feasible(chosen)
        # Earliest finish time first should pick (1,4) first.
        assert chosen[0] == (1, 4)

        # No overlaps at all -> select everything
        disjoint = [(0, 1), (1, 2), (2, 3)]
        chosen2 = earliest_finish_time_first(disjoint)
        assert sorted(chosen2) == disjoint
        assert is_feasible(chosen2)

        # Empty input
        assert earliest_finish_time_first([]) == []

        # All intervals identical -> only one can be chosen
        same = [(0, 5), (0, 5), (0, 5)]
        chosen3 = earliest_finish_time_first(same)
        assert len(chosen3) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
