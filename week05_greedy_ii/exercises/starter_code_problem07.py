"""
Problem 07 - Kruskal's Minimum Spanning Tree with Union-Find
============================================================

Implement Kruskal's algorithm: sort the edges by weight and add each edge that
joins two different components (tested with the ``UnionFind`` class from
starter_code.py). See practical_exercises.pdf, Problem 7.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, Edge, UnionFind, add_edge, edge_list, vertices  # noqa: F401,E402


def kruskal(graph: Graph) -> Tuple[List[Edge], float]:
    """Compute a minimum spanning tree (or forest) of the undirected ``graph``.

    Returns ``(mst_edges, total_weight)``.
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

        mst, total = kruskal(g)
        assert len(mst) == 3
        assert total == 6.0
        for u, v, w in mst:
            assert g[u][v] == w

        g2: Graph = {}
        add_edge(g2, 0, 1, 5)
        add_edge(g2, 1, 2, 5)
        add_edge(g2, 0, 2, 5)
        mst2, total2 = kruskal(g2)
        assert len(mst2) == 2
        assert total2 == 10.0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
