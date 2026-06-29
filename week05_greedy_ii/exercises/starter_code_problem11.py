"""
Problem 11 - Classify an Edge: in EVERY / SOME / NO MST
=======================================================

Using the cut and cycle properties, classify a given edge as belonging to
EVERY minimum spanning tree, SOME (but not all) MST, or NO MST. See
practical_exercises.pdf, Problem 11.

Hint: compare the overall MST weight with the MST weight when the edge is
forced in, and when it is forbidden.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from starter_code import Graph, Edge, UnionFind, add_edge, edge_list, vertices  # noqa: F401,E402

from starter_code_problem07 import kruskal  # noqa: F401,E402


def classify_edge(graph: Graph, edge: Edge) -> str:
    """Classify ``edge`` with respect to MSTs.

    Returns one of the strings ``"every"``, ``"some"``, ``"none"``.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g: Graph = {}
        add_edge(g, 0, 1, 1)
        add_edge(g, 1, 2, 2)
        add_edge(g, 2, 3, 3)
        add_edge(g, 0, 3, 4)

        assert classify_edge(g, (0, 3, 4)) == "none"
        assert classify_edge(g, (0, 1, 1)) == "every"
        assert classify_edge(g, (1, 2, 2)) == "every"
        assert classify_edge(g, (2, 3, 3)) == "every"

        g2: Graph = {}
        add_edge(g2, 0, 1, 5)
        add_edge(g2, 1, 2, 5)
        add_edge(g2, 0, 2, 5)
        assert classify_edge(g2, (0, 1, 5)) == "some"
        assert classify_edge(g2, (1, 2, 5)) == "some"
        assert classify_edge(g2, (0, 2, 5)) == "some"

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
