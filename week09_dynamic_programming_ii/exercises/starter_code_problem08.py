"""
Problem 08 - Floyd-Warshall All-Pairs Shortest Paths
=====================================================

Implement `floyd_warshall(n, edges)` returning an n-by-n matrix `dist` where
dist[i][j] is the shortest-path distance from i to j (INF if no path; 0 on the
diagonal). Assume no negative cycle. Use the classic triple loop over k, i, j.

See practical_exercises.pdf, Problem 8, for the full statement and examples.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import INF

Edge = Tuple[int, int, float]


def floyd_warshall(n: int, edges: List[Edge]) -> List[List[float]]:
    """Return the all-pairs shortest-path distance matrix (assumes no negative cycle)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        dist = floyd_warshall(3, [(0, 1, 4), (0, 2, 5), (1, 2, -3)])
        assert dist[0] == [0, 4, 1]
        assert dist[1] == [INF, 0, -3]
        assert dist[2][2] == 0

        dist = floyd_warshall(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)])
        assert dist[0] == [0, 1, 2, 3]
        assert dist[3] == [INF, INF, INF, 0]

        assert floyd_warshall(1, []) == [[0]]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
