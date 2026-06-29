"""
Problem 04 - Vertex-Cover Verifier, Minimum Vertex Cover, Complementarity (SOLUTION)
=====================================================================================
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


def is_vertex_cover(graph: Graph, subset: Iterable[int]) -> bool:
    """Return True iff every edge has at least one endpoint in `subset`."""
    _, edges = graph
    cover = set(subset)
    for e in edges:
        if not (e & cover):
            return False
    return True


def min_vertex_cover(graph: Graph) -> FrozenSet[int]:
    """Return a minimum vertex cover (brute force, smallest first)."""
    n, _ = graph
    for size in range(0, n + 1):
        for combo in itertools.combinations(range(n), size):
            if is_vertex_cover(graph, combo):
                return frozenset(combo)
    return frozenset(range(n))


def verify_vc_complement(graph: Graph) -> bool:
    """True iff V \\ (max IS) is a minimum vertex cover, i.e. |VC| = n - |IS|
    and the complement of a max IS is actually a valid vertex cover."""
    n, _ = graph
    mis = max_independent_set(graph)
    mvc = min_vertex_cover(graph)
    complement = frozenset(range(n)) - mis
    return (
        is_vertex_cover(graph, complement)
        and len(complement) == len(mvc)
        and len(mvc) == n - len(mis)
    )


if __name__ == "__main__":
    # Triangle K3: min vertex cover has size 2
    g = make_graph(3, [(0, 1), (1, 2), (0, 2)])
    assert is_vertex_cover(g, [0, 1]) is True
    assert is_vertex_cover(g, [0]) is False
    assert len(min_vertex_cover(g)) == 2
    assert verify_vc_complement(g)

    # Path 0-1-2-3: min vertex cover has size 1 ({1}? no, edge 2-3 uncovered) => 2
    p = make_graph(4, [(0, 1), (1, 2), (2, 3)])
    assert len(min_vertex_cover(p)) == 2
    assert verify_vc_complement(p)

    # Empty graph: min vertex cover is empty
    e = make_graph(5, [])
    assert len(min_vertex_cover(e)) == 0
    assert verify_vc_complement(e)

    # A few random-ish graphs
    for edges in ([(0, 1), (2, 3), (0, 3)], [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]):
        n = 1 + max(max(u, v) for u, v in edges)
        gg = make_graph(n, edges)
        assert verify_vc_complement(gg)

    print("All tests passed!")
