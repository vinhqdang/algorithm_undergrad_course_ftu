"""
Problem 10 - Verify the Cut Property (SOLUTION)
================================================

Cut property: for any cut (a partition of the vertices into S and V\\S), the
minimum-weight edge crossing the cut belongs to *some* minimum spanning tree.
If that crossing edge is the *unique* minimum, it belongs to *every* MST.
"""

import os
import sys
from typing import List, Optional, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, Edge, add_edge, edge_list  # noqa: E402

from solution_problem07 import kruskal  # noqa: E402


def crossing_edges(graph: Graph, S: Set) -> List[Edge]:
    """Return all edges with exactly one endpoint in ``S``."""
    out = []
    for u, v, w in edge_list(graph):
        if (u in S) != (v in S):
            out.append((u, v, w))
    return out


def min_crossing_edge(graph: Graph, S: Set) -> Optional[Edge]:
    """Return a minimum-weight edge crossing the cut ``(S, V\\S)`` (or None)."""
    crossing = crossing_edges(graph, S)
    if not crossing:
        return None
    return min(crossing, key=lambda e: e[2])


def _mst_contains(mst: List[Edge], edge: Edge) -> bool:
    u, v, w = edge
    for a, b, c in mst:
        if c == w and {a, b} == {u, v}:
            return True
    return False


def cut_property_holds(graph: Graph, S: Set) -> bool:
    """Verify the cut property for the given cut on ``graph``.

    Builds an MST (via Kruskal). If the minimum crossing edge is unique, it must
    appear in this MST. If there are ties, *some* MST contains the chosen min
    edge -- we verify by forcing that edge first and completing it to a spanning
    tree of the same total weight as the unconstrained MST.
    """
    e = min_crossing_edge(graph, S)
    if e is None:
        return True  # empty cut: vacuously true

    mst, mst_weight = kruskal(graph)

    if _mst_contains(mst, e):
        return True

    # Tie case: force e into an MST and check the total weight is unchanged.
    forced_weight, ok = _mst_forcing_edge(graph, e)
    return ok and abs(forced_weight - mst_weight) <= 1e-9


def _mst_forcing_edge(graph: Graph, edge: Edge) -> Tuple[float, bool]:
    """Build a spanning tree that includes ``edge`` first (Kruskal variant)."""
    from starter_code import UnionFind, vertices

    u0, v0, w0 = edge
    uf = UnionFind(vertices(graph))
    total = w0
    uf.union(u0, v0)
    count = 1
    for u, v, w in sorted(edge_list(graph), key=lambda e: e[2]):
        if uf.union(u, v):
            total += w
            count += 1
    n = len(vertices(graph))
    return total, count == n - 1


if __name__ == "__main__":
    g: Graph = {}
    add_edge(g, 0, 1, 1)
    add_edge(g, 1, 2, 2)
    add_edge(g, 0, 2, 2)
    add_edge(g, 2, 3, 3)
    add_edge(g, 1, 3, 4)

    # Cut {0} vs rest: min crossing edge is 0-1 (weight 1).
    e = min_crossing_edge(g, {0})
    assert e[2] == 1.0 and {e[0], e[1]} == {0, 1}
    assert cut_property_holds(g, {0}) is True

    # Several other cuts.
    assert cut_property_holds(g, {0, 1}) is True
    assert cut_property_holds(g, {3}) is True
    assert cut_property_holds(g, {0, 2}) is True

    # Random instances.
    from starter_code import generate_weighted_graph

    for seed in range(20):
        rg = generate_weighted_graph(10, seed=seed, edge_prob=0.4)
        assert cut_property_holds(rg, {0, 1, 2}) is True

    print("All tests passed!")
