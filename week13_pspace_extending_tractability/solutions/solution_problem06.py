"""
Problem 06 - Kernelization for Vertex Cover (SOLUTION)
=======================================================

Two reduction rules for the parameterized problem "is there a cover of size
<= k?":

  Rule 1 (high degree): any vertex of degree > k MUST be in every cover of
    size <= k (otherwise all > k of its edges would need distinct other
    endpoints). Force it into the cover, remove it and its edges, decrement k.

  Rule 2 (isolated vertices): a vertex of degree 0 covers no edge, so it is
    never needed; drop it.

Applying these exhaustively yields an equivalent "kernel" instance.
"""

import os
import sys
from typing import List, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import edges_to_adj  # noqa: E402

Edge = Tuple[int, int]


def kernelize_vertex_cover(n: int, edges: List[Edge], k: int):
    """Apply the high-degree and isolated-vertex rules until no rule fires.

    Returns ``(remaining_vertices, remaining_edges, k_reduced, forced)`` where
    ``forced`` is the set of vertices forced into the cover by Rule 1, and the
    original instance has a cover of size <= k iff the reduced instance has a
    cover of size <= k_reduced (then prepend ``forced``).
    """
    edges = list(edges)
    forced: Set[int] = set()
    active = set(range(n))

    changed = True
    while changed:
        changed = False
        adj = edges_to_adj(n, edges)
        # Rule 1: force any active vertex with degree > k.
        for v in list(active):
            deg = len(adj[v] & active)
            if deg > k:
                forced.add(v)
                active.discard(v)
                edges = [(a, b) for (a, b) in edges if a != v and b != v]
                k -= 1
                changed = True
                break
        if changed:
            continue
        # Rule 2: drop isolated active vertices.
        adj = edges_to_adj(n, edges)
        for v in list(active):
            if len(adj[v] & active) == 0 and v not in forced:
                active.discard(v)
                changed = True

    remaining_vertices = sorted(active)
    remaining_edges = sorted(set(edges))
    return remaining_vertices, remaining_edges, k, forced


if __name__ == "__main__":
    # Star: center 0 has degree 5 > k=1, so it is forced; rest become isolated.
    n = 6
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
    verts, red_edges, k_red, forced = kernelize_vertex_cover(n, edges, k=1)
    assert forced == {0}
    assert red_edges == []        # all edges removed with vertex 0
    assert verts == []            # leaves became isolated and were dropped
    assert k_red == 0

    # If k is large, the high-degree rule should NOT fire.
    verts, red_edges, k_red, forced = kernelize_vertex_cover(n, edges, k=5)
    assert forced == set()
    assert sorted(red_edges) == sorted(edges)
    assert k_red == 5
    # Isolated vertices (none here) dropped; all 6 are incident to an edge.
    assert set(verts) == set(range(6))

    # Graph with one isolated vertex (4) plus a triangle 0-1-2 and edge 2-3.
    n = 5
    edges = [(0, 1), (1, 2), (0, 2), (2, 3)]
    verts, red_edges, k_red, forced = kernelize_vertex_cover(n, edges, k=10)
    assert 4 not in verts          # isolated vertex dropped
    assert set(red_edges) == set(edges)

    print("All tests passed!")
