"""
Problem 07 - Subset-Sum Verifier and Brute-Force Decision
=========================================================

Implement:
  - verify_subset_sum(weights, subset_indices, target): True iff the items at
    those indices sum to exactly target.
  - subset_sum_exists(weights, target): brute force over all 2**n subsets;
    True iff some subset sums exactly to target.
  - find_subset_sum(weights, target): return a list of indices summing to
    target, or None.

See practical_exercises.pdf, Problem 7.
"""

import itertools
from typing import Iterable, List, Optional

Weights = List[int]


def verify_subset_sum(weights: Weights, subset_indices: Iterable[int], target: int) -> bool:
    """Return True iff sum of weights at the given indices equals target."""
    # TODO: implement this function.
    raise NotImplementedError


def subset_sum_exists(weights: Weights, target: int) -> bool:
    """Return True iff some subset of weights sums exactly to target."""
    # TODO: implement this function.
    raise NotImplementedError


def find_subset_sum(weights: Weights, target: int) -> Optional[List[int]]:
    """Return a list of indices whose weights sum to target, or None."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        w = [3, 34, 4, 12, 5, 2]
        assert subset_sum_exists(w, 9) is True
        assert subset_sum_exists(w, 36) is True
        assert subset_sum_exists(w, 35) is False
        assert subset_sum_exists(w, 1) is False
        assert subset_sum_exists(w, 0) is True

        idx = find_subset_sum(w, 9)
        assert idx is not None
        assert verify_subset_sum(w, idx, 9)

        assert find_subset_sum(w, 1) is None
        assert verify_subset_sum(w, [], 0) is True
        assert verify_subset_sum([5, 5, 5], [0, 2], 10) is True
        assert verify_subset_sum([5, 5, 5], [0], 10) is False

        assert subset_sum_exists(w, sum(w)) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
