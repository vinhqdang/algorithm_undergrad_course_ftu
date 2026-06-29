"""
Problem 07 - Maximum Edge-Disjoint s-t Paths
=============================================

Implement `max_edge_disjoint_paths(vertices, directed_edges, s, t)`: the maximum
number of edge-disjoint directed paths from s to t.

By Menger's theorem, this equals the max flow in the network where every edge
has capacity 1. Use the `MaxFlow` helper from starter_code.py (note: parallel
edges add their capacities, which correctly permits multiple disjoint paths).

See practical_exercises.pdf, Problem 7, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import MaxFlow

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def max_edge_disjoint_paths(
    vertices: List[Vertex], directed_edges: List[Edge], s: Vertex, t: Vertex
) -> int:
    """Maximum number of edge-disjoint directed paths from s to t."""
    # TODO: implement this function using MaxFlow.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        V = ["s", "a", "b", "t"]
        E = [("s", "a"), ("a", "t"), ("s", "b"), ("b", "t")]
        assert max_edge_disjoint_paths(V, E, "s", "t") == 2

        V2 = ["s", "a", "b", "t"]
        E2 = [("s", "a"), ("s", "b"), ("a", "m"), ("b", "m"), ("m", "t")]
        assert max_edge_disjoint_paths(V2 + ["m"], E2, "s", "t") == 1

        V3 = ["s", "t", "x", "y", "z"]
        E3 = [("s", "x"), ("x", "t"), ("s", "y"), ("y", "t"), ("s", "z"), ("z", "t")]
        assert max_edge_disjoint_paths(V3, E3, "s", "t") == 3

        assert max_edge_disjoint_paths(["s", "t", "a"], [("s", "a")], "s", "t") == 0

        V4 = ["s", "a", "b", "t"]
        E4 = [("s", "a"), ("s", "b"), ("a", "t"), ("b", "t"), ("a", "b")]
        assert max_edge_disjoint_paths(V4, E4, "s", "t") == 2

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
