"""
Problem 15 - Topological Sort via DFS (SOLUTION)
===================================================
"""

import os
import sys
from typing import List, Optional

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem14 import has_cycle_directed
from starter_code import edges_to_adjacency_list

WHITE, GRAY, BLACK = 0, 1, 2


def topological_sort_dfs(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a topological order of the DAG `adj`, or None if it has a cycle."""
    if has_cycle_directed(adj):
        return None

    n = len(adj)
    color = [WHITE] * n
    order: List[int] = []

    def dfs(u: int) -> None:
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == WHITE:
                dfs(v)
        color[u] = BLACK
        order.append(u)

    for start in range(n):
        if color[start] == WHITE:
            dfs(start)

    order.reverse()
    return order


def verify_topological_order(adj: List[List[int]], order: List[int]) -> bool:
    """Return True iff `order` is a valid topological order of `adj`."""
    n = len(adj)
    if sorted(order) != list(range(n)):
        return False
    position = {v: i for i, v in enumerate(order)}
    for u in range(n):
        for v in adj[u]:
            if position[u] >= position[v]:
                return False
    return True


if __name__ == "__main__":
    dag = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    order = topological_sort_dfs(dag)
    assert order is not None
    assert sorted(order) == [0, 1, 2, 3]
    assert verify_topological_order(dag, order) is True

    assert order.index(0) < order.index(1)
    assert order.index(0) < order.index(2)
    assert order.index(3) > order.index(1)
    assert order.index(3) > order.index(2)

    cyclic = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    assert topological_sort_dfs(cyclic) is None
    assert has_cycle_directed(cyclic) is True

    chain = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
    assert topological_sort_dfs(chain) == [0, 1, 2, 3]

    assert verify_topological_order(chain, [3, 2, 1, 0]) is False
    assert verify_topological_order(chain, [0, 1, 2, 3]) is True

    print("All tests passed!")
