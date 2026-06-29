"""
Problem 01 - Weighted Graph Builder and Edge Listing (SOLUTION)
================================================================
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, Edge, add_edge, edge_list  # noqa: E402


def build_graph(edges: List[Tuple[Hashable, Hashable, float]], directed: bool = False) -> Graph:
    """Build an adjacency-dict graph from a list of ``(u, v, w)`` edges."""
    graph: Graph = {}
    for u, v, w in edges:
        add_edge(graph, u, v, w, directed=directed)
    return graph


def neighbors(graph: Graph, u: Hashable) -> Dict[Hashable, float]:
    """Return the neighbour->weight dict of ``u`` (empty if ``u`` is isolated)."""
    return dict(graph.get(u, {}))


def list_edges(graph: Graph, directed: bool = False) -> List[Edge]:
    """Return the edges of ``graph`` as ``(u, v, w)`` tuples (each once if undirected)."""
    return edge_list(graph, directed=directed)


def total_weight(graph: Graph, directed: bool = False) -> float:
    """Return the sum of all edge weights in ``graph``."""
    return sum(w for _, _, w in list_edges(graph, directed=directed))


if __name__ == "__main__":
    g = build_graph([(0, 1, 4), (1, 2, 3), (0, 2, 5)])

    # Undirected: edge appears in both directions in the adjacency dict.
    assert g[0][1] == 4
    assert g[1][0] == 4
    assert neighbors(g, 1) == {0: 4, 2: 3}

    # Each undirected edge listed exactly once.
    edges = list_edges(g)
    assert len(edges) == 3
    assert total_weight(g) == 12

    # Directed graph keeps direction.
    dg = build_graph([(0, 1, 7), (1, 0, 2)], directed=True)
    assert dg[0] == {1: 7}
    assert dg[1] == {0: 2}
    assert len(list_edges(dg, directed=True)) == 2

    # Isolated vertex has no neighbours.
    g2 = build_graph([(0, 1, 1)])
    assert neighbors(g2, 5) == {}

    print("All tests passed!")
