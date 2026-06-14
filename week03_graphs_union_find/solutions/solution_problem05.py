"""
Problem 05 - Shortest Path Reconstruction via BFS (SOLUTION)
==============================================================
"""

import os
import sys
from collections import deque
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def bfs_shortest_path(adj: List[List[int]], source: int, target: int) -> Optional[List[int]]:
    """Return a shortest path (list of vertices) from source to target, or None."""
    if source == target:
        return [source]

    n = len(adj)
    visited = [False] * n
    visited[source] = True
    parent = {source: None}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                if v == target:
                    queue.clear()
                    break
                queue.append(v)

    if not visited[target]:
        return None

    path = [target]
    while path[-1] != source:
        path.append(parent[path[-1]])
    path.reverse()
    return path


if __name__ == "__main__":
    adj = [[1], [0, 2], [1, 3], [2, 4], [3]]
    assert bfs_shortest_path(adj, 0, 4) == [0, 1, 2, 3, 4]
    assert bfs_shortest_path(adj, 2, 2) == [2]
    assert bfs_shortest_path(adj, 4, 0) == [4, 3, 2, 1, 0]

    disconnected = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
    assert bfs_shortest_path(disconnected, 0, 3) is None

    diamond = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    path = bfs_shortest_path(diamond, 0, 3)
    assert path is not None
    assert len(path) == 3
    assert path[0] == 0 and path[-1] == 3
    for a, b in zip(path, path[1:]):
        assert b in diamond[a]

    print("All tests passed!")
