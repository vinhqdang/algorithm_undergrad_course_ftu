"""
Problem 08 - Hamiltonian Cycle by Backtracking
==============================================

Implement:
  - verify_hamiltonian_cycle(graph, cycle): True iff `cycle` (a list of
    vertices, WITHOUT repeating the start at the end) visits every vertex
    exactly once and consecutive vertices -- including the wrap-around from
    last to first -- are joined by edges.
  - find_hamiltonian_cycle(graph): backtracking search; return a Hamiltonian
    cycle as a list of vertices (starting at vertex 0), or None.

See practical_exercises.pdf, Problem 8.
"""

from typing import FrozenSet, Iterable, List, Optional, Set, Tuple

Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def make_graph(n: int, edge_list: Iterable[Tuple[int, int]]) -> Graph:
    edges: Set[Edge] = set()
    for u, v in edge_list:
        if u != v:
            edges.add(frozenset({u, v}))
    return (n, edges)


def verify_hamiltonian_cycle(graph: Graph, cycle: List[int]) -> bool:
    """Return True iff `cycle` is a valid Hamiltonian cycle of `graph`."""
    # TODO: implement this function.
    raise NotImplementedError


def find_hamiltonian_cycle(graph: Graph) -> Optional[List[int]]:
    """Backtracking search for a Hamiltonian cycle starting at vertex 0."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        c4 = make_graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
        cyc = find_hamiltonian_cycle(c4)
        assert cyc is not None
        assert verify_hamiltonian_cycle(c4, cyc)

        path = make_graph(4, [(0, 1), (1, 2), (2, 3)])
        assert find_hamiltonian_cycle(path) is None

        k4 = make_graph(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
        cyc = find_hamiltonian_cycle(k4)
        assert cyc is not None and verify_hamiltonian_cycle(k4, cyc)

        assert verify_hamiltonian_cycle(c4, [0, 2, 1, 3]) is False
        assert verify_hamiltonian_cycle(c4, [0, 1, 2]) is False

        two = make_graph(6, [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)])
        assert find_hamiltonian_cycle(two) is None

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
