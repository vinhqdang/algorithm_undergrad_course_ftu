"""
Problem 12 - Single-Link k-Clustering via Kruskal
=================================================

Form k clusters of maximum spacing by running Kruskal's algorithm until exactly
k components remain (equivalently, build the MST and delete its k-1 heaviest
edges). The spacing is the minimum distance between points in different
clusters. See practical_exercises.pdf, Problem 12.
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, UnionFind, add_edge, edge_list, vertices  # noqa: F401,E402


def single_link_clustering(
    graph: Graph, k: int
) -> Tuple[List[List[Hashable]], float]:
    """Partition the vertices of ``graph`` into ``k`` clusters of max spacing.

    Returns ``(clusters, spacing)``: a list of ``k`` lists of vertices, and the
    minimum inter-cluster edge weight (``float('inf')`` when ``k`` equals the
    number of vertices).
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g: Graph = {}
        add_edge(g, 0, 1, 1)
        add_edge(g, 2, 3, 1)
        add_edge(g, 1, 2, 10)

        clusters, spacing = single_link_clustering(g, k=2)
        assert len(clusters) == 2
        sets = sorted(sorted(c) for c in clusters)
        assert sets == [[0, 1], [2, 3]]
        assert spacing == 10.0

        clusters1, spacing1 = single_link_clustering(g, k=1)
        assert len(clusters1) == 1
        assert spacing1 == float("inf")

        clusters4, spacing4 = single_link_clustering(g, k=4)
        assert len(clusters4) == 4
        assert spacing4 == 1.0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
