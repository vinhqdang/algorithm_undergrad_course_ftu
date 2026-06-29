"""
Problem 03 - Independent-Set Verifier and Maximum Independent Set (SOLUTION)
=============================================================================
"""

import itertools
from typing import FrozenSet, Iterable, Set, Tuple

Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def make_graph(n: int, edge_list: Iterable[Tuple[int, int]]) -> Graph:
    edges: Set[Edge] = set()
    for u, v in edge_list:
        if u != v:
            edges.add(frozenset({u, v}))
    return (n, edges)


def is_independent_set(graph: Graph, subset: Iterable[int]) -> bool:
    """Return True iff no two vertices of `subset` are joined by an edge."""
    _, edges = graph
    vs = list(subset)
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if frozenset({vs[i], vs[j]}) in edges:
                return False
    return True


def max_independent_set(graph: Graph) -> FrozenSet[int]:
    """Return a maximum independent set (brute force over all subsets)."""
    n, _ = graph
    for size in range(n, -1, -1):
        for combo in itertools.combinations(range(n), size):
            if is_independent_set(graph, combo):
                return frozenset(combo)
    return frozenset()


if __name__ == "__main__":
    # Triangle K3: largest independent set has size 1
    g = make_graph(3, [(0, 1), (1, 2), (0, 2)])
    assert is_independent_set(g, []) is True
    assert is_independent_set(g, [0]) is True
    assert is_independent_set(g, [0, 1]) is False
    assert len(max_independent_set(g)) == 1

    # Path 0-1-2-3: max independent set has size 2 (e.g. {0, 2} or {0, 3})
    p = make_graph(4, [(0, 1), (1, 2), (2, 3)])
    mis = max_independent_set(p)
    assert len(mis) == 2
    assert is_independent_set(p, mis)

    # Empty graph on 5 vertices: all 5 form an independent set
    e = make_graph(5, [])
    assert len(max_independent_set(e)) == 5

    # 4-cycle: max independent set has size 2
    c4 = make_graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    assert len(max_independent_set(c4)) == 2

    print("All tests passed!")
