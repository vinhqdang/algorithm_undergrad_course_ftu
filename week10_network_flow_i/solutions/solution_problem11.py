"""
Problem 11 - Edge-Disjoint Paths via Unit-Capacity Max Flow (Menger) (SOLUTION)
================================================================================
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem05 import edmonds_karp
from starter_code import FlowNetwork

Node = Hashable


def max_edge_disjoint_paths(
    nodes: List[Node], directed_edges: List[Tuple[Node, Node]], s: Node, t: Node
) -> int:
    """Maximum number of edge-disjoint s-t paths in a directed graph.

    Menger's theorem (the edge-connectivity / max-flow special case): assign
    capacity 1 to every edge; then the maximum number of pairwise edge-disjoint
    s-t paths equals the maximum s-t flow. With unit capacities and integral
    flow, each unit of flow corresponds to one edge-disjoint path. Returns the
    count.
    """
    g = FlowNetwork(source=s, sink=t)
    for u in nodes:
        g.add_node(u)
    for (u, v) in directed_edges:
        g.add_edge(u, v, 1)
    return int(edmonds_karp(g))


if __name__ == "__main__":
    # Two parallel disjoint paths s->a->t and s->b->t.
    nodes = ["s", "a", "b", "t"]
    edges = [("s", "a"), ("a", "t"), ("s", "b"), ("b", "t")]
    assert max_edge_disjoint_paths(nodes, edges, "s", "t") == 2

    # A shared middle edge limits the number of edge-disjoint paths to 1.
    nodes2 = ["s", "a", "b", "t"]
    edges2 = [("s", "a"), ("a", "b"), ("b", "t")]
    assert max_edge_disjoint_paths(nodes2, edges2, "s", "t") == 1

    # Two paths that share a vertex but no edge: still 2 edge-disjoint paths.
    # s->m->t via two distinct edge sets requires distinct edges; build a "bowtie".
    nodes3 = ["s", "x", "y", "t"]
    edges3 = [("s", "x"), ("x", "t"), ("s", "y"), ("y", "t")]
    assert max_edge_disjoint_paths(nodes3, edges3, "s", "t") == 2

    # Three disjoint paths.
    nodes4 = ["s", "a", "b", "c", "t"]
    edges4 = [
        ("s", "a"), ("a", "t"),
        ("s", "b"), ("b", "t"),
        ("s", "c"), ("c", "t"),
    ]
    assert max_edge_disjoint_paths(nodes4, edges4, "s", "t") == 3

    # No path at all.
    nodes5 = ["s", "a", "t"]
    edges5 = [("s", "a")]
    assert max_edge_disjoint_paths(nodes5, edges5, "s", "t") == 0

    print("All tests passed!")
