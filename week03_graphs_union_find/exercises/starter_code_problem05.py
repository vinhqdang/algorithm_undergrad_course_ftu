"""
Problem 05 - Shortest Path Reconstruction via BFS
===================================================

Implement `bfs_shortest_path(adj, source, target)`, which returns the actual
sequence of vertices on a SHORTEST path from `source` to `target` (an
unweighted graph, given as an adjacency list), as a list
`[source, ..., target]`.

If `target` is unreachable from `source`, return `None`. If `source ==
target`, return `[source]`.

Hint: run BFS while recording, for each vertex `v`, the vertex `parent[v]`
from which `v` was first discovered (i.e. a "BFS tree"). Then walk
`parent` pointers backward from `target` to `source` and reverse.

See practical_exercises.pdf, Problem 5.
"""

import os
import sys
from collections import deque
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def bfs_shortest_path(adj: List[List[int]], source: int, target: int) -> Optional[List[int]]:
    """Return a shortest path (list of vertices) from source to target, or None."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Path graph: 0 - 1 - 2 - 3 - 4
        adj = [[1], [0, 2], [1, 3], [2, 4], [3]]
        assert bfs_shortest_path(adj, 0, 4) == [0, 1, 2, 3, 4]
        assert bfs_shortest_path(adj, 2, 2) == [2]
        assert bfs_shortest_path(adj, 4, 0) == [4, 3, 2, 1, 0]

        # Disconnected graph
        disconnected = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
        assert bfs_shortest_path(disconnected, 0, 3) is None

        # Grid-like graph with multiple shortest paths: 0-1-3 and 0-2-3
        # should both have length 2; the result must be a valid path of
        # length 2 (either is acceptable).
        diamond = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
        path = bfs_shortest_path(diamond, 0, 3)
        assert path is not None
        assert len(path) == 3
        assert path[0] == 0 and path[-1] == 3
        # consecutive vertices must be connected
        for a, b in zip(path, path[1:]):
            assert b in diamond[a]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
