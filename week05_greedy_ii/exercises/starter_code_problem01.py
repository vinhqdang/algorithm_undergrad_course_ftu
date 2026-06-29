"""
Problem 01 - Weighted Graph Builder and Edge Listing
=====================================================

Build an adjacency-dict weighted graph from a list of edges and provide helpers
to inspect its neighbours and list its edges. See practical_exercises.pdf,
Problem 1.

A "weighted graph" is a dict mapping each vertex u to a dict {v: weight}. For
undirected graphs each edge appears in both graph[u] and graph[v].
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, Edge  # noqa: E402


def build_graph(edges: List[Tuple[Hashable, Hashable, float]], directed: bool = False) -> Graph:
    """Build an adjacency-dict graph from a list of ``(u, v, w)`` edges."""
    # TODO: implement this function.
    raise NotImplementedError


def neighbors(graph: Graph, u: Hashable) -> Dict[Hashable, float]:
    """Return the neighbour->weight dict of ``u`` (empty if ``u`` is isolated)."""
    # TODO: implement this function.
    raise NotImplementedError


def list_edges(graph: Graph, directed: bool = False) -> List[Edge]:
    """Return the edges of ``graph`` as ``(u, v, w)`` tuples (each once if undirected)."""
    # TODO: implement this function.
    raise NotImplementedError


def total_weight(graph: Graph, directed: bool = False) -> float:
    """Return the sum of all edge weights in ``graph``."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g = build_graph([(0, 1, 4), (1, 2, 3), (0, 2, 5)])

        assert g[0][1] == 4
        assert g[1][0] == 4
        assert neighbors(g, 1) == {0: 4, 2: 3}

        edges = list_edges(g)
        assert len(edges) == 3
        assert total_weight(g) == 12

        dg = build_graph([(0, 1, 7), (1, 0, 2)], directed=True)
        assert dg[0] == {1: 7}
        assert dg[1] == {0: 2}
        assert len(list_edges(dg, directed=True)) == 2

        g2 = build_graph([(0, 1, 1)])
        assert neighbors(g2, 5) == {}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
