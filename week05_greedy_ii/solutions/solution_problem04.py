"""
Problem 04 - Bellman-Ford with Negative Edges and Negative-Cycle Detection (SOLUTION)
=====================================================================================
"""

import os
import sys
from typing import Dict, Hashable, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge, edge_list  # noqa: E402


def bellman_ford(
    graph: Graph, source: Hashable, directed: bool = False
) -> Optional[Dict[Hashable, float]]:
    """Single-source shortest paths via Bellman-Ford.

    Handles negative edge weights. Returns the distance dict, or ``None`` if a
    negative cycle is reachable that affects (i.e. can decrease) some distance.
    For undirected graphs any negative edge is itself a negative cycle.
    """
    dist: Dict[Hashable, float] = {v: float("inf") for v in graph}
    dist[source] = 0.0
    edges = edge_list(graph, directed=directed)

    # For an undirected graph, relax each edge in both directions.
    def relaxations():
        for u, v, w in edges:
            yield u, v, w
            if not directed:
                yield v, u, w

    n = len(graph)
    for _ in range(n - 1):
        changed = False
        for u, v, w in relaxations():
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    # One more pass: any further relaxation means a negative cycle.
    for u, v, w in relaxations():
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return None
    return dist


if __name__ == "__main__":
    # Directed graph with a negative edge but no negative cycle.
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
    assert dist[2] == 1.0  # 0->1->2 = 4 + (-3)
    assert dist[3] == 3.0  # 0->1->2->3

    # Directed negative cycle: 1->2->1 totals -1.
    gc: Graph = {}
    add_edge(gc, 0, 1, 1, directed=True)
    add_edge(gc, 1, 2, -2, directed=True)
    add_edge(gc, 2, 1, 1, directed=True)
    assert bellman_ford(gc, 0, directed=True) is None

    # Non-negative directed graph agrees with the obvious distances.
    g2: Graph = {}
    add_edge(g2, 0, 1, 2, directed=True)
    add_edge(g2, 1, 2, 3, directed=True)
    g2.setdefault(2, {})
    assert bellman_ford(g2, 0, directed=True) == {0: 0.0, 1: 2.0, 2: 5.0}

    print("All tests passed!")
