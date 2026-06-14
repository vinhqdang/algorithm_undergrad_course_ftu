"""
Problem 11 - Cycle Detection in an Undirected Graph (DFS) (SOLUTION)
=======================================================================
"""

import os
import sys
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def has_cycle_undirected(adj: List[List[int]]) -> bool:
    """Return True iff the undirected graph contains a cycle."""
    n = len(adj)
    visited = [False] * n

    def dfs(u: int, parent: int) -> bool:
        visited[u] = True
        skipped_parent = False
        for v in adj[u]:
            if v == parent and not skipped_parent:
                # Skip exactly one occurrence of the edge back to the parent
                # (handles the case where adj[u] contains parent only once).
                skipped_parent = True
                continue
            if visited[v]:
                return True
            if dfs(v, u):
                return True
        return False

    for start in range(n):
        if not visited[start]:
            if dfs(start, -1):
                return True
    return False


def find_a_cycle(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a list of vertices forming a cycle (first == last), or None if acyclic."""
    n = len(adj)
    visited = [False] * n

    def dfs(u: int, parent: int, path: List[int]) -> Optional[List[int]]:
        visited[u] = True
        path.append(u)
        skipped_parent = False
        for v in adj[u]:
            if v == parent and not skipped_parent:
                skipped_parent = True
                continue
            if visited[v]:
                # Found a back edge to v: extract the cycle from path.
                idx = path.index(v)
                return path[idx:] + [v]
            result = dfs(v, u, path)
            if result is not None:
                return result
        path.pop()
        return None

    for start in range(n):
        if not visited[start]:
            result = dfs(start, -1, [])
            if result is not None:
                return result
    return None


if __name__ == "__main__":
    tree = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3)])
    assert has_cycle_undirected(tree) is False
    assert find_a_cycle(tree) is None

    triangle = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)])
    assert has_cycle_undirected(triangle) is True
    cycle = find_a_cycle(triangle)
    assert cycle is not None
    assert cycle[0] == cycle[-1]
    assert len(set(cycle[:-1])) == 3

    mixed = edges_to_adjacency_list(5, [(0, 1), (2, 3), (3, 4), (2, 4)])
    assert has_cycle_undirected(mixed) is True

    forest = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
    assert has_cycle_undirected(forest) is False

    single_edge = edges_to_adjacency_list(2, [(0, 1)])
    assert has_cycle_undirected(single_edge) is False

    print("All tests passed!")
