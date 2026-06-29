"""
Problem 11 - Chromatic Number (Trying k = 1, 2, 3, ...) (SOLUTION)
===================================================================
"""

from typing import Iterable, List, Optional, Set, Tuple, FrozenSet

Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def make_graph(n: int, edge_list: Iterable[Tuple[int, int]]) -> Graph:
    edges: Set[Edge] = set()
    for u, v in edge_list:
        if u != v:
            edges.add(frozenset({u, v}))
    return (n, edges)


def k_coloring(graph: Graph, k: int) -> Optional[List[int]]:
    """Backtracking search for a proper k-coloring, or None."""
    n, edges = graph
    if n == 0:
        return []
    if k <= 0:
        return None

    adj: List[Set[int]] = [set() for _ in range(n)]
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)

    coloring = [-1] * n

    def backtrack(v: int) -> bool:
        if v == n:
            return True
        for c in range(k):
            if all(coloring[w] != c for w in adj[v]):
                coloring[v] = c
                if backtrack(v + 1):
                    return True
                coloring[v] = -1
        return False

    return list(coloring) if backtrack(0) else None


def chromatic_number(graph: Graph) -> int:
    """Smallest k for which `graph` has a proper k-coloring.
    Empty graph on 0 vertices needs 0; a graph with vertices but no edges needs 1."""
    n, _ = graph
    if n == 0:
        return 0
    for k in range(1, n + 1):
        if k_coloring(graph, k) is not None:
            return k
    return n  # at most n colors always suffice


def is_three_colorable(graph: Graph) -> bool:
    """Return True iff chromatic_number(graph) <= 3."""
    return chromatic_number(graph) <= 3


if __name__ == "__main__":
    # Triangle K3: chromatic number 3
    k3 = make_graph(3, [(0, 1), (1, 2), (0, 2)])
    assert chromatic_number(k3) == 3
    assert is_three_colorable(k3)

    # Even cycle C4 (bipartite): chromatic number 2
    c4 = make_graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    assert chromatic_number(c4) == 2

    # Odd cycle C5: chromatic number 3
    c5 = make_graph(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
    assert chromatic_number(c5) == 3

    # Empty graph on 4 vertices: chromatic number 1
    e = make_graph(4, [])
    assert chromatic_number(e) == 1

    # No vertices: chromatic number 0
    assert chromatic_number(make_graph(0, [])) == 0

    # K4: chromatic number 4 (NOT 3-colorable)
    k4 = make_graph(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    assert chromatic_number(k4) == 4
    assert is_three_colorable(k4) is False

    print("All tests passed!")
