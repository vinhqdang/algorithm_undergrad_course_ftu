"""
Problem 07 - Graph Diameter via Repeated BFS
==============================================

The DIAMETER of a connected, unweighted graph is the maximum, over all pairs
of vertices (u, v), of the shortest-path distance between u and v (i.e. the
"longest shortest path").

Implement `eccentricity(adj, v)`, returning the maximum distance from `v` to
any other vertex (using BFS), and `diameter(adj)`, returning the diameter of
the graph by computing `eccentricity(adj, v)` for EVERY vertex `v` and taking
the overall maximum.

Assume `adj` represents a CONNECTED undirected graph (every vertex reachable
from every other). For a graph with a single vertex, the diameter is 0.

This reuses `bfs_distances` from Problem 4 (re-imported from its solution).

See practical_exercises.pdf, Problem 7.
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
    # TODO: implement this function.
    raise NotImplementedError


def diameter(adj: List[List[int]]) -> int:
    """Return the diameter of a connected graph (max eccentricity over all vertices)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Path graph: 0 - 1 - 2 - 3 - 4 (diameter = 4)
        path = edges_to_adjacency_list(5, [(0, 1), (1, 2), (2, 3), (3, 4)])
        assert eccentricity(path, 0) == 4
        assert eccentricity(path, 2) == 2
        assert diameter(path) == 4

        # Star graph: center 0 connected to 1,2,3,4 (diameter = 2, via two leaves)
        star = edges_to_adjacency_list(5, [(0, 1), (0, 2), (0, 3), (0, 4)])
        assert eccentricity(star, 0) == 1
        assert eccentricity(star, 1) == 2
        assert diameter(star) == 2

        # Single vertex
        assert diameter([[]]) == 0

        # Triangle: every pairwise distance is 1
        triangle = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)])
        assert diameter(triangle) == 1

        # Cycle of length 6: diameter = 3
        cycle6 = edges_to_adjacency_list(6, [(i, (i + 1) % 6) for i in range(6)])
        assert diameter(cycle6) == 3

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
