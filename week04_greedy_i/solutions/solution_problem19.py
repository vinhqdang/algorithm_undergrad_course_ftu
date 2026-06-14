"""
Problem 19 - Brute-Force Optimal Caching and Verifying FIF Optimality (SOLUTION)
====================================================================================
"""

import os
import sys
from functools import lru_cache
from itertools import combinations
from typing import List, Sequence, Tuple, TypeVar

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem16 import furthest_in_future

T = TypeVar("T")


def brute_force_min_misses(seq: Sequence[T], k: int) -> int:
    """Return the minimum possible number of cache misses over all eviction strategies."""
    seq = tuple(seq)
    n = len(seq)

    @lru_cache(maxsize=None)
    def search(pos: int, cache: frozenset) -> int:
        if pos == n:
            return 0

        item = seq[pos]
        if item in cache:
            return search(pos + 1, cache)

        # Miss: pay 1, then choose how to add `item` to the cache.
        if len(cache) < k:
            new_cache = frozenset(cache | {item})
            return 1 + search(pos + 1, new_cache)

        # Cache full: try evicting each possible item.
        best = None
        for evict in cache:
            new_cache = frozenset((cache - {evict}) | {item})
            cost = 1 + search(pos + 1, new_cache)
            if best is None or cost < best:
                best = cost
        return best

    result = search(0, frozenset())
    search.cache_clear()
    return result


def verify_fif_optimal(seqs: List[Sequence[T]], k: int) -> bool:
    """Return True iff furthest_in_future matches brute_force_min_misses on every sequence in `seqs`."""
    for seq in seqs:
        if furthest_in_future(seq, k) != brute_force_min_misses(seq, k):
            return False
    return True


if __name__ == "__main__":
    assert brute_force_min_misses([], k=2) == 0
    assert brute_force_min_misses([1, 2, 3, 1, 2, 3], k=3) == 3
    assert brute_force_min_misses(["A", "B", "C", "B", "A"], k=2) == 4

    sequences = [
        [1, 2, 1, 2, 1, 2],
        ["A", "B", "C", "B", "A"],
        [1, 2, 3, 1, 2, 3, 1],
        [1, 2, 3, 4, 1, 2, 3, 4],
    ]
    assert verify_fif_optimal(sequences, k=2) is True

    print("All tests passed!")
