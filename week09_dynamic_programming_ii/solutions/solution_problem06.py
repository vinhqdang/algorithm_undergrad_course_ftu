"""
Problem 06 - Bellman-Ford Shortest-Path Distances (SOLUTION)
=============================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import INF

Edge = Tuple[int, int, float]


def bellman_ford(n: int, edges: List[Edge], source: int) -> List[float]:
    """Return shortest-path distances from `source` (assumes no negative cycle)."""
    dist = [INF] * n
    dist[source] = 0.0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    return dist


if __name__ == "__main__":
    dist = bellman_ford(3, [(0, 1, 4), (0, 2, 5), (1, 2, -3)], 0)
    assert dist == [0, 4, 1]

    # Unreachable vertex stays INF
    dist = bellman_ford(3, [(0, 1, 2)], 0)
    assert dist[0] == 0 and dist[1] == 2 and dist[2] == INF

    # Negative edges along a longer path win
    dist = bellman_ford(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 10)], 0)
    assert dist == [0, 1, 2, 3]

    dist = bellman_ford(5, [(0, 1, 6), (0, 2, 7), (1, 2, 8), (1, 3, 5),
                            (1, 4, -4), (2, 3, -3), (2, 4, 9), (3, 1, -2),
                            (4, 0, 2), (4, 3, 7)], 0)
    assert dist == [0, 2, 7, 4, -2]

    print("All tests passed!")
