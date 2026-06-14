"""
Problem 13 - Finding an Odd Cycle (Certificate of Non-Bipartiteness) (SOLUTION)
==================================================================================
"""

import os
import sys
from collections import deque
from typing import List, Optional

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem12 import is_bipartite
from starter_code import edges_to_adjacency_list


def _path_to_root(parent: List[int], v: int) -> List[int]:
    path = [v]
    while parent[path[-1]] != -1:
        path.append(parent[path[-1]])
    return path


def find_odd_cycle(adj: List[List[int]]) -> Optional[List[int]]:
    """Return an odd-length cycle (list of vertices, first == last) if the
    graph is not bipartite, else None."""
    n = len(adj)
    color = [-1] * n
    parent = [-1] * n
    dist = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif color[v] == color[u] and v != parent[u]:
                    # Same-color edge (u, v): found an odd cycle.
                    path_u = _path_to_root(parent, u)
                    path_v = _path_to_root(parent, v)
                    set_v = set(path_v)
                    # Find the lowest common ancestor.
                    lca_index_u = next(i for i, x in enumerate(path_u) if x in set_v)
                    lca = path_u[lca_index_u]
                    lca_index_v = path_v.index(lca)
                    up = path_u[:lca_index_u + 1]            # u ... lca
                    down = list(reversed(path_v[:lca_index_v]))  # ... -> v (excluding lca)
                    # Close the cycle: u -> ... -> lca -> ... -> v -> u (edge u-v)
                    cycle = up + down + [u]
                    return cycle

    return None


if __name__ == "__main__":
    c3 = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)])
    cycle = find_odd_cycle(c3)
    assert cycle is not None
    assert cycle[0] == cycle[-1]
    assert (len(cycle) - 1) % 2 == 1
    for a, b in zip(cycle, cycle[1:]):
        assert b in c3[a]

    c4 = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3), (0, 3)])
    assert find_odd_cycle(c4) is None
    assert is_bipartite(c4) is True

    c5 = edges_to_adjacency_list(5, [(i, (i + 1) % 5) for i in range(5)])
    cycle5 = find_odd_cycle(c5)
    assert cycle5 is not None
    assert (len(cycle5) - 1) % 2 == 1
    assert (len(cycle5) - 1) == 5

    tree = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3)])
    assert find_odd_cycle(tree) is None

    print("All tests passed!")
