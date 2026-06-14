"""
Problem 17 - Online Caching: Least-Recently-Used (LRU)
=========================================================

Implement `least_recently_used(seq, k)`, the LEAST-RECENTLY-USED (LRU)
eviction policy:

    On a cache miss with a full cache, evict the item in the cache that was
    LEAST RECENTLY requested (i.e. whose most recent prior use is furthest in
    the PAST).

Return the total number of cache misses, exactly as in Problem 16's
`furthest_in_future`.

LRU is an ONLINE algorithm (it does not know the future), unlike
furthest-in-future which is OFFLINE (it looks ahead at the whole sequence).
Problem 18 asks you to compare the two.

See practical_exercises.pdf, Problem 17.
"""

from collections import OrderedDict
from typing import Sequence, TypeVar

T = TypeVar("T")


def least_recently_used(seq: Sequence[T], k: int) -> int:
    """Return the number of cache misses using the least-recently-used eviction policy."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Cache size 1: every distinct-from-previous request is a miss.
        assert least_recently_used([1, 2, 1, 2, 1, 2], k=1) == 6

        # Cache size 2, sequence fits entirely -> only the first two are misses.
        assert least_recently_used([1, 2, 1, 2, 1, 2], k=2) == 2

        # Empty sequence -> 0 misses.
        assert least_recently_used([], k=3) == 0

        # k >= number of distinct items -> exactly one miss per distinct item.
        assert least_recently_used([1, 2, 3, 1, 2, 3], k=3) == 3

        # A B C B A with k=2:
        # A: miss {A}
        # B: miss {A,B}
        # C: miss, evict A (least recently used) -> {B,C}
        # B: hit -> {C,B} (B becomes most recent)
        # A: miss, evict C (least recently used) -> {B,A}
        # Total misses: 4
        assert least_recently_used(["A", "B", "C", "B", "A"], k=2) == 4

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
