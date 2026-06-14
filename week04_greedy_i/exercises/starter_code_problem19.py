"""
Problem 19 - Brute-Force Optimal Caching and Verifying FIF Optimality
========================================================================

For small sequences, implement `brute_force_min_misses(seq, k)` that tries
ALL possible eviction strategies and returns the minimum possible number of
cache misses.

Concretely: process `seq` position by position. At each position, the cache
state is a frozenset of at most `k` items. On a miss with a full cache, there
are up to `k` choices of which item to evict. Use a recursive
search (with memoization on `(position, frozenset(cache))` to keep it
tractable) to find the minimum total misses over all sequences of eviction
choices.

This is exponential and only intended for short sequences (say len(seq) <=
12) and small `k` (say <= 3); it exists so we can empirically verify that
`furthest_in_future` (Problem 16) is optimal.

Then implement `verify_fif_optimal(seqs, k)` that returns True iff, for every
sequence `seq` in `seqs`, `furthest_in_future(seq, k) ==
brute_force_min_misses(seq, k)`.

See practical_exercises.pdf, Problem 19.
"""

import os
import sys
from functools import lru_cache
from typing import List, Sequence, Tuple, TypeVar

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem16 import furthest_in_future

T = TypeVar("T")


def brute_force_min_misses(seq: Sequence[T], k: int) -> int:
    """Return the minimum possible number of cache misses over all eviction strategies."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_fif_optimal(seqs: List[Sequence[T]], k: int) -> bool:
    """Return True iff furthest_in_future matches brute_force_min_misses on every sequence in `seqs`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Empty sequence -> 0 misses regardless of strategy.
        assert brute_force_min_misses([], k=2) == 0

        # k >= distinct items -> exactly one miss per distinct item, no choices matter.
        assert brute_force_min_misses([1, 2, 3, 1, 2, 3], k=3) == 3

        # The A B C B A example from Problem 16: optimal is 4.
        assert brute_force_min_misses(["A", "B", "C", "B", "A"], k=2) == 4

        sequences = [
            [1, 2, 1, 2, 1, 2],
            ["A", "B", "C", "B", "A"],
            [1, 2, 3, 1, 2, 3, 1],
            [1, 2, 3, 4, 1, 2, 3, 4],
        ]
        assert verify_fif_optimal(sequences, k=2) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
