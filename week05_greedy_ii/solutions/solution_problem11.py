"""
Problem 11 - Classify an Edge: in EVERY / SOME / NO MST (SOLUTION)
==================================================================

Uses the cut property and cycle property:
  - An edge is in NO MST iff it is the unique maximum-weight edge on some cycle
    (equivalently: its endpoints are already connected using only strictly
    cheaper edges).
  - An edge is in EVERY MST iff removing it would change the MST weight (it is a
    "bridge" for the cheaper-edge structure / a unique minimum across some cut).
  - Otherwise it is in SOME (but not all) MSTs.

We classify by comparing MST weights with the edge forced-in vs. forbidden.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, Edge, UnionFind, add_edge, edge_list, vertices  # noqa: E402

from solution_problem07 import kruskal  # noqa: E402


def _mst_weight_excluding(graph: Graph, banned: Edge) -> float:
    """MST weight of ``graph`` with ``banned`` removed (inf if disconnected)."""
    bu, bv, bw = banned
    uf = UnionFind(vertices(graph))
    total = 0.0
    count = 0
    for u, v, w in sorted(edge_list(graph), key=lambda e: e[2]):
        if {u, v} == {bu, bv} and w == bw:
            continue
        if uf.union(u, v):
            total += w
            count += 1
    return total if count == len(vertices(graph)) - 1 else float("inf")


def _mst_weight_including(graph: Graph, forced: Edge) -> float:
    """MST weight of ``graph`` forcing ``forced`` in first (inf if impossible)."""
    fu, fv, fw = forced
    uf = UnionFind(vertices(graph))
    total = fw
    uf.union(fu, fv)
    count = 1
    for u, v, w in sorted(edge_list(graph), key=lambda e: e[2]):
        if uf.union(u, v):
            total += w
            count += 1
    return total if count == len(vertices(graph)) - 1 else float("inf")


def classify_edge(graph: Graph, edge: Edge) -> str:
    """Classify ``edge`` as 'every', 'some', or 'none' with respect to MSTs.

    Returns one of the strings ``"every"``, ``"some"``, ``"none"``.
    """
    _, base = kruskal(graph)
    w_in = _mst_weight_including(graph, edge)
    w_out = _mst_weight_excluding(graph, edge)

    in_some = abs(w_in - base) <= 1e-9
    excludable = abs(w_out - base) <= 1e-9

    if not in_some:
        return "none"          # forcing the edge worsens the MST -> in no MST
    if not excludable:
        return "every"         # banning the edge worsens the MST -> in every MST
    return "some"              # achievable both with and without the edge


if __name__ == "__main__":
    # Graph: a 4-cycle 0-1-2-3-0 with weights, plus a chord.
    g: Graph = {}
    add_edge(g, 0, 1, 1)
    add_edge(g, 1, 2, 2)
    add_edge(g, 2, 3, 3)
    add_edge(g, 0, 3, 4)

    # The 4-cycle: the unique heaviest edge 0-3 (weight 4) is in NO MST.
    assert classify_edge(g, (0, 3, 4)) == "none"
    # The unique lightest edges are in EVERY MST.
    assert classify_edge(g, (0, 1, 1)) == "every"
    assert classify_edge(g, (1, 2, 2)) == "every"
    assert classify_edge(g, (2, 3, 3)) == "every"

    # Triangle with equal weights: each edge is in SOME but not EVERY MST.
    g2: Graph = {}
    add_edge(g2, 0, 1, 5)
    add_edge(g2, 1, 2, 5)
    add_edge(g2, 0, 2, 5)
    assert classify_edge(g2, (0, 1, 5)) == "some"
    assert classify_edge(g2, (1, 2, 5)) == "some"
    assert classify_edge(g2, (0, 2, 5)) == "some"

    print("All tests passed!")
