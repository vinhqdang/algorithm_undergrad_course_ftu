"""
Problem 06 - Kernelization for Vertex Cover
============================================

Implement `kernelize_vertex_cover(n, edges, k)` applying two reduction rules
exhaustively for the parameterized problem "is there a cover of size <= k?":

  Rule 1 (high degree): any vertex of degree > k must be in every cover of
    size <= k. Force it into the cover, delete it and its incident edges, and
    decrement k.
  Rule 2 (isolated vertices): a degree-0 vertex covers nothing, so drop it.

Return ``(remaining_vertices, remaining_edges, k_reduced, forced)`` where
``forced`` is the set of vertices forced into the cover by Rule 1. The original
instance is a yes-instance iff the reduced one is (with budget ``k_reduced``).

The helper `edges_to_adj` in starter_code.py builds adjacency sets.

See practical_exercises.pdf, Problem 6.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import edges_to_adj  # noqa: E402

Edge = Tuple[int, int]


def kernelize_vertex_cover(n: int, edges: List[Edge], k: int):
    """Apply the high-degree and isolated-vertex rules until none fires."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        n = 6
        edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
        verts, red_edges, k_red, forced = kernelize_vertex_cover(n, edges, k=1)
        assert forced == {0}
        assert red_edges == []
        assert verts == []
        assert k_red == 0

        verts, red_edges, k_red, forced = kernelize_vertex_cover(n, edges, k=5)
        assert forced == set()
        assert sorted(red_edges) == sorted(edges)
        assert k_red == 5
        assert set(verts) == set(range(6))

        n = 5
        edges = [(0, 1), (1, 2), (0, 2), (2, 3)]
        verts, red_edges, k_red, forced = kernelize_vertex_cover(n, edges, k=10)
        assert 4 not in verts
        assert set(red_edges) == set(edges)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
