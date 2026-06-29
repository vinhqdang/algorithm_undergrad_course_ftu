"""
Problem 04 - Vertex Cover via Bounded-Search-Tree FPT
======================================================

Implement `vertex_cover_fpt(n, edges, k)`: decide whether the graph has a
vertex cover of size <= k, returning the cover (a set of vertices) or None.

Use the bounded search tree: while uncovered edges remain and budget > 0, pick
any uncovered edge (u, v); at least one of u, v must be in the cover, so branch
on adding u (recurse with budget k-1) and on adding v. Depth k, branching
factor 2 gives O(2^k) leaves, hence O(2^k * (n+m)) overall -- FPT in k.

See practical_exercises.pdf, Problem 4.
"""

import os
import sys
from typing import List, Optional, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import is_vertex_cover  # noqa: E402

Edge = Tuple[int, int]


def vertex_cover_fpt(n: int, edges: List[Edge], k: int) -> Optional[Set[int]]:
    """Return a vertex cover of size <= k, or None if none exists."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        n, edges = 3, [(0, 1), (1, 2), (0, 2)]
        assert vertex_cover_fpt(n, edges, 1) is None
        cover = vertex_cover_fpt(n, edges, 2)
        assert cover is not None and len(cover) <= 2 and is_vertex_cover(edges, cover)

        n, edges = 4, [(0, 1), (1, 2), (2, 3)]
        assert vertex_cover_fpt(n, edges, 1) is None
        cover = vertex_cover_fpt(n, edges, 2)
        assert cover is not None and is_vertex_cover(edges, cover)

        assert vertex_cover_fpt(5, [], 0) == set()

        n, edges = 5, [(0, 1), (0, 2), (0, 3), (0, 4)]
        assert vertex_cover_fpt(n, edges, 1) == {0}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
