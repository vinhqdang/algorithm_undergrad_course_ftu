"""
Problem 08 - Prim's Minimum Spanning Tree with a Heap
=====================================================

Implement Prim's algorithm: grow a tree from a start vertex, always adding the
cheapest edge crossing from the tree to a vertex outside it, using a binary heap
(``heapq``). See practical_exercises.pdf, Problem 8.
"""

import heapq  # noqa: F401  (you will need this)
import os
import sys
from typing import Hashable, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge, vertices  # noqa: F401,E402


def prim(graph: Graph, start: Optional[Hashable] = None) -> float:
    """Return the total weight of a minimum spanning tree via Prim's algorithm.

    Assumes the graph is connected. Default ``start`` is the first vertex.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g: Graph = {}
        add_edge(g, 0, 1, 1)
        add_edge(g, 1, 2, 2)
        add_edge(g, 0, 2, 2)
        add_edge(g, 2, 3, 3)
        add_edge(g, 1, 3, 4)

        assert prim(g) == 6.0
        assert prim(g, start=3) == 6.0

        g2: Graph = {}
        add_edge(g2, 0, 1, 5)
        add_edge(g2, 1, 2, 5)
        add_edge(g2, 0, 2, 5)
        assert prim(g2) == 10.0

        assert prim({0: {}}) == 0.0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
