"""
Problem 12 - Reduction Certificate Demo: Vertex Cover <-> Independent Set (SOLUTION)
=====================================================================================

We build the poly-time mapping reduction Independent Set <=p Vertex Cover and
verify the certificate equivalence "x in A  iff  f(x) in B" on random small
instances, where:
    A = { (G, k) : G has an independent set of size >= k }
    B = { (G, j) : G has a vertex cover of size <= j }
    f(G, k) = (G, n - k).
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
    n, _ = graph
    if k <= 0:
        return True
    for combo in itertools.combinations(range(n), k):
        if _is_independent_set(graph, combo):
            return True
    return False


def has_vertex_cover(graph: Graph, k: int) -> bool:
    """Return True iff `graph` has a vertex cover of size <= k."""
    n, _ = graph
    if k < 0:
        return False
    upper = min(k, n)
    for size in range(0, upper + 1):
        for combo in itertools.combinations(range(n), size):
            if _is_vertex_cover(graph, combo):
                return True
    return False


def reduce_is_to_vc(graph: Graph, k: int) -> Tuple[Graph, int]:
    """Mapping reduction: (G has IS >= k)  iff  (G has VC <= n - k).
    Leave the graph unchanged; complement the threshold."""
    n, _ = graph
    return graph, n - k


def verify_mapping(num_trials: int, n: int, seed: int) -> bool:
    """For random graphs and a sweep of thresholds k, confirm
    has_independent_set(G, k) == has_vertex_cover(*reduce_is_to_vc(G, k))."""
    for t in range(num_trials):
        rng = random.Random(seed + t)
        edges: Set[Edge] = set()
        for u in range(n):
            for v in range(u + 1, n):
                if rng.random() < 0.5:
                    edges.add(frozenset({u, v}))
        graph: Graph = (n, edges)
        for k in range(0, n + 1):
            lhs = has_independent_set(graph, k)
            rhs = has_vertex_cover(*reduce_is_to_vc(graph, k))
            if lhs != rhs:
                return False
    return True


if __name__ == "__main__":
    # Triangle K3: IS of size 1 exists (yes), so VC of size n-1 = 2 must exist.
    k3 = (3, {frozenset({0, 1}), frozenset({1, 2}), frozenset({0, 2})})
    assert has_independent_set(k3, 1) is True
    assert has_independent_set(k3, 2) is False
    g, j = reduce_is_to_vc(k3, 1)
    assert (g, j) == (k3, 2)
    assert has_vertex_cover(k3, 2) is True
    assert has_vertex_cover(k3, 1) is False

    # The mapping equivalence holds across random instances and all thresholds
    assert verify_mapping(num_trials=30, n=5, seed=7)
    assert verify_mapping(num_trials=15, n=7, seed=123)

    print("All tests passed!")
