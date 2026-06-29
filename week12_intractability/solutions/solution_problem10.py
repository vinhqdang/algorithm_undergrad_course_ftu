"""
Problem 10 - Graph k-Coloring by Backtracking (SOLUTION)
=========================================================
"""

from typing import Dict, FrozenSet, Iterable, List, Optional, Sequence, Set, Tuple

Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def make_graph(n: int, edge_list: Iterable[Tuple[int, int]]) -> Graph:
    edges: Set[Edge] = set()
    for u, v in edge_list:
        if u != v:
            edges.add(frozenset({u, v}))
    return (n, edges)


def verify_coloring(graph: Graph, coloring: Sequence[int]) -> bool:
    """Return True iff `coloring` (indexed by vertex) is a proper coloring:
    no edge joins two equally-colored vertices."""
    n, edges = graph
    if len(coloring) != n:
        return False
    for e in edges:
        u, v = tuple(e)
        if coloring[u] == coloring[v]:
            return False
    return True


def k_coloring(graph: Graph, k: int) -> Optional[List[int]]:
    """Backtracking search for a proper coloring with colors {0..k-1}, or None."""
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

    if backtrack(0):
        return list(coloring)
    return None


if __name__ == "__main__":
    # Triangle K3: needs 3 colors
    k3 = make_graph(3, [(0, 1), (1, 2), (0, 2)])
    assert k_coloring(k3, 2) is None
    c = k_coloring(k3, 3)
    assert c is not None and verify_coloring(k3, c)

    # Even cycle C4: 2-colorable
    c4 = make_graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    c = k_coloring(c4, 2)
    assert c is not None and verify_coloring(c4, c)

    # Odd cycle C5: not 2-colorable, but 3-colorable
    c5 = make_graph(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
    assert k_coloring(c5, 2) is None
    c = k_coloring(c5, 3)
    assert c is not None and verify_coloring(c5, c)

    # Empty graph: 1 color suffices
    e = make_graph(4, [])
    c = k_coloring(e, 1)
    assert c is not None and verify_coloring(e, c)

    # Verifier catches a bad coloring
    assert verify_coloring(k3, [0, 0, 1]) is False

    print("All tests passed!")
