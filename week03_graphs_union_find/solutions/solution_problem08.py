"""
Problem 08 - Recursive DFS Traversal and Discovery/Finish Times (SOLUTION)
=============================================================================
"""

import os
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def dfs_recursive(adj: List[List[int]], source: int) -> List[int]:
    """Return the DFS preorder (discovery order) starting at source."""
    visited = [False] * len(adj)
    order: List[int] = []

    def visit(u: int) -> None:
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visit(v)

    visit(source)
    return order


def dfs_discovery_finish_times(adj: List[List[int]], source: int) -> Tuple[Dict[int, int], Dict[int, int]]:
    """Return (discovery, finish) timestamp dicts for vertices reachable from source."""
    visited = [False] * len(adj)
    discovery: Dict[int, int] = {}
    finish: Dict[int, int] = {}
    clock = [0]

    def visit(u: int) -> None:
        visited[u] = True
        discovery[u] = clock[0]
        clock[0] += 1
        for v in adj[u]:
            if not visited[v]:
                visit(v)
        finish[u] = clock[0]
        clock[0] += 1

    visit(source)
    return discovery, finish


if __name__ == "__main__":
    path = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)])
    assert dfs_recursive(path, 0) == [0, 1, 2, 3]

    disc, fin = dfs_discovery_finish_times(path, 0)
    for v in range(4):
        assert disc[v] < fin[v]
    assert disc[0] == min(disc.values())
    assert fin[0] == max(fin.values())
    all_times = sorted(list(disc.values()) + list(fin.values()))
    assert all_times == list(range(8))

    tree = [[1, 2], [3], [], []]
    assert dfs_recursive(tree, 0) == [0, 1, 3, 2]

    disconnected = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
    order = dfs_recursive(disconnected, 0)
    assert set(order) == {0, 1}

    print("All tests passed!")
