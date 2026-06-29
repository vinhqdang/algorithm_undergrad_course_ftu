"""
Problem 11 - Edge-Disjoint Paths via Unit-Capacity Max Flow (Menger)
=====================================================================

Implement ``max_edge_disjoint_paths(nodes, directed_edges, s, t)``: the maximum
number of pairwise edge-disjoint s-t paths in a directed graph.

By Menger's theorem (the edge form), this equals the max s-t flow when EVERY
edge is given capacity 1: with unit capacities and integral flow, each unit of
flow traces one edge-disjoint path. Return the count.

See practical_exercises.pdf, Problem 11, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

# from starter_code_problem05 import edmonds_karp

Node = Hashable


def max_edge_disjoint_paths(
    nodes: List[Node], directed_edges: List[Tuple[Node, Node]], s: Node, t: Node
) -> int:
    """Maximum number of edge-disjoint s-t paths via unit-capacity max flow."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        nodes = ["s", "a", "b", "t"]
        edges = [("s", "a"), ("a", "t"), ("s", "b"), ("b", "t")]
        assert max_edge_disjoint_paths(nodes, edges, "s", "t") == 2

        nodes2 = ["s", "a", "b", "t"]
        edges2 = [("s", "a"), ("a", "b"), ("b", "t")]
        assert max_edge_disjoint_paths(nodes2, edges2, "s", "t") == 1

        nodes4 = ["s", "a", "b", "c", "t"]
        edges4 = [("s", "a"), ("a", "t"), ("s", "b"), ("b", "t"), ("s", "c"), ("c", "t")]
        assert max_edge_disjoint_paths(nodes4, edges4, "s", "t") == 3

        nodes5 = ["s", "a", "t"]
        edges5 = [("s", "a")]
        assert max_edge_disjoint_paths(nodes5, edges5, "s", "t") == 0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
