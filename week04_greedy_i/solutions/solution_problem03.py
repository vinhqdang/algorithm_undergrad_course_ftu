"""
Problem 03 - Earliest-Finish-Time-First Interval Scheduling (SOLUTION)
==========================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import is_feasible

Interval = Tuple[float, float]


def earliest_finish_time_first(intervals: List[Interval]) -> List[Interval]:
    """Return a maximal feasible set of intervals chosen greedily by earliest finish time."""
    selected: List[Interval] = []
    last_finish = float("-inf")
    for s, f in sorted(intervals, key=lambda iv: iv[1]):
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f
    return selected


if __name__ == "__main__":
    intervals = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
    chosen = earliest_finish_time_first(intervals)
    assert is_feasible(chosen)
    assert chosen[0] == (1, 4)

    disjoint = [(0, 1), (1, 2), (2, 3)]
    chosen2 = earliest_finish_time_first(disjoint)
    assert sorted(chosen2) == disjoint
    assert is_feasible(chosen2)

    assert earliest_finish_time_first([]) == []

    same = [(0, 5), (0, 5), (0, 5)]
    chosen3 = earliest_finish_time_first(same)
    assert len(chosen3) == 1

    print("All tests passed!")
