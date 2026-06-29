"""
Problem 08 - Floyd-Warshall All-Pairs Shortest Paths (SOLUTION)
================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import INF

Edge = Tuple[int, int, float]


def floyd_warshall(n: int, edges: List[Edge]) -> List[List[float]]:
    """Return the all-pairs shortest-path distance matrix (assumes no negative cycle)."""
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0.0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    return dist


if __name__ == "__main__":
    dist = floyd_warshall(3, [(0, 1, 4), (0, 2, 5), (1, 2, -3)])
    assert dist[0] == [0, 4, 1]
    assert dist[1] == [INF, 0, -3]
    assert dist[2][2] == 0

    # Path graph 0->1->2->3
    dist = floyd_warshall(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)])
    assert dist[0] == [0, 1, 2, 3]
    assert dist[3] == [INF, INF, INF, 0]

    # Single vertex
    assert floyd_warshall(1, []) == [[0]]

    print("All tests passed!")
