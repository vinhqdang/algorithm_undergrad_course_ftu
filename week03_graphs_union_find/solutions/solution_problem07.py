"""
Problem 07 - Graph Diameter via Repeated BFS (SOLUTION)
==========================================================
"""

import os
import sys
from typing import List

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem04 import bfs_distances
from starter_code import edges_to_adjacency_list


def eccentricity(adj: List[List[int]], v: int) -> int:
    """Return the maximum shortest-path distance from v to any other vertex."""
    return max(bfs_distances(adj, v))


def diameter(adj: List[List[int]]) -> int:
    """Return the diameter of a connected graph (max eccentricity over all vertices)."""
    return max(eccentricity(adj, v) for v in range(len(adj)))


if __name__ == "__main__":
    path = edges_to_adjacency_list(5, [(0, 1), (1, 2), (2, 3), (3, 4)])
    assert eccentricity(path, 0) == 4
    assert eccentricity(path, 2) == 2
    assert diameter(path) == 4

    star = edges_to_adjacency_list(5, [(0, 1), (0, 2), (0, 3), (0, 4)])
    assert eccentricity(star, 0) == 1
    assert eccentricity(star, 1) == 2
    assert diameter(star) == 2

    assert diameter([[]]) == 0

    triangle = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)])
    assert diameter(triangle) == 1

    cycle6 = edges_to_adjacency_list(6, [(i, (i + 1) % 6) for i in range(6)])
    assert diameter(cycle6) == 3

    print("All tests passed!")
