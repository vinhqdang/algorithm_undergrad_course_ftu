"""
Problem 17 - Counting Topological Orderings & Uniqueness (SOLUTION)
=======================================================================
"""

import os
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def count_topological_orders(adj: List[List[int]]) -> int:
    """Return the total number of distinct topological orderings of `adj`."""
    n = len(adj)
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1

    placed = [False] * n

    def backtrack() -> int:
        available = [v for v in range(n) if not placed[v] and indeg[v] == 0]
        if not available:
            return 1 if all(placed) else 0

        total = 0
        for v in available:
            placed[v] = True
            for w in adj[v]:
                indeg[w] -= 1
            total += backtrack()
            for w in adj[v]:
                indeg[w] += 1
            placed[v] = False

        return total

    return backtrack()


def has_unique_topological_order(adj: List[List[int]]) -> bool:
    """Return True iff `adj` has exactly one topological ordering."""
    return count_topological_orders(adj) == 1


if __name__ == "__main__":
    chain = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
    assert count_topological_orders(chain) == 1
    assert has_unique_topological_order(chain) is True

    empty = [[], [], []]
    assert count_topological_orders(empty) == 6
    assert has_unique_topological_order(empty) is False

    diamond = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    assert count_topological_orders(diamond) == 2
    assert has_unique_topological_order(diamond) is False

    independent = edges_to_adjacency_list(4, [(0, 1), (2, 3)], directed=True)
    assert count_topological_orders(independent) == 6

    cyclic = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    assert count_topological_orders(cyclic) == 0
    assert has_unique_topological_order(cyclic) is False

    print("All tests passed!")
