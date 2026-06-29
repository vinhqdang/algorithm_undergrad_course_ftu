"""
Problem 12 - Set Cover via Bitmask / FPT Search (SOLUTION)
==========================================================

Set Cover: given a universe and a family of subsets, find the fewest subsets
whose union is the whole universe. Parameterizing by the solution size k, we
search the branching tree: pick any still-uncovered element, branch over the
(few) sets that cover it. We verify against brute force on small instances.
"""

import itertools
import os
import random
import sys
from typing import List, Optional, Set

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa: E402


def _to_mask(s: Set[int]) -> int:
    m = 0
    for x in s:
        m |= (1 << x)
    return m


def set_cover_fpt(universe: Set[int], subsets: List[Set[int]], k: int) -> Optional[List[int]]:
    """Return indices of <= k subsets whose union is ``universe``, or None.

    Branches on an uncovered element over the sets containing it (bounded
    search tree of depth k).
    """
    full = _to_mask(universe)
    masks = [_to_mask(s) for s in subsets]

    best: Optional[List[int]] = None

    def search(covered: int, budget: int, chosen: List[int]):
        nonlocal best
        if covered == full:
            if best is None or len(chosen) < len(best):
                best = list(chosen)
            return
        if budget == 0:
            return
        # Choose an uncovered element to branch on.
        uncovered = full & ~covered
        elem = (uncovered & -uncovered).bit_length() - 1  # lowest set bit index
        for i, m in enumerate(masks):
            if i in chosen:
                continue
            if m & (1 << elem):
                chosen.append(i)
                search(covered | m, budget - 1, chosen)
                chosen.pop()

    search(0, k, [])
    return best


def min_set_cover_via_fpt(universe: Set[int], subsets: List[Set[int]]) -> Optional[List[int]]:
    """Smallest cover by trying k = 0, 1, ... up to len(subsets)."""
    for k in range(len(subsets) + 1):
        res = set_cover_fpt(universe, subsets, k)
        if res is not None:
            return res
    return None


def brute_force_set_cover(universe: Set[int], subsets: List[Set[int]]) -> Optional[int]:
    """Minimum number of subsets covering the universe, by trying all sizes."""
    n = len(subsets)
    for size in range(n + 1):
        for combo in itertools.combinations(range(n), size):
            union: Set[int] = set()
            for i in combo:
                union |= subsets[i]
            if union >= universe:
                return size
    return None


if __name__ == "__main__":
    universe = {0, 1, 2, 3, 4}
    subsets = [{0, 1, 2}, {2, 3}, {3, 4}, {0, 4}]
    cover = min_set_cover_via_fpt(universe, subsets)
    assert cover is not None
    union = set()
    for i in cover:
        union |= subsets[i]
    assert union >= universe
    assert len(cover) == brute_force_set_cover(universe, subsets) == 2

    # No cover possible (element 9 in no subset).
    assert min_set_cover_via_fpt({9}, [{0}, {1}]) is None

    # Randomized verification vs brute force.
    rng = random.Random(123)
    for _ in range(200):
        u_size = rng.randint(1, 8)
        universe = set(range(u_size))
        num_sets = rng.randint(1, 7)
        subsets = []
        for _ in range(num_sets):
            sz = rng.randint(0, u_size)
            subsets.append(set(rng.sample(range(u_size), sz)))
        cover = min_set_cover_via_fpt(universe, subsets)
        bf = brute_force_set_cover(universe, subsets)
        if bf is None:
            assert cover is None
        else:
            assert cover is not None and len(cover) == bf

    print("All tests passed!")
