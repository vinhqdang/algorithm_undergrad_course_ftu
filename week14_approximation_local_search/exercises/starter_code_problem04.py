"""
Problem 04 - Greedy Set Cover vs. the Optimum
==============================================

Implement `brute_force_min_set_cover(universe, subsets)` returning the minimum
number of subsets needed (try all sub-collections of size 1, 2, ...). Then
implement `set_cover_ratio(universe, subsets)` returning greedy_size / opt_size.

The greedy size never exceeds OPT by more than H_n = sum_{k=1}^{n} 1/k.

You may reuse `greedy_set_cover` from Problem 3 (re-implemented here for
self-containment).

See practical_exercises.pdf, Problem 4.
"""

import itertools
from typing import List, Set


def greedy_set_cover(universe: Set, subsets: List[Set]) -> List[int]:
    """Greedy set cover (copied from Problem 3)."""
    uncovered = set(universe)
    chosen: List[int] = []
    while uncovered:
        best_idx, best_gain = -1, -1
        for i, s in enumerate(subsets):
            gain = len(s & uncovered)
            if gain > best_gain:
                best_gain, best_idx = gain, i
        if best_gain <= 0:
            raise ValueError("subsets do not cover the universe")
        chosen.append(best_idx)
        uncovered -= subsets[best_idx]
    return chosen


def brute_force_min_set_cover(universe: Set, subsets: List[Set]) -> int:
    """Return the minimum number of subsets whose union is the universe."""
    # TODO: implement this function.
    raise NotImplementedError


def set_cover_ratio(universe: Set, subsets: List[Set]) -> float:
    """Return greedy_size / optimal_size."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        universe = {1, 2, 3, 4, 5}
        subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
        assert brute_force_min_set_cover(universe, subsets) == 2
        assert set_cover_ratio(universe, subsets) == 1.0

        U = set(range(1, 9))
        bait = {1, 2, 3, 4, 5}
        subsets2 = [bait, {1, 2, 3, 4}, {5, 6, 7, 8}]
        greedy = len(greedy_set_cover(U, subsets2))
        opt = brute_force_min_set_cover(U, subsets2)
        assert opt == 2
        assert greedy >= opt

        n = len(U)
        H_n = sum(1.0 / k for k in range(1, n + 1))
        assert set_cover_ratio(U, subsets2) <= H_n + 1e-9

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
