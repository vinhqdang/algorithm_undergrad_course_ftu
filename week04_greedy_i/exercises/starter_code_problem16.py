"""
Problem 16 - Optimal Caching: Furthest-In-Future (Belady's Algorithm)
========================================================================

In the Optimal Caching (offline) problem, a cache can hold up to `k` items.
Given a sequence of requests `seq` (a list of hashable items, e.g. page
numbers), we must decide which item to EVICT whenever a requested item is not
already in the cache (a "cache miss") and the cache is full.

Implement `furthest_in_future(seq, k)`, the FURTHEST-IN-FUTURE (a.k.a.
Belady's MIN, or LFD -- "longest forward distance") eviction policy:

    On a cache miss with a full cache, evict the item in the cache whose NEXT
    use in `seq` (after the current position) is FURTHEST in the future (or
    that is never used again, which counts as "infinitely far").

Return the total number of cache MISSES (including the misses that occur the
first time any item is loaded into a not-yet-full cache).

This is provably optimal for the offline problem (Kleinberg & Tardos, Ch
4.4): no eviction policy achieves fewer misses on any request sequence.

See practical_exercises.pdf, Problem 16.
"""

from typing import List, Sequence, TypeVar

T = TypeVar("T")


def furthest_in_future(seq: Sequence[T], k: int) -> int:
    """Return the number of cache misses using the furthest-in-future eviction policy."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Cache size 1: every distinct-from-previous request is a miss.
        assert furthest_in_future([1, 2, 1, 2, 1, 2], k=1) == 6

        # Cache size 2, sequence fits entirely -> only the first two are misses.
        assert furthest_in_future([1, 2, 1, 2, 1, 2], k=2) == 2

        # Classic example: cache size 2, sequence A B C B A
        # A: miss (cache={A})
        # B: miss (cache={A,B})
        # C: miss, evict the one used furthest in future.
        #    A's next use: index 4. B's next use: index 3. Evict A (further).
        #    cache={B,C}
        # B: hit (cache={B,C})
        # A: miss, cache full {B,C}. B's next use: never. C's next use: never.
        #    Evict either (say B, the one earlier in cache order is fine).
        #    cache={A,C} or {A,B}
        # Total misses: A,B,C,A = 4
        assert furthest_in_future(["A", "B", "C", "B", "A"], k=2) == 4

        # Empty sequence -> 0 misses.
        assert furthest_in_future([], k=3) == 0

        # k >= number of distinct items -> exactly one miss per distinct item.
        assert furthest_in_future([1, 2, 3, 1, 2, 3], k=3) == 3

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
