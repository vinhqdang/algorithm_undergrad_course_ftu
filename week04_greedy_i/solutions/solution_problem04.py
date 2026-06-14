"""
Problem 04 - Brute-Force Optimal Interval Scheduling (SOLUTION)
==================================================================
"""

import os
import sys
from itertools import combinations
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import is_feasible

Interval = Tuple[float, float]


def brute_force_max_independent_set(intervals: List[Interval]) -> List[Interval]:
    """Return a largest feasible subset of `intervals` (by brute force over all subsets)."""
    n = len(intervals)
    best: List[Interval] = []
    for size in range(n, 0, -1):
        for combo in combinations(intervals, size):
            if is_feasible(list(combo)):
                return list(combo)
    return best


if __name__ == "__main__":
    intervals = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
    best = brute_force_max_independent_set(intervals)
    assert is_feasible(best)
    assert len(best) == 3

    assert brute_force_max_independent_set([]) == []

    all_overlap = [(0, 5), (1, 5), (2, 5)]
    best2 = brute_force_max_independent_set(all_overlap)
    assert len(best2) == 1
    assert is_feasible(best2)

    disjoint = [(0, 1), (1, 2), (2, 3)]
    best3 = brute_force_max_independent_set(disjoint)
    assert len(best3) == 3

    print("All tests passed!")
