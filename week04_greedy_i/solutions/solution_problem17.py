"""
Problem 17 - Online Caching: Least-Recently-Used (LRU) (SOLUTION)
=====================================================================
"""

from collections import OrderedDict
from typing import Sequence, TypeVar

T = TypeVar("T")


def least_recently_used(seq: Sequence[T], k: int) -> int:
    """Return the number of cache misses using the least-recently-used eviction policy."""
    cache: "OrderedDict[T, None]" = OrderedDict()
    misses = 0

    for item in seq:
        if item in cache:
            cache.move_to_end(item)
            continue

        misses += 1
        if len(cache) >= k:
            cache.popitem(last=False)  # evict least-recently-used (front)
        cache[item] = None

    return misses


if __name__ == "__main__":
    assert least_recently_used([1, 2, 1, 2, 1, 2], k=1) == 6
    assert least_recently_used([1, 2, 1, 2, 1, 2], k=2) == 2
    assert least_recently_used([], k=3) == 0
    assert least_recently_used([1, 2, 3, 1, 2, 3], k=3) == 3
    assert least_recently_used(["A", "B", "C", "B", "A"], k=2) == 4

    print("All tests passed!")
