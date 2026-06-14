"""
Problem 12 - Bipartiteness Testing via BFS 2-Coloring (SOLUTION)
===================================================================
"""

from collections import deque
from typing import List, Optional


def two_color_bfs(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a valid 2-coloring (list of 0/1) if the graph is bipartite, else None."""
    n = len(adj)
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return None

    return color


def is_bipartite(adj: List[List[int]]) -> bool:
    """Return True iff the graph is bipartite."""
    return two_color_bfs(adj) is not None


if __name__ == "__main__":
    c4 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert is_bipartite(c4) is True
    coloring = two_color_bfs(c4)
    assert coloring is not None
    for u in range(4):
        for v in c4[u]:
            assert coloring[u] != coloring[v]

    c3 = [[1, 2], [0, 2], [0, 1]]
    assert is_bipartite(c3) is False
    assert two_color_bfs(c3) is None

    star = [[1, 2, 3], [0], [0], [0]]
    assert is_bipartite(star) is True

    mixed = [
        [1, 3], [0, 2], [1, 3], [0, 2],
        [5, 6], [4, 6], [4, 5],
    ]
    assert is_bipartite(mixed) is False

    empty = [[], [], []]
    assert is_bipartite(empty) is True

    print("All tests passed!")
