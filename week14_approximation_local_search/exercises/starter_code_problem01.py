"""
Problem 01 - Vertex Cover via Maximal Matching
===============================================

Implement `vertex_cover_matching(graph)`, where `graph` is a tuple (n, edges).
Scan the edges; whenever an edge (u, v) has NEITHER endpoint already in the
cover, add BOTH u and v to the cover. Return the cover as a set of vertices.

This is the classic 2-approximation: the cover is exactly the set of endpoints
of a maximal matching, and any vertex cover must contain at least one endpoint
of each matched (vertex-disjoint) edge.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

import os
import sys
from typing import List, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import is_vertex_cover  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def vertex_cover_matching(graph: Graph) -> Set[int]:
    """Return a vertex cover by taking both endpoints of a maximal matching."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g = (4, [(0, 1), (1, 2), (2, 3)])
        cover = vertex_cover_matching(g)
        assert is_vertex_cover(g, cover)
        assert cover == {0, 1, 2, 3}

        tri = (3, [(0, 1), (0, 2), (1, 2)])
        cover = vertex_cover_matching(tri)
        assert is_vertex_cover(tri, cover)
        assert len(cover) == 2

        assert vertex_cover_matching((5, [])) == set()

        star = (4, [(0, 1), (0, 2), (0, 3)])
        cover = vertex_cover_matching(star)
        assert is_vertex_cover(star, cover)
        assert cover == {0, 1}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
