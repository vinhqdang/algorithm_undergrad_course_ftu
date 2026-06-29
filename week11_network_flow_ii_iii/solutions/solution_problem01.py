"""
Problem 01 - Bipartite Check via 2-Coloring (SOLUTION)
========================================================
"""

import os
import sys
from collections import deque
from typing import Dict, Hashable, List, Optional, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def bipartite_partition(
    vertices: List[Vertex], edges: List[Edge]
) -> Optional[Tuple[Set[Vertex], Set[Vertex]]]:
    """Return a 2-coloring (A, B) of the graph, or None if it has an odd cycle.

    Runs BFS from each unvisited vertex, alternating colors 0/1 across edges.
    If an edge ever joins two same-colored vertices, the graph is not bipartite.
    """
    adj: Dict[Vertex, Set[Vertex]] = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    color: Dict[Vertex, int] = {}
    for start in vertices:
        if start in color:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for w in adj[u]:
                if w not in color:
                    color[w] = 1 - color[u]
                    queue.append(w)
                elif color[w] == color[u]:
                    return None

    side_a = {v for v in vertices if color[v] == 0}
    side_b = {v for v in vertices if color[v] == 1}
    return side_a, side_b


if __name__ == "__main__":
    # An even cycle is bipartite.
    res = bipartite_partition([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (3, 0)])
    assert res is not None
    a, b = res
    for u, v in [(0, 1), (1, 2), (2, 3), (3, 0)]:
        assert (u in a) != (v in a)  # endpoints on opposite sides

    # A triangle (odd cycle) is NOT bipartite.
    assert bipartite_partition([0, 1, 2], [(0, 1), (1, 2), (2, 0)]) is None

    # A path is bipartite.
    assert bipartite_partition([0, 1, 2], [(0, 1), (1, 2)]) is not None

    # Disconnected graph: triangle in one component makes the whole thing fail.
    assert bipartite_partition([0, 1, 2, 3, 4], [(0, 1), (2, 3), (3, 4), (4, 2)]) is None

    # Empty graph / isolated vertices are trivially bipartite.
    assert bipartite_partition([0, 1, 2], []) is not None
    assert bipartite_partition([], []) is not None

    print("All tests passed!")
