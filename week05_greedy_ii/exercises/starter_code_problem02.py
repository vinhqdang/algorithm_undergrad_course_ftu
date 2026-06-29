"""
Problem 02 - Dijkstra's Shortest-Path Distances
================================================

Implement Dijkstra's algorithm using a binary heap (``heapq``) to compute the
shortest-path distance from a source to every vertex in a non-negatively
weighted graph. See practical_exercises.pdf, Problem 2.
"""

import heapq  # noqa: F401  (you will need this)
import os
import sys
from typing import Dict, Hashable

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge  # noqa: E402


def dijkstra(graph: Graph, source: Hashable) -> Dict[Hashable, float]:
    """Return shortest-path distances from ``source`` to every vertex.

    Uses a binary heap. Assumes all edge weights are non-negative. Unreachable
    vertices get distance ``float('inf')``.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g: Graph = {}
        add_edge(g, 0, 1, 4)
        add_edge(g, 0, 2, 1)
        add_edge(g, 2, 1, 2)
        add_edge(g, 1, 3, 1)
        add_edge(g, 2, 3, 5)

        dist = dijkstra(g, 0)
        assert dist[0] == 0.0
        assert dist[2] == 1.0
        assert dist[1] == 3.0
        assert dist[3] == 4.0

        g2: Graph = {}
        add_edge(g2, 0, 1, 1)
        g2.setdefault(9, {})
        assert dijkstra(g2, 0)[9] == float("inf")

        assert dijkstra({0: {}}, 0) == {0: 0.0}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
