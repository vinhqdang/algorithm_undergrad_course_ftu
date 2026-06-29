"""
Problem 06 - Counter-Example: Dijkstra Fails on a Negative Edge (SOLUTION)
==========================================================================
"""

import os
import sys
from typing import Dict, Hashable, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge  # noqa: E402

from solution_problem02 import dijkstra  # noqa: E402
from solution_problem04 import bellman_ford  # noqa: E402


def negative_edge_graph() -> Graph:
    """A small directed graph with one negative edge and no negative cycle.

    Vertices 0 (source), 1, 2. Edges: 0->1 (2), 0->2 (3), 2->1 (-2). The true
    shortest distance to 1 is 0->2->1 = 3 + (-2) = 1. But Dijkstra pops and
    *finalizes* vertex 1 at distance 2 (its cheapest tentative value so far)
    before it ever pops vertex 2 (tentative distance 3) and relaxes the negative
    edge 2->1. Once vertex 1 is finalized Dijkstra never revisits it, so it
    reports 2 for vertex 1 instead of the correct 1.
    """
    g: Graph = {}
    add_edge(g, 0, 1, 2, directed=True)
    add_edge(g, 0, 2, 3, directed=True)
    add_edge(g, 2, 1, -2, directed=True)
    g.setdefault(1, {})
    return g


def dijkstra_vs_bellman_ford() -> Tuple[Dict[Hashable, float], Dict[Hashable, float]]:
    """Return ``(dijkstra_dist, bellman_ford_dist)`` for the counter-example.

    The two distance dicts differ at vertex 2, demonstrating that Dijkstra is
    incorrect in the presence of negative edges.
    """
    g = negative_edge_graph()
    d_dij = dijkstra(g, 0)
    d_bf = bellman_ford(g, 0, directed=True)
    assert d_bf is not None
    return d_dij, d_bf


if __name__ == "__main__":
    d_dij, d_bf = dijkstra_vs_bellman_ford()

    # Bellman-Ford finds the correct distance to vertex 1 (via 0->2->1 = 1).
    assert d_bf[1] == 1.0
    # Dijkstra is wrong: it finalizes vertex 1 at the direct edge weight 2.
    assert d_dij[1] == 2.0
    # They genuinely disagree, which is the point of the counter-example.
    assert d_dij[1] != d_bf[1]

    print("All tests passed!")
