"""
Problem 01 - Bipartite Check via 2-Coloring
=============================================

Implement `bipartite_partition(vertices, edges)` that decides whether an
undirected graph is bipartite using BFS 2-coloring. If it is, return a tuple of
two sets (A, B) giving the bipartition; if it has an odd cycle, return None.

A graph is bipartite iff its vertices can be 2-colored so that every edge joins
vertices of different colors. Run BFS from each unvisited vertex, coloring each
neighbour the opposite color; if you ever find an edge between same-colored
vertices, the graph is not bipartite.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, List, Optional, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def bipartite_partition(
    vertices: List[Vertex], edges: List[Edge]
) -> Optional[Tuple[Set[Vertex], Set[Vertex]]]:
    """Return a 2-coloring (A, B) of the graph, or None if it has an odd cycle."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        res = bipartite_partition([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (3, 0)])
        assert res is not None
        a, b = res
        for u, v in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            assert (u in a) != (v in a)

        assert bipartite_partition([0, 1, 2], [(0, 1), (1, 2), (2, 0)]) is None
        assert bipartite_partition([0, 1, 2], [(0, 1), (1, 2)]) is not None
        assert bipartite_partition([0, 1, 2, 3, 4], [(0, 1), (2, 3), (3, 4), (4, 2)]) is None
        assert bipartite_partition([0, 1, 2], []) is not None
        assert bipartite_partition([], []) is not None

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
