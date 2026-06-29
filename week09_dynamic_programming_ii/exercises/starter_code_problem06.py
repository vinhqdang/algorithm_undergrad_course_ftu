"""
Problem 06 - Bellman-Ford Shortest-Path Distances
==================================================

Implement `bellman_ford(n, edges, source)` returning a list `dist` of length `n`,
where dist[v] is the shortest-path distance from `source` to `v` (use INF for
unreachable vertices). The graph (n, edges) may have negative edge weights but is
assumed to have no negative cycle reachable from the source. Relax all edges
n - 1 times.

See practical_exercises.pdf, Problem 6, for the full statement and examples.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import INF

Edge = Tuple[int, int, float]


def bellman_ford(n: int, edges: List[Edge], source: int) -> List[float]:
    """Return shortest-path distances from `source` (assumes no negative cycle)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        dist = bellman_ford(3, [(0, 1, 4), (0, 2, 5), (1, 2, -3)], 0)
        assert dist == [0, 4, 1]

        dist = bellman_ford(3, [(0, 1, 2)], 0)
        assert dist[0] == 0 and dist[1] == 2 and dist[2] == INF

        dist = bellman_ford(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 10)], 0)
        assert dist == [0, 1, 2, 3]

        dist = bellman_ford(5, [(0, 1, 6), (0, 2, 7), (1, 2, 8), (1, 3, 5),
                                (1, 4, -4), (2, 3, -3), (2, 4, 9), (3, 1, -2),
                                (4, 0, 2), (4, 3, 7)], 0)
        assert dist == [0, 2, 7, 4, -2]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
