"""
Problem 08 - Vertex-Disjoint s-t Paths via Node Splitting (SOLUTION)
====================================================================
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import MaxFlow

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def max_vertex_disjoint_paths(
    vertices: List[Vertex], directed_edges: List[Edge], s: Vertex, t: Vertex
) -> int:
    """Maximum number of internally vertex-disjoint directed s->t paths.

    Node-splitting reduction: split every internal vertex v into v_in -> v_out
    with capacity 1 (this caps how many paths may pass THROUGH v). An original
    edge (u, v) becomes u_out -> v_in with capacity 1. s and t are not capped
    (we model them as s_out and t_in directly). The max flow then counts paths
    that share no internal vertex.
    """
    mf = MaxFlow()

    def out_node(v: Vertex):
        # s and t are kept "uncapped"; internal nodes use their _out half.
        return (v, "out")

    def in_node(v: Vertex):
        return (v, "in")

    for v in vertices:
        if v == s or v == t:
            continue
        mf.add_edge(in_node(v), out_node(v), 1)

    for u, v in directed_edges:
        u_side = out_node(u) if u != s else (s, "src")
        v_side = in_node(v) if v != t else (t, "snk")
        # Map s's outgoing and t's incoming consistently.
        src = (s, "src") if u == s else out_node(u)
        dst = (t, "snk") if v == t else in_node(v)
        mf.add_edge(src, dst, 1)

    return int(round(mf.max_flow((s, "src"), (t, "snk"))))


if __name__ == "__main__":
    # Two vertex-disjoint paths: s->a->t and s->b->t.
    V = ["s", "a", "b", "t"]
    E = [("s", "a"), ("a", "t"), ("s", "b"), ("b", "t")]
    assert max_vertex_disjoint_paths(V, E, "s", "t") == 2

    # Edge-disjoint but NOT vertex-disjoint: both paths pass through m.
    # s->a->m->t and s->b->m->t share internal vertex m, so only 1 vertex-disjoint path.
    V2 = ["s", "a", "b", "m", "t"]
    E2 = [("s", "a"), ("s", "b"), ("a", "m"), ("b", "m"), ("m", "t")]
    assert max_vertex_disjoint_paths(V2, E2, "s", "t") == 1

    # Three vertex-disjoint paths.
    V3 = ["s", "t", "x", "y", "z"]
    E3 = [("s", "x"), ("x", "t"), ("s", "y"), ("y", "t"), ("s", "z"), ("z", "t")]
    assert max_vertex_disjoint_paths(V3, E3, "s", "t") == 3

    # No path.
    assert max_vertex_disjoint_paths(["s", "t", "a"], [("s", "a")], "s", "t") == 0

    # Direct edge s->t (no internal vertices) gives one path.
    assert max_vertex_disjoint_paths(["s", "t"], [("s", "t")], "s", "t") == 1

    print("All tests passed!")
