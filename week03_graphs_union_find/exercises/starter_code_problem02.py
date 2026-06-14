"""
Problem 02 - Degrees, Self-Loops, and Multi-Edges
===================================================

Given an undirected graph as an edge list, implement:

  - `degree_sequence(n, edges)`: return a list `deg` of length n where
    `deg[v]` is the degree of vertex v. A self-loop (u, u) contributes 2 to
    deg[u] (the standard convention so that the Handshake Lemma
    sum(deg) == 2 * |edges| holds even with self-loops).
  - `has_self_loop(edges)`: return True iff some edge (u, u) is present.
  - `has_multi_edge(edges)`: return True iff some unordered pair {u, v}
    (u != v) appears more than once in `edges`.
  - `handshake_check(n, edges)`: return True iff sum(degree_sequence(n,
    edges)) == 2 * len(edges) (a sanity check / illustration of the
    Handshake Lemma).

See practical_exercises.pdf, Problem 2.
"""

from typing import Iterable, List, Tuple


def degree_sequence(n: int, edges: Iterable[Tuple[int, int]]) -> List[int]:
    """Return the degree of each vertex 0..n-1."""
    # TODO: implement this function.
    raise NotImplementedError


def has_self_loop(edges: Iterable[Tuple[int, int]]) -> bool:
    """Return True iff some edge is a self-loop (u, u)."""
    # TODO: implement this function.
    raise NotImplementedError


def has_multi_edge(edges: Iterable[Tuple[int, int]]) -> bool:
    """Return True iff some pair of vertices is connected by more than one edge."""
    # TODO: implement this function.
    raise NotImplementedError


def handshake_check(n: int, edges: Iterable[Tuple[int, int]]) -> bool:
    """Return True iff sum of degrees == 2 * number of edges."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Simple path 0-1-2-3
        edges = [(0, 1), (1, 2), (2, 3)]
        assert degree_sequence(4, edges) == [1, 2, 2, 1]
        assert has_self_loop(edges) is False
        assert has_multi_edge(edges) is False
        assert handshake_check(4, edges) is True

        # Graph with a self-loop and a multi-edge
        edges2 = [(0, 0), (0, 1), (0, 1), (1, 2)]
        # vertex 0: self-loop contributes 2, plus 2 edges to vertex 1 -> deg 4
        # vertex 1: 2 edges to 0, 1 edge to 2 -> deg 3
        # vertex 2: 1 edge to 1 -> deg 1
        assert degree_sequence(3, edges2) == [4, 3, 1]
        assert has_self_loop(edges2) is True
        assert has_multi_edge(edges2) is True
        assert handshake_check(3, edges2) is True

        # Isolated vertex
        edges3 = [(0, 1)]
        assert degree_sequence(3, edges3) == [1, 1, 0]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
