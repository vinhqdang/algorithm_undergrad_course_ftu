"""
Problem 01 - Vertex Cover via Maximal Matching (SOLUTION)
==========================================================
"""

import os
import sys
from typing import List, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import is_vertex_cover  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def vertex_cover_matching(graph: Graph) -> Set[int]:
    """Return a vertex cover by taking both endpoints of a maximal matching."""
    _, edges = graph
    cover: Set[int] = set()
    for u, v in edges:
        if u not in cover and v not in cover:
            cover.add(u)
            cover.add(v)
    assert is_vertex_cover(graph, cover)
    return cover


if __name__ == "__main__":
    # Path 0-1-2-3
    g = (4, [(0, 1), (1, 2), (2, 3)])
    cover = vertex_cover_matching(g)
    assert is_vertex_cover(g, cover)
    assert cover == {0, 1, 2, 3}

    # Triangle: any single matched edge covers two vertices, the third edge is then covered.
    tri = (3, [(0, 1), (0, 2), (1, 2)])
    cover = vertex_cover_matching(tri)
    assert is_vertex_cover(tri, cover)
    assert len(cover) == 2

    # Empty graph: empty cover.
    assert vertex_cover_matching((5, [])) == set()

    # Star: center 0 connected to 1,2,3 -> first edge (0,1) covers {0,1}, rest covered by 0.
    star = (4, [(0, 1), (0, 2), (0, 3)])
    cover = vertex_cover_matching(star)
    assert is_vertex_cover(star, cover)
    assert cover == {0, 1}

    print("All tests passed!")
