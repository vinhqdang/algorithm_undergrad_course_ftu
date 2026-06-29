"""
Problem 02 - Dijkstra's Shortest-Path Distances (SOLUTION)
===========================================================
"""

import heapq
import os
import sys
from typing import Dict, Hashable

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge  # noqa: E402


def dijkstra(graph: Graph, source: Hashable) -> Dict[Hashable, float]:
    """Return shortest-path distances from ``source`` to every vertex.

    Uses a binary heap (``heapq``). Assumes all edge weights are non-negative.
    Unreachable vertices get distance ``float('inf')``.
    """
    dist: Dict[Hashable, float] = {v: float("inf") for v in graph}
    dist[source] = 0.0
    heap = [(0.0, source)]
    visited = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u].items():
            if v in visited:
                continue  # a finalized vertex is never updated again
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


if __name__ == "__main__":
    g: Graph = {}
    add_edge(g, 0, 1, 4)
    add_edge(g, 0, 2, 1)
    add_edge(g, 2, 1, 2)
    add_edge(g, 1, 3, 1)
    add_edge(g, 2, 3, 5)

    dist = dijkstra(g, 0)
    # 0->2 (1), 2->1 (2) => dist[1] = 3 (better than direct 0->1 = 4)
    assert dist[0] == 0.0
    assert dist[2] == 1.0
    assert dist[1] == 3.0
    assert dist[3] == 4.0  # 0->2->1->3 = 1+2+1

    # Unreachable vertex.
    g2: Graph = {}
    add_edge(g2, 0, 1, 1)
    g2.setdefault(9, {})
    assert dijkstra(g2, 0)[9] == float("inf")

    # Single vertex.
    assert dijkstra({0: {}}, 0) == {0: 0.0}

    print("All tests passed!")
