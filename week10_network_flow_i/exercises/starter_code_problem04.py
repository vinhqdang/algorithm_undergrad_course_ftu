"""
Problem 04 - BFS for an Augmenting Path in the Residual Graph
==============================================================

Implement a breadth-first search that finds a SHORTEST (fewest-edges)
augmenting path in the residual graph of a flow network.

Use the current edge flows stored in `network` to determine residual
capacities (an edge of the adjacency lists is usable iff its
``residual_capacity()`` is positive). Return the path as a list of nodes
``[s, ..., t]``, or ``None`` if the sink is unreachable in the residual graph
(meaning the current flow is already maximum). If source == sink, return
``[s]``.

See practical_exercises.pdf, Problem 4, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable


def bfs_augmenting_path(network: FlowNetwork) -> Optional[List[Node]]:
    """Find a shortest augmenting path in the residual graph, or None."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        G = FlowNetwork(source="s", sink="t")
        G.add_edge("s", "a", 3)
        G.add_edge("a", "t", 3)
        assert bfs_augmenting_path(G) == ["s", "a", "t"]

        G2 = FlowNetwork(source="s", sink="t")
        G2.add_edge("s", "a", 1)
        G2.add_edge("a", "t", 1)
        G2.add_edge("s", "b", 1)
        G2.add_edge("b", "c", 1)
        G2.add_edge("c", "t", 1)
        assert bfs_augmenting_path(G2) == ["s", "a", "t"]

        edge_sa = next(e for e in G.adj["s"] if e.v == "a" and e.capacity > 0)
        edge_at = next(e for e in G.adj["a"] if e.v == "t" and e.capacity > 0)
        edge_sa.push(3)
        edge_at.push(3)
        assert bfs_augmenting_path(G) is None

        G3 = FlowNetwork(source="x", sink="x")
        G3.add_node("x")
        assert bfs_augmenting_path(G3) == ["x"]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
