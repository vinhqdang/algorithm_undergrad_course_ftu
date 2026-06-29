"""
Problem 07 - Kruskal's Minimum Spanning Tree with Union-Find (SOLUTION)
=======================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, Edge, UnionFind, add_edge, edge_list, vertices  # noqa: E402


def kruskal(graph: Graph) -> Tuple[List[Edge], float]:
    """Compute a minimum spanning tree (or forest) of the undirected ``graph``.

    Returns ``(mst_edges, total_weight)``. Edges are processed in
    non-decreasing weight order; an edge is added iff it joins two different
    components (tested with union-find).
    """
    edges = sorted(edge_list(graph), key=lambda e: e[2])
    uf = UnionFind(vertices(graph))
    mst: List[Edge] = []
    total = 0.0
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total


if __name__ == "__main__":
    g: Graph = {}
    add_edge(g, 0, 1, 1)
    add_edge(g, 1, 2, 2)
    add_edge(g, 0, 2, 2)
    add_edge(g, 2, 3, 3)
    add_edge(g, 1, 3, 4)

    mst, total = kruskal(g)
    # An MST of a 4-vertex connected graph has exactly 3 edges.
    assert len(mst) == 3
    assert total == 6.0  # edges of weight 1, 2, 3

    # Every MST edge actually exists in the graph.
    for u, v, w in mst:
        assert g[u][v] == w

    # Triangle with equal weights: any 2 edges form the MST.
    g2: Graph = {}
    add_edge(g2, 0, 1, 5)
    add_edge(g2, 1, 2, 5)
    add_edge(g2, 0, 2, 5)
    mst2, total2 = kruskal(g2)
    assert len(mst2) == 2
    assert total2 == 10.0

    print("All tests passed!")
