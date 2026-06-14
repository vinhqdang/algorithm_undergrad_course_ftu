"""
Problem 16 - Topological Sort via Kahn's Algorithm (BFS + In-Degree Queue) (SOLUTION)
========================================================================================
"""

import os
import sys
from collections import deque
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def in_degrees(adj: List[List[int]]) -> List[int]:
    """Return the in-degree of every vertex."""
    indeg = [0] * len(adj)
    for u in range(len(adj)):
        for v in adj[u]:
            indeg[v] += 1
    return indeg


def topological_sort_kahn(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a topological order via Kahn's algorithm, or None if `adj` has a cycle."""
    n = len(adj)
    indeg = in_degrees(adj)
    queue = deque(v for v in range(n) if indeg[v] == 0)
    order: List[int] = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)

    if len(order) != n:
        return None
    return order


if __name__ == "__main__":
    dag = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    assert in_degrees(dag) == [0, 1, 1, 2]

    order = topological_sort_kahn(dag)
    assert order is not None
    assert order == [0, 1, 2, 3]

    cyclic = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    assert topological_sort_kahn(cyclic) is None
    assert in_degrees(cyclic) == [1, 1, 1]

    chain = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
    assert topological_sort_kahn(chain) == [0, 1, 2, 3]

    independent = edges_to_adjacency_list(4, [(0, 1), (2, 3)], directed=True)
    assert topological_sort_kahn(independent) == [0, 2, 1, 3]

    print("All tests passed!")
