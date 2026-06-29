"""
Problem 03 - Independent-Set Verifier and Maximum Independent Set
=================================================================

A graph is (n, edges) where edges is a set of frozenset({u, v}).

Implement:
  - is_independent_set(graph, subset): True iff no two vertices of `subset`
    are joined by an edge.
  - max_independent_set(graph): brute force over all 2**n subsets (largest
    first), returning a maximum independent set as a frozenset.

See practical_exercises.pdf, Problem 3.
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
    # TODO: implement this function.
    raise NotImplementedError


def max_independent_set(graph: Graph) -> FrozenSet[int]:
    """Return a maximum independent set (brute force over all subsets)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g = make_graph(3, [(0, 1), (1, 2), (0, 2)])
        assert is_independent_set(g, []) is True
        assert is_independent_set(g, [0]) is True
        assert is_independent_set(g, [0, 1]) is False
        assert len(max_independent_set(g)) == 1

        p = make_graph(4, [(0, 1), (1, 2), (2, 3)])
        mis = max_independent_set(p)
        assert len(mis) == 2
        assert is_independent_set(p, mis)

        e = make_graph(5, [])
        assert len(max_independent_set(e)) == 5

        c4 = make_graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
        assert len(max_independent_set(c4)) == 2

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
