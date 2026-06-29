"""
Problem 05 - Clique Verifier, Maximum Clique, Complement Identity (SOLUTION)
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


def complement_graph(graph: Graph) -> Graph:
    n, edges = graph
    comp: Set[Edge] = set()
    for u in range(n):
        for v in range(u + 1, n):
            if frozenset({u, v}) not in edges:
                comp.add(frozenset({u, v}))
    return (n, comp)


def is_independent_set(graph: Graph, subset: Iterable[int]) -> bool:
    _, edges = graph
    vs = list(subset)
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if frozenset({vs[i], vs[j]}) in edges:
                return False
    return True


def max_independent_set(graph: Graph) -> FrozenSet[int]:
    n, _ = graph
    for size in range(n, -1, -1):
        for combo in itertools.combinations(range(n), size):
            if is_independent_set(graph, combo):
                return frozenset(combo)
    return frozenset()


def is_clique_subset(graph: Graph, subset: Iterable[int]) -> bool:
    """Return True iff every pair of vertices in `subset` is joined by an edge."""
    _, edges = graph
    vs = list(subset)
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if frozenset({vs[i], vs[j]}) not in edges:
                return False
    return True


def max_clique(graph: Graph) -> FrozenSet[int]:
    """Return a maximum clique (brute force, largest first)."""
    n, _ = graph
    for size in range(n, -1, -1):
        for combo in itertools.combinations(range(n), size):
            if is_clique_subset(graph, combo):
                return frozenset(combo)
    return frozenset()


def verify_clique_is_complement(graph: Graph) -> bool:
    """True iff max clique size in G == max independent set size in complement(G)."""
    clique = max_clique(graph)
    mis_comp = max_independent_set(complement_graph(graph))
    return len(clique) == len(mis_comp)


if __name__ == "__main__":
    # Triangle K3: maximum clique is the whole triangle (size 3)
    g = make_graph(3, [(0, 1), (1, 2), (0, 2)])
    assert is_clique_subset(g, [0, 1, 2]) is True
    assert is_clique_subset(g, [0, 1]) is True
    assert len(max_clique(g)) == 3
    assert verify_clique_is_complement(g)

    # Path 0-1-2-3: max clique is an edge (size 2)
    p = make_graph(4, [(0, 1), (1, 2), (2, 3)])
    assert len(max_clique(p)) == 2
    assert verify_clique_is_complement(p)

    # Empty graph: max clique is a single vertex (size 1)
    e = make_graph(4, [])
    assert len(max_clique(e)) == 1
    assert verify_clique_is_complement(e)

    # K4: max clique size 4
    k4 = make_graph(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    assert len(max_clique(k4)) == 4
    assert verify_clique_is_complement(k4)

    print("All tests passed!")
