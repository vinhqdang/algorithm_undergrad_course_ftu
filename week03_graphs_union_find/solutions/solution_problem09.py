"""
Problem 09 - Iterative DFS with an Explicit Stack (SOLUTION)
===============================================================
"""

import os
import sys
from typing import List

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem08 import dfs_recursive
from starter_code import edges_to_adjacency_list


def dfs_iterative(adj: List[List[int]], source: int) -> List[int]:
    """Return the DFS preorder (discovery order), computed iteratively."""
    visited = [False] * len(adj)
    order: List[int] = []
    stack = [source]

    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        for v in reversed(adj[u]):
            if not visited[v]:
                stack.append(v)

    return order


def max_stack_size(adj: List[List[int]], source: int) -> int:
    """Return the maximum size reached by the explicit stack during dfs_iterative."""
    visited = [False] * len(adj)
    stack = [source]
    max_size = len(stack)

    while stack:
        u = stack.pop()
        if visited[u]:
            max_size = max(max_size, len(stack))
            continue
        visited[u] = True
        for v in reversed(adj[u]):
            if not visited[v]:
                stack.append(v)
        max_size = max(max_size, len(stack))

    return max_size


if __name__ == "__main__":
    path = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)])
    assert dfs_iterative(path, 0) == dfs_recursive(path, 0) == [0, 1, 2, 3]

    tree = [[1, 2], [3], [], []]
    assert dfs_iterative(tree, 0) == dfs_recursive(tree, 0) == [0, 1, 3, 2]

    star = [[1, 2, 3], [0], [0], [0]]
    assert dfs_iterative(star, 0) == dfs_recursive(star, 0)

    long_path = edges_to_adjacency_list(6, [(i, i + 1) for i in range(5)])
    assert max_stack_size(long_path, 0) <= 3

    disconnected = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
    assert set(dfs_iterative(disconnected, 0)) == {0, 1}

    print("All tests passed!")
