"""
Problem 04 - Bellman-Ford with Negative Edges and Negative-Cycle Detection
==========================================================================

Implement the Bellman-Ford single-source shortest-path algorithm. Unlike
Dijkstra, it handles negative edge weights, and it can report when a negative
cycle is present (return ``None`` in that case). See practical_exercises.pdf,
Problem 4.
"""

import os
import sys
from typing import Dict, Hashable, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge, edge_list  # noqa: F401,E402


def bellman_ford(
    graph: Graph, source: Hashable, directed: bool = False
) -> Optional[Dict[Hashable, float]]:
    """Single-source shortest paths via Bellman-Ford.

    Handles negative edge weights. Returns the distance dict, or ``None`` if a
    negative cycle reachable from ``source`` is detected.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g: Graph = {}
        add_edge(g, 0, 1, 4, directed=True)
        add_edge(g, 0, 2, 5, directed=True)
        add_edge(g, 1, 2, -3, directed=True)
        add_edge(g, 2, 3, 2, directed=True)
        g.setdefault(3, {})

        dist = bellman_ford(g, 0, directed=True)
        assert dist is not None
        assert dist[0] == 0.0
        assert dist[1] == 4.0
        assert dist[2] == 1.0
        assert dist[3] == 3.0

        gc: Graph = {}
        add_edge(gc, 0, 1, 1, directed=True)
        add_edge(gc, 1, 2, -2, directed=True)
        add_edge(gc, 2, 1, 1, directed=True)
        assert bellman_ford(gc, 0, directed=True) is None

        g2: Graph = {}
        add_edge(g2, 0, 1, 2, directed=True)
        add_edge(g2, 1, 2, 3, directed=True)
        g2.setdefault(2, {})
        assert bellman_ford(g2, 0, directed=True) == {0: 0.0, 1: 2.0, 2: 5.0}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
