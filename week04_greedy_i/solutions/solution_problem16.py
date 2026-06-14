"""
Problem 16 - Optimal Caching: Furthest-In-Future (Belady's Algorithm) (SOLUTION)
====================================================================================
"""

from typing import Sequence, TypeVar

T = TypeVar("T")


def furthest_in_future(seq: Sequence[T], k: int) -> int:
    """Return the number of cache misses using the furthest-in-future eviction policy."""
    cache: set = set()
    misses = 0
    n = len(seq)

    for i, item in enumerate(seq):
        if item in cache:
            continue

        misses += 1
        if len(cache) < k:
            cache.add(item)
            continue

        # Cache is full: evict the item whose next use is furthest away
        # (or never used again).
        def next_use(x: T) -> float:
            for j in range(i + 1, n):
                if seq[j] == x:
                    return j
            return float("inf")

        evict = max(cache, key=next_use)
        cache.remove(evict)
        cache.add(item)

    return misses


if __name__ == "__main__":
    assert furthest_in_future([1, 2, 1, 2, 1, 2], k=1) == 6
    assert furthest_in_future([1, 2, 1, 2, 1, 2], k=2) == 2
    assert furthest_in_future(["A", "B", "C", "B", "A"], k=2) == 4
    assert furthest_in_future([], k=3) == 0
    assert furthest_in_future([1, 2, 3, 1, 2, 3], k=3) == 3

    print("All tests passed!")
