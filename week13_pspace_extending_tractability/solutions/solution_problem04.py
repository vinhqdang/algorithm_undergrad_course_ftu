"""
Problem 04 - Vertex Cover via Bounded-Search-Tree FPT (SOLUTION)
================================================================

Decide whether a vertex cover of size <= k exists in O(2^k * (n+m)) time by
branching on the two endpoints of any uncovered edge: at least one endpoint
must be in the cover.
"""

import os
import sys
from typing import List, Optional, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import is_vertex_cover  # noqa: E402

Edge = Tuple[int, int]


def vertex_cover_fpt(n: int, edges: List[Edge], k: int) -> Optional[Set[int]]:
    """Return a vertex cover of size <= k, or None if none exists.

    Branches on the endpoints of an uncovered edge (bounded search tree of
    depth k, branching factor 2 -> O(2^k) leaves).
    """

    def search(remaining_edges: List[Edge], budget: int, chosen: Set[int]) -> Optional[Set[int]]:
        if not remaining_edges:
            return set(chosen)  # all edges covered
        if budget == 0:
            return None  # out of budget but edges remain
        # Pick any uncovered edge to branch on.
        u, v = remaining_edges[0]
        for endpoint in (u, v):
            chosen.add(endpoint)
            rest = [(a, b) for (a, b) in remaining_edges if a != endpoint and b != endpoint]
            result = search(rest, budget - 1, chosen)
            if result is not None:
                return result
            chosen.discard(endpoint)
        return None

    return search(list(edges), k, set())


if __name__ == "__main__":
    # Triangle: minimum vertex cover is 2.
    n, edges = 3, [(0, 1), (1, 2), (0, 2)]
    assert vertex_cover_fpt(n, edges, 1) is None
    cover = vertex_cover_fpt(n, edges, 2)
    assert cover is not None and len(cover) <= 2 and is_vertex_cover(edges, cover)

    # Path 0-1-2-3: minimum cover is 2 (e.g. {1, 2}).
    n, edges = 4, [(0, 1), (1, 2), (2, 3)]
    assert vertex_cover_fpt(n, edges, 1) is None
    cover = vertex_cover_fpt(n, edges, 2)
    assert cover is not None and is_vertex_cover(edges, cover)

    # Empty graph: cover of size 0 works.
    assert vertex_cover_fpt(5, [], 0) == set()

    # Star with center 0 and 4 leaves: cover {0} of size 1.
    n, edges = 5, [(0, 1), (0, 2), (0, 3), (0, 4)]
    cover = vertex_cover_fpt(n, edges, 1)
    assert cover == {0}

    print("All tests passed!")
