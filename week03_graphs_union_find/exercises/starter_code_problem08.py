"""
Problem 08 - Recursive DFS Traversal and Discovery/Finish Times
=================================================================

Implement `dfs_recursive(adj, source)`, which performs a recursive
Depth-First Search starting from `source` on a graph given as an adjacency
list (directed or undirected) and returns the list of vertices in the order
they are FIRST VISITED (discovered), i.e. the DFS preorder.

Visit neighbors of a vertex `u` in the order they appear in `adj[u]`.

Also implement `dfs_discovery_finish_times(adj, source)`, returning a pair
of dicts `(discovery, finish)` mapping each REACHABLE vertex to an integer
"timestamp": start a counter at 0, increment it each time you discover a
vertex (record in `discovery`) or finish processing a vertex (record in
`finish`, i.e. when the recursive call for that vertex returns). This is the
classic discovery/finish-time bookkeeping used to classify edges in DFS
(tree, back, forward, cross edges).

See practical_exercises.pdf, Problem 8.
"""

import os
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def dfs_recursive(adj: List[List[int]], source: int) -> List[int]:
    """Return the DFS preorder (discovery order) starting at source."""
    # TODO: implement this function.
    raise NotImplementedError


def dfs_discovery_finish_times(adj: List[List[int]], source: int) -> Tuple[Dict[int, int], Dict[int, int]]:
    """Return (discovery, finish) timestamp dicts for vertices reachable from source."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Path graph: 0 - 1 - 2 - 3
        path = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)])
        assert dfs_recursive(path, 0) == [0, 1, 2, 3]

        disc, fin = dfs_discovery_finish_times(path, 0)
        # Each vertex's discovery time is strictly less than its finish time.
        for v in range(4):
            assert disc[v] < fin[v]
        # Vertex 0 (the root) is discovered first and finishes last.
        assert disc[0] == min(disc.values())
        assert fin[0] == max(fin.values())
        # All 8 timestamps (4 discovery + 4 finish) are distinct, in 0..7.
        all_times = sorted(list(disc.values()) + list(fin.values()))
        assert all_times == list(range(8))

        # Tree: 0 -> [1, 2], 1 -> [3], 2 -> [], 3 -> []  (directed)
        tree = [[1, 2], [3], [], []]
        assert dfs_recursive(tree, 0) == [0, 1, 3, 2]

        # Disconnected: DFS from 0 should not visit vertex 2 (separate component)
        disconnected = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
        order = dfs_recursive(disconnected, 0)
        assert set(order) == {0, 1}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
