"""
Problem 04 - Greedy Set Cover vs. the Optimum (SOLUTION)
========================================================
"""

import itertools
import os
import sys
from typing import List, Set

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from solution_problem03 import greedy_set_cover  # noqa: E402


def brute_force_min_set_cover(universe: Set, subsets: List[Set]) -> int:
    """Return the minimum number of subsets whose union is the universe."""
    universe = set(universe)
    indices = list(range(len(subsets)))
    for size in range(1, len(subsets) + 1):
        for combo in itertools.combinations(indices, size):
            if set().union(*(subsets[i] for i in combo)) >= universe:
                return size
    raise ValueError("subsets do not cover the universe")


def set_cover_ratio(universe: Set, subsets: List[Set]) -> float:
    """Return greedy_size / optimal_size."""
    greedy_size = len(greedy_set_cover(universe, subsets))
    opt_size = brute_force_min_set_cover(universe, subsets)
    return greedy_size / opt_size


if __name__ == "__main__":
    universe = {1, 2, 3, 4, 5}
    subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
    assert brute_force_min_set_cover(universe, subsets) == 2
    assert set_cover_ratio(universe, subsets) == 1.0  # greedy is optimal here

    # An instance where greedy is suboptimal: classic 2-row construction.
    # Universe split into two halves; greedy grabs a "diagonal" set first.
    U = set(range(1, 9))  # 1..8
    half1 = {1, 2, 3, 4}
    half2 = {5, 6, 7, 8}
    # A bait set covering 5 elements first, forcing extra picks afterwards.
    bait = {1, 2, 3, 4, 5}
    subsets2 = [bait, half1, half2]
    greedy = len(greedy_set_cover(U, subsets2))
    opt = brute_force_min_set_cover(U, subsets2)
    assert opt == 2  # half1 + half2
    assert greedy >= opt

    # The ratio must always be within the H_n guarantee.
    n = len(U)
    H_n = sum(1.0 / k for k in range(1, n + 1))
    assert set_cover_ratio(U, subsets2) <= H_n + 1e-9

    print("All tests passed!")
