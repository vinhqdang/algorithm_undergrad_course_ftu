"""
Problem 18 - Comparing Furthest-In-Future and LRU
====================================================

LRU (Problem 17) is a reasonable "online" heuristic: it assumes that an item
not used recently is unlikely to be used soon. But this assumption can fail.

Implement `construct_bad_sequence_for_lru(k)` that returns a request sequence
(a list of small ints) and a cache size `k` such that:

    least_recently_used(seq, k) > furthest_in_future(seq, k)

i.e. LRU makes strictly MORE misses than the offline-optimal
furthest-in-future policy, on the SAME sequence and cache size.

Hint: a classic bad case for LRU is a "cyclic" access pattern with period
`k+1` over a cache of size `k`: e.g. for k=2, the sequence `0,1,2,0,1,2,0,1,2`
cycles through 3 items with a cache that holds only 2 -- LRU evicts the item
that is about to be needed again, every single time, while
furthest-in-future can do better by recognizing the cyclic pattern (though
for a perfectly uniform cycle the two may tie; you may need to break the
cycle's symmetry, e.g. by repeating it or adding a "load-bearing" prefix, to
get a strict inequality).

Then implement `compare_policies(seq, k)` returning a tuple
`(fif_misses, lru_misses)`.

See practical_exercises.pdf, Problem 18.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem16 import furthest_in_future
from solution_problem17 import least_recently_used


def construct_bad_sequence_for_lru(k: int = 2) -> Tuple[List[int], int]:
    """Return (seq, k) such that LRU makes strictly more misses than furthest-in-future."""
    # TODO: implement this function.
    raise NotImplementedError


def compare_policies(seq: List[int], k: int) -> Tuple[int, int]:
    """Return (furthest_in_future_misses, lru_misses) for the given sequence and cache size."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        seq, k = construct_bad_sequence_for_lru(k=2)
        fif_misses, lru_misses = compare_policies(seq, k)

        assert fif_misses < lru_misses, (
            f"furthest-in-future misses = {fif_misses}, LRU misses = {lru_misses}"
        )

        # furthest-in-future is always optimal: no policy beats it (we only
        # check LRU here, but this is the general claim).
        assert fif_misses <= lru_misses

        print(f"Sequence: {seq}, k={k}")
        print(f"furthest-in-future misses = {fif_misses}, LRU misses = {lru_misses}")
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
