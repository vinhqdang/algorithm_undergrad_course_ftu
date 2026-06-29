"""
Problem 08 - Prim's Minimum Spanning Tree with a Heap (SOLUTION)
================================================================
"""

import heapq
import os
import sys
from typing import Hashable, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge, vertices  # noqa: E402


def prim(graph: Graph, start: Optional[Hashable] = None) -> float:
    """Return the total weight of a minimum spanning tree via Prim's algorithm.

    Grows a tree from ``start`` (default: the first vertex), always adding the
    cheapest edge crossing from the tree to a vertex outside it, using a binary
    heap of candidate edges. Assumes the graph is connected.
    """
    verts = vertices(graph)
    if not verts:
        return 0.0
    if start is None:
        start = verts[0]

    in_tree = {start}
    total = 0.0
    heap = [(w, v) for v, w in graph[start].items()]
    heapq.heapify(heap)

    while heap and len(in_tree) < len(verts):
        w, v = heapq.heappop(heap)
        if v in in_tree:
            continue
        in_tree.add(v)
        total += w
        for nv, nw in graph[v].items():
            if nv not in in_tree:
                heapq.heappush(heap, (nw, nv))
    return total


if __name__ == "__main__":
    g: Graph = {}
    add_edge(g, 0, 1, 1)
    add_edge(g, 1, 2, 2)
    add_edge(g, 0, 2, 2)
    add_edge(g, 2, 3, 3)
    add_edge(g, 1, 3, 4)

    assert prim(g) == 6.0
    assert prim(g, start=3) == 6.0  # MST weight is start-independent

    # Triangle with equal weights.
    g2: Graph = {}
    add_edge(g2, 0, 1, 5)
    add_edge(g2, 1, 2, 5)
    add_edge(g2, 0, 2, 5)
    assert prim(g2) == 10.0

    # Single vertex.
    assert prim({0: {}}) == 0.0

    print("All tests passed!")
