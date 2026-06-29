"""
Problem 12 - Set Cover via Bitmask / FPT Search
================================================

Implement `set_cover_fpt(universe, subsets, k)` returning the indices of at
most ``k`` subsets whose union is ``universe`` (the smallest such found), or
None if no cover of size <= k exists.

Use a bounded search tree parameterized by k: while elements remain uncovered
and budget > 0, pick any uncovered element and branch over the subsets that
contain it (one of them must be chosen). Represent covered sets as bitmasks for
speed.

Also implement `min_set_cover_via_fpt(universe, subsets)` (try k = 0, 1, ...).
Verify against `brute_force_set_cover` (provided) on small random instances.

See practical_exercises.pdf, Problem 12.
"""

import itertools
from typing import List, Optional, Set


def brute_force_set_cover(universe: Set[int], subsets: List[Set[int]]) -> Optional[int]:
    """Minimum number of subsets covering the universe; provided for verification."""
    n = len(subsets)
    for size in range(n + 1):
        for combo in itertools.combinations(range(n), size):
            union: Set[int] = set()
            for i in combo:
                union |= subsets[i]
            if union >= universe:
                return size
    return None


def set_cover_fpt(universe: Set[int], subsets: List[Set[int]], k: int) -> Optional[List[int]]:
    """Return indices of <= k subsets covering ``universe``, or None."""
    # TODO: implement this function.
    raise NotImplementedError


def min_set_cover_via_fpt(universe: Set[int], subsets: List[Set[int]]) -> Optional[List[int]]:
    """Smallest cover by trying k = 0, 1, ..., len(subsets)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        import random

        universe = {0, 1, 2, 3, 4}
        subsets = [{0, 1, 2}, {2, 3}, {3, 4}, {0, 4}]
        cover = min_set_cover_via_fpt(universe, subsets)
        assert cover is not None
        union = set()
        for i in cover:
            union |= subsets[i]
        assert union >= universe
        assert len(cover) == brute_force_set_cover(universe, subsets) == 2

        assert min_set_cover_via_fpt({9}, [{0}, {1}]) is None

        rng = random.Random(123)
        for _ in range(200):
            u_size = rng.randint(1, 8)
            uni = set(range(u_size))
            num_sets = rng.randint(1, 7)
            subs = []
            for _ in range(num_sets):
                sz = rng.randint(0, u_size)
                subs.append(set(rng.sample(range(u_size), sz)))
            cover = min_set_cover_via_fpt(uni, subs)
            bf = brute_force_set_cover(uni, subs)
            if bf is None:
                assert cover is None
            else:
                assert cover is not None and len(cover) == bf

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
