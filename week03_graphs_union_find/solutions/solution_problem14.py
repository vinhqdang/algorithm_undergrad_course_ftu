"""
Problem 14 - Cycle Detection in a Directed Graph (DFS with Colors) (SOLUTION)
================================================================================
"""

import os
import sys
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list

WHITE, GRAY, BLACK = 0, 1, 2


def has_cycle_directed(adj: List[List[int]]) -> bool:
    """Return True iff the directed graph contains a directed cycle."""
    n = len(adj)
    color = [WHITE] * n

    def dfs(u: int) -> bool:
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    for start in range(n):
        if color[start] == WHITE:
            if dfs(start):
                return True
    return False


def find_a_directed_cycle(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a directed cycle (list of vertices, first == last), or None if acyclic."""
    n = len(adj)
    color = [WHITE] * n
    stack: List[int] = []

    def dfs(u: int) -> Optional[List[int]]:
        color[u] = GRAY
        stack.append(u)
        for v in adj[u]:
            if color[v] == GRAY:
                idx = stack.index(v)
                return stack[idx:] + [v]
            if color[v] == WHITE:
                result = dfs(v)
                if result is not None:
                    return result
        color[u] = BLACK
        stack.pop()
        return None

    for start in range(n):
        if color[start] == WHITE:
            result = dfs(start)
            if result is not None:
                return result
    return None


if __name__ == "__main__":
    dag = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)], directed=True)
    assert has_cycle_directed(dag) is False
    assert find_a_directed_cycle(dag) is None

    cycle_graph = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    assert has_cycle_directed(cycle_graph) is True
    cyc = find_a_directed_cycle(cycle_graph)
    assert cyc is not None
    assert cyc[0] == cyc[-1]
    for a, b in zip(cyc, cyc[1:]):
        assert b in cycle_graph[a]

    self_loop = edges_to_adjacency_list(2, [(0, 0), (0, 1)], directed=True)
    assert has_cycle_directed(self_loop) is True

    diamond = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    assert has_cycle_directed(diamond) is False

    mixed = [[1], [], [3], [2]]
    assert has_cycle_directed(mixed) is True

    print("All tests passed!")
