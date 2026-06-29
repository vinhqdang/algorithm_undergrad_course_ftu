"""
Problem 10 - Graph k-Coloring by Backtracking
=============================================

Implement:
  - verify_coloring(graph, coloring): True iff `coloring` (indexed by vertex)
    is proper -- no edge joins two equally-colored vertices.
  - k_coloring(graph, k): backtracking search for a proper coloring with colors
    {0..k-1}; return it as a list (indexed by vertex), or None.

See practical_exercises.pdf, Problem 10.
"""

from typing import Iterable, List, Optional, Sequence, Set, Tuple, FrozenSet

Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def make_graph(n: int, edge_list: Iterable[Tuple[int, int]]) -> Graph:
    edges: Set[Edge] = set()
    for u, v in edge_list:
        if u != v:
            edges.add(frozenset({u, v}))
    return (n, edges)


def verify_coloring(graph: Graph, coloring: Sequence[int]) -> bool:
    """Return True iff `coloring` is a proper coloring of `graph`."""
    # TODO: implement this function.
    raise NotImplementedError


def k_coloring(graph: Graph, k: int) -> Optional[List[int]]:
    """Backtracking search for a proper k-coloring, or None."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        k3 = make_graph(3, [(0, 1), (1, 2), (0, 2)])
        assert k_coloring(k3, 2) is None
        c = k_coloring(k3, 3)
        assert c is not None and verify_coloring(k3, c)

        c4 = make_graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
        c = k_coloring(c4, 2)
        assert c is not None and verify_coloring(c4, c)

        c5 = make_graph(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
        assert k_coloring(c5, 2) is None
        c = k_coloring(c5, 3)
        assert c is not None and verify_coloring(c5, c)

        e = make_graph(4, [])
        c = k_coloring(e, 1)
        assert c is not None and verify_coloring(e, c)

        assert verify_coloring(k3, [0, 0, 1]) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
