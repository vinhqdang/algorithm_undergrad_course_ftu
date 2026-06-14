"""
Problem 12 - Bipartiteness Testing via BFS 2-Coloring
========================================================

A graph is BIPARTITE iff its vertices can be partitioned into two sets A and
B such that every edge has one endpoint in A and one in B (equivalently: it
can be properly colored with 2 colors).

Implement `two_color_bfs(adj)`, which attempts to 2-color the graph using
BFS: assign the source of each BFS a color (0), then alternate colors level
by level (every neighbor gets the OPPOSITE color of its discoverer). Handle
graphs with multiple connected components (run BFS from every unvisited
vertex).

Return a list `color` of length `len(adj)` where `color[v] in {0, 1}` for
every vertex, IF the graph is bipartite. If the graph is NOT bipartite,
return `None`.

Then implement `is_bipartite(adj)`, returning `True`/`False`.

See practical_exercises.pdf, Problem 12.
"""

from collections import deque
from typing import List, Optional


def two_color_bfs(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a valid 2-coloring (list of 0/1) if the graph is bipartite, else None."""
    # TODO: implement this function.
    raise NotImplementedError


def is_bipartite(adj: List[List[int]]) -> bool:
    """Return True iff the graph is bipartite."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Even cycle (4-cycle): bipartite
        c4 = [[1, 3], [0, 2], [1, 3], [0, 2]]
        assert is_bipartite(c4) is True
        coloring = two_color_bfs(c4)
        assert coloring is not None
        for u in range(4):
            for v in c4[u]:
                assert coloring[u] != coloring[v]

        # Odd cycle (triangle, 3-cycle): NOT bipartite
        c3 = [[1, 2], [0, 2], [0, 1]]
        assert is_bipartite(c3) is False
        assert two_color_bfs(c3) is None

        # Star graph: bipartite (center vs leaves)
        star = [[1, 2, 3], [0], [0], [0]]
        assert is_bipartite(star) is True

        # Disconnected: one bipartite component + one non-bipartite component
        mixed = [[1, 3], [0, 2], [1, 3], [0, 2]] + [[5, 6], [4, 6], [4, 5]]
        # vertices 0-3 form a C4 (bipartite), vertices 4-6 form a C3 (not bipartite)
        # but adjacency lists must reference correct global indices:
        mixed = [
            [1, 3], [0, 2], [1, 3], [0, 2],  # C4 on {0,1,2,3}
            [5, 6], [4, 6], [4, 5],          # C3 on {4,5,6}
        ]
        assert is_bipartite(mixed) is False

        # Empty graph (no edges): trivially bipartite
        empty = [[], [], []]
        assert is_bipartite(empty) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
