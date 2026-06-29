"""
Problem 12 - Reduction Certificate Demo: Vertex Cover <-> Independent Set
========================================================================

Build a poly-time mapping reduction and verify the certificate equivalence
"x in A  iff  f(x) in B" on random small instances, where
    A = { (G, k) : G has an independent set of size >= k }
    B = { (G, j) : G has a vertex cover of size <= j }
    f(G, k) = (G, n - k).

Implement:
  - has_independent_set(graph, k): brute force; True iff IS of size >= k exists.
  - has_vertex_cover(graph, k):    brute force; True iff VC of size <= k exists.
  - reduce_is_to_vc(graph, k):     return (graph, n - k).
  - verify_mapping(num_trials, n, seed): for random graphs and all thresholds k,
    confirm has_independent_set(G, k) == has_vertex_cover(*reduce_is_to_vc(G, k)).

See practical_exercises.pdf, Problem 12.
"""

import itertools
import random
from typing import FrozenSet, Iterable, Set, Tuple

Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def _is_independent_set(graph: Graph, subset: Iterable[int]) -> bool:
    _, edges = graph
    vs = list(subset)
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if frozenset({vs[i], vs[j]}) in edges:
                return False
    return True


def _is_vertex_cover(graph: Graph, subset: Iterable[int]) -> bool:
    _, edges = graph
    cover = set(subset)
    return all(bool(e & cover) for e in edges)


def has_independent_set(graph: Graph, k: int) -> bool:
    """Return True iff `graph` has an independent set of size >= k."""
    # TODO: implement this function.
    raise NotImplementedError


def has_vertex_cover(graph: Graph, k: int) -> bool:
    """Return True iff `graph` has a vertex cover of size <= k."""
    # TODO: implement this function.
    raise NotImplementedError


def reduce_is_to_vc(graph: Graph, k: int) -> Tuple[Graph, int]:
    """Mapping reduction: return (graph, n - k)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_mapping(num_trials: int, n: int, seed: int) -> bool:
    """Confirm has_independent_set(G, k) == has_vertex_cover(*reduce_is_to_vc(G, k))."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        k3 = (3, {frozenset({0, 1}), frozenset({1, 2}), frozenset({0, 2})})
        assert has_independent_set(k3, 1) is True
        assert has_independent_set(k3, 2) is False
        g, j = reduce_is_to_vc(k3, 1)
        assert (g, j) == (k3, 2)
        assert has_vertex_cover(k3, 2) is True
        assert has_vertex_cover(k3, 1) is False

        assert verify_mapping(num_trials=30, n=5, seed=7)
        assert verify_mapping(num_trials=15, n=7, seed=123)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
