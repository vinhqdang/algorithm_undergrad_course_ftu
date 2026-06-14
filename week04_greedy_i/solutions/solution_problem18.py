"""
Problem 18 - Comparing Furthest-In-Future and LRU (SOLUTION)
================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem16 import furthest_in_future
from solution_problem17 import least_recently_used


def construct_bad_sequence_for_lru(k: int = 2) -> Tuple[List[int], int]:
    """Return (seq, k) such that LRU makes strictly more misses than furthest-in-future."""
    # Cyclic access pattern over k+1 distinct items, repeated several times.
    # A cache of size k can never hold all k+1 items, so every policy misses
    # repeatedly -- but LRU evicts exactly the item that is about to be
    # needed again on every step (a "thrashing" worst case), while
    # furthest-in-future can occasionally get a hit by keeping an item whose
    # next use is sooner.
    items = list(range(k + 1))
    seq = items * 3
    return seq, k


def compare_policies(seq: List[int], k: int) -> Tuple[int, int]:
    """Return (furthest_in_future_misses, lru_misses) for the given sequence and cache size."""
    return furthest_in_future(seq, k), least_recently_used(seq, k)


if __name__ == "__main__":
    seq, k = construct_bad_sequence_for_lru(k=2)
    fif_misses, lru_misses = compare_policies(seq, k)

    assert fif_misses < lru_misses, (
        f"furthest-in-future misses = {fif_misses}, LRU misses = {lru_misses}"
    )
    assert fif_misses <= lru_misses

    print(f"Sequence: {seq}, k={k}")
    print(f"furthest-in-future misses = {fif_misses}, LRU misses = {lru_misses}")
    print("All tests passed!")
