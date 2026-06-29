"""
Problem 12 - Single-Link k-Clustering via Kruskal (SOLUTION)
============================================================

To split a set of points into k clusters of maximum *spacing* (the minimum
distance between points in different clusters), run Kruskal's algorithm but stop
as soon as exactly k components remain. Equivalently: build the MST and delete
its k-1 most expensive edges. The spacing equals the next edge Kruskal *would*
have added (the (k-1)-th most expensive MST edge).
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, UnionFind, add_edge, edge_list, vertices  # noqa: E402


def single_link_clustering(
    graph: Graph, k: int
) -> Tuple[List[List[Hashable]], float]:
    """Partition the vertices of ``graph`` into ``k`` clusters of max spacing.

    Returns ``(clusters, spacing)`` where ``clusters`` is a list of ``k`` lists
    of vertices, and ``spacing`` is the minimum inter-cluster edge weight (the
    weight of the first edge Kruskal would add to drop below ``k`` clusters), or
    ``float('inf')`` if ``k`` equals the number of vertices (every point alone).
    """
    verts = vertices(graph)
    n = len(verts)
    if k <= 0 or k > n:
        raise ValueError("k must satisfy 1 <= k <= number of vertices")

    uf = UnionFind(verts)
    edges = sorted(edge_list(graph), key=lambda e: e[2])

    spacing = float("inf")
    for u, v, w in edges:
        if uf.num_sets <= k:
            # The next edge that would merge two distinct clusters defines the
            # spacing (the smallest distance between separate clusters).
            if uf.find(u) != uf.find(v):
                spacing = w
                break
            continue
        uf.union(u, v)

    # Group vertices by their union-find representative.
    groups: Dict[Hashable, List[Hashable]] = {}
    for x in verts:
        groups.setdefault(uf.find(x), []).append(x)
    clusters = list(groups.values())
    return clusters, spacing


if __name__ == "__main__":
    # Points roughly on a line: 0-1 close, 2-3 close, big gap between the pairs.
    g: Graph = {}
    add_edge(g, 0, 1, 1)
    add_edge(g, 2, 3, 1)
    add_edge(g, 1, 2, 10)  # the expensive bridge between the two pairs

    clusters, spacing = single_link_clustering(g, k=2)
    assert len(clusters) == 2
    # The two natural clusters are {0,1} and {2,3}.
    sets = sorted(sorted(c) for c in clusters)
    assert sets == [[0, 1], [2, 3]]
    # Spacing is the cut edge weight (10).
    assert spacing == 10.0

    # k = 1: everything in one cluster, spacing infinite.
    clusters1, spacing1 = single_link_clustering(g, k=1)
    assert len(clusters1) == 1
    assert spacing1 == float("inf")

    # k = n: every point alone; spacing is the smallest edge that would merge.
    clusters4, spacing4 = single_link_clustering(g, k=4)
    assert len(clusters4) == 4
    assert spacing4 == 1.0

    print("All tests passed!")
