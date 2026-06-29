"""
Problem 10 - Verify the Cut Property
====================================

Cut property: for any cut (S, V\\S), the minimum-weight edge crossing the cut
belongs to some minimum spanning tree. Verify this empirically. See
practical_exercises.pdf, Problem 10.
"""

import os
import sys
from typing import List, Optional, Set

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from starter_code import Graph, Edge, add_edge, edge_list  # noqa: F401,E402

from starter_code_problem07 import kruskal  # noqa: F401,E402


def crossing_edges(graph: Graph, S: Set) -> List[Edge]:
    """Return all edges with exactly one endpoint in ``S``."""
    # TODO: implement this function.
    raise NotImplementedError


def min_crossing_edge(graph: Graph, S: Set) -> Optional[Edge]:
    """Return a minimum-weight edge crossing the cut ``(S, V\\S)`` (or None)."""
    # TODO: implement this function.
    raise NotImplementedError


def cut_property_holds(graph: Graph, S: Set) -> bool:
    """Verify the cut property for the given cut on ``graph``.

    The minimum crossing edge must appear in some MST of the graph.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g: Graph = {}
        add_edge(g, 0, 1, 1)
        add_edge(g, 1, 2, 2)
        add_edge(g, 0, 2, 2)
        add_edge(g, 2, 3, 3)
        add_edge(g, 1, 3, 4)

        e = min_crossing_edge(g, {0})
        assert e[2] == 1.0 and {e[0], e[1]} == {0, 1}
        assert cut_property_holds(g, {0}) is True
        assert cut_property_holds(g, {0, 1}) is True
        assert cut_property_holds(g, {3}) is True
        assert cut_property_holds(g, {0, 2}) is True

        from starter_code import generate_weighted_graph

        for seed in range(20):
            rg = generate_weighted_graph(10, seed=seed, edge_prob=0.4)
            assert cut_property_holds(rg, {0, 1, 2}) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
