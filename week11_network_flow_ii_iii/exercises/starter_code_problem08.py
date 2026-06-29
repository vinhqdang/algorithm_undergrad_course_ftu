"""
Problem 08 - Vertex-Disjoint s-t Paths via Node Splitting
==========================================================

Implement `max_vertex_disjoint_paths(vertices, directed_edges, s, t)`: the
maximum number of internally vertex-disjoint directed s->t paths.

Node-splitting reduction: split each internal vertex v into v_in -> v_out with
capacity 1 (this caps how many paths pass THROUGH v). An original edge (u, v)
becomes u_out -> v_in with capacity 1. Keep s and t uncapped. The max flow then
counts paths that share no internal vertex.

Use the `MaxFlow` helper from starter_code.py.

See practical_exercises.pdf, Problem 8, for the full statement and examples.
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
    """Maximum number of internally vertex-disjoint directed s->t paths."""
    # TODO: implement this function using node splitting + MaxFlow.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        V = ["s", "a", "b", "t"]
        E = [("s", "a"), ("a", "t"), ("s", "b"), ("b", "t")]
        assert max_vertex_disjoint_paths(V, E, "s", "t") == 2

        V2 = ["s", "a", "b", "m", "t"]
        E2 = [("s", "a"), ("s", "b"), ("a", "m"), ("b", "m"), ("m", "t")]
        assert max_vertex_disjoint_paths(V2, E2, "s", "t") == 1

        V3 = ["s", "t", "x", "y", "z"]
        E3 = [("s", "x"), ("x", "t"), ("s", "y"), ("y", "t"), ("s", "z"), ("z", "t")]
        assert max_vertex_disjoint_paths(V3, E3, "s", "t") == 3

        assert max_vertex_disjoint_paths(["s", "t", "a"], [("s", "a")], "s", "t") == 0
        assert max_vertex_disjoint_paths(["s", "t"], [("s", "t")], "s", "t") == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
