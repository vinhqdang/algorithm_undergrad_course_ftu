"""
Problem 04 - Vertex-Cover Verifier, Minimum Vertex Cover, Complementarity
=========================================================================

Implement:
  - is_vertex_cover(graph, subset): True iff every edge has an endpoint in subset.
  - min_vertex_cover(graph): brute-force minimum vertex cover (frozenset).
  - verify_vc_complement(graph): True iff V \\ (max IS) is a minimum vertex
    cover -- i.e. |VC| = n - |IS| AND the complement of a max IS is a valid
    vertex cover.

The helpers `is_independent_set` and `max_independent_set` (from Problem 3) are
re-provided here so this file is self-contained.

See practical_exercises.pdf, Problem 4.
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
    # TODO: implement this function.
    raise NotImplementedError


def min_vertex_cover(graph: Graph) -> FrozenSet[int]:
    """Return a minimum vertex cover (brute force, smallest first)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_vc_complement(graph: Graph) -> bool:
    """True iff V \\ (max IS) is a minimum vertex cover."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g = make_graph(3, [(0, 1), (1, 2), (0, 2)])
        assert is_vertex_cover(g, [0, 1]) is True
        assert is_vertex_cover(g, [0]) is False
        assert len(min_vertex_cover(g)) == 2
        assert verify_vc_complement(g)

        p = make_graph(4, [(0, 1), (1, 2), (2, 3)])
        assert len(min_vertex_cover(p)) == 2
        assert verify_vc_complement(p)

        e = make_graph(5, [])
        assert len(min_vertex_cover(e)) == 0
        assert verify_vc_complement(e)

        for edges in ([(0, 1), (2, 3), (0, 3)], [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]):
            n = 1 + max(max(u, v) for u, v in edges)
            gg = make_graph(n, edges)
            assert verify_vc_complement(gg)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
