"""
Problem 07 - Maximum Edge-Disjoint s-t Paths (SOLUTION)
========================================================
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
    """Maximum number of edge-disjoint directed paths from s to t.

    Menger's theorem: this equals the max flow in the network where every edge
    has capacity 1. (Parallel edges between the same pair add their capacities,
    correctly allowing multiple disjoint paths along a multi-edge.)
    """
    mf = MaxFlow()
    for u, v in directed_edges:
        mf.add_edge(u, v, 1)
    return int(round(mf.max_flow(s, t)))


if __name__ == "__main__":
    # Two parallel disjoint paths s->a->t and s->b->t.
    V = ["s", "a", "b", "t"]
    E = [("s", "a"), ("a", "t"), ("s", "b"), ("b", "t")]
    assert max_edge_disjoint_paths(V, E, "s", "t") == 2

    # A single bottleneck edge limits to 1 path.
    V2 = ["s", "a", "b", "t"]
    E2 = [("s", "a"), ("s", "b"), ("a", "m"), ("b", "m"), ("m", "t")]
    assert max_edge_disjoint_paths(V2 + ["m"], E2, "s", "t") == 1

    # Three independent direct edges via parallel structure.
    V3 = ["s", "t", "x", "y", "z"]
    E3 = [("s", "x"), ("x", "t"), ("s", "y"), ("y", "t"), ("s", "z"), ("z", "t")]
    assert max_edge_disjoint_paths(V3, E3, "s", "t") == 3

    # No path -> 0.
    assert max_edge_disjoint_paths(["s", "t", "a"], [("s", "a")], "s", "t") == 0

    # Diamond graph s -> a,b -> t with cross edges; min cut around t is 2.
    V4 = ["s", "a", "b", "t"]
    E4 = [("s", "a"), ("s", "b"), ("a", "t"), ("b", "t"), ("a", "b")]
    assert max_edge_disjoint_paths(V4, E4, "s", "t") == 2

    print("All tests passed!")
