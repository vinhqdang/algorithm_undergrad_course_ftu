"""
Problem 05 - Clique Verifier, Maximum Clique, Complement Identity
=================================================================

Implement:
  - is_clique_subset(graph, subset): True iff every pair in subset is an edge.
  - max_clique(graph): brute-force maximum clique (frozenset).
  - verify_clique_is_complement(graph): True iff the max clique size in G equals
    the max independent set size in complement(G).

Helpers `complement_graph`, `is_independent_set`, `max_independent_set` are
re-provided so this file is self-contained.

See practical_exercises.pdf, Problem 5.
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
    # TODO: implement this function.
    raise NotImplementedError


def max_clique(graph: Graph) -> FrozenSet[int]:
    """Return a maximum clique (brute force, largest first)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_clique_is_complement(graph: Graph) -> bool:
    """True iff max clique size in G == max independent set size in complement(G)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g = make_graph(3, [(0, 1), (1, 2), (0, 2)])
        assert is_clique_subset(g, [0, 1, 2]) is True
        assert is_clique_subset(g, [0, 1]) is True
        assert len(max_clique(g)) == 3
        assert verify_clique_is_complement(g)

        p = make_graph(4, [(0, 1), (1, 2), (2, 3)])
        assert len(max_clique(p)) == 2
        assert verify_clique_is_complement(p)

        e = make_graph(4, [])
        assert len(max_clique(e)) == 1
        assert verify_clique_is_complement(e)

        k4 = make_graph(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
        assert len(max_clique(k4)) == 4
        assert verify_clique_is_complement(k4)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
