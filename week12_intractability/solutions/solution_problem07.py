"""
Problem 07 - Subset-Sum Verifier and Brute-Force Decision (SOLUTION)
=====================================================================
"""

import itertools
from typing import Iterable, List, Optional

Weights = List[int]


def verify_subset_sum(weights: Weights, subset_indices: Iterable[int], target: int) -> bool:
    """Return True iff sum of weights at the given indices equals target."""
    return sum(weights[i] for i in subset_indices) == target


def subset_sum_exists(weights: Weights, target: int) -> bool:
    """Return True iff some subset of weights sums exactly to target."""
    n = len(weights)
    for r in range(n + 1):
        for combo in itertools.combinations(range(n), r):
            if sum(weights[i] for i in combo) == target:
                return True
    return False


def find_subset_sum(weights: Weights, target: int) -> Optional[List[int]]:
    """Return a list of indices whose weights sum to target, or None."""
    n = len(weights)
    for r in range(n + 1):
        for combo in itertools.combinations(range(n), r):
            if sum(weights[i] for i in combo) == target:
                return list(combo)
    return None


if __name__ == "__main__":
    w = [3, 34, 4, 12, 5, 2]
    assert subset_sum_exists(w, 9) is True            # 4 + 5
    assert subset_sum_exists(w, 36) is True           # 34 + 2
    assert subset_sum_exists(w, 35) is False
    assert subset_sum_exists(w, 1) is False
    assert subset_sum_exists(w, 0) is True            # empty subset

    idx = find_subset_sum(w, 9)
    assert idx is not None
    assert verify_subset_sum(w, idx, 9)

    assert find_subset_sum(w, 1) is None
    assert verify_subset_sum(w, [], 0) is True
    assert verify_subset_sum([5, 5, 5], [0, 2], 10) is True
    assert verify_subset_sum([5, 5, 5], [0], 10) is False

    # Sum of all
    assert subset_sum_exists(w, sum(w)) is True

    print("All tests passed!")
