"""
Problem 02 - Degrees, Self-Loops, and Multi-Edges (SOLUTION)
==============================================================
"""

from collections import Counter
from typing import Iterable, List, Tuple


def degree_sequence(n: int, edges: Iterable[Tuple[int, int]]) -> List[int]:
    """Return the degree of each vertex 0..n-1."""
    deg = [0] * n
    for u, v in edges:
        if u == v:
            deg[u] += 2
        else:
            deg[u] += 1
            deg[v] += 1
    return deg


def has_self_loop(edges: Iterable[Tuple[int, int]]) -> bool:
    """Return True iff some edge is a self-loop (u, u)."""
    return any(u == v for u, v in edges)


def has_multi_edge(edges: Iterable[Tuple[int, int]]) -> bool:
    """Return True iff some pair of vertices is connected by more than one edge."""
    counts = Counter(frozenset((u, v)) if u != v else (u, v) for u, v in edges)
    # Only count non-self-loop pairs for "multi-edge" purposes.
    for pair, cnt in counts.items():
        if isinstance(pair, frozenset) and cnt > 1:
            return True
    return False


def handshake_check(n: int, edges: Iterable[Tuple[int, int]]) -> bool:
    """Return True iff sum of degrees == 2 * number of edges."""
    edges = list(edges)
    return sum(degree_sequence(n, edges)) == 2 * len(edges)


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 3)]
    assert degree_sequence(4, edges) == [1, 2, 2, 1]
    assert has_self_loop(edges) is False
    assert has_multi_edge(edges) is False
    assert handshake_check(4, edges) is True

    edges2 = [(0, 0), (0, 1), (0, 1), (1, 2)]
    assert degree_sequence(3, edges2) == [4, 3, 1]
    assert has_self_loop(edges2) is True
    assert has_multi_edge(edges2) is True
    assert handshake_check(3, edges2) is True

    edges3 = [(0, 1)]
    assert degree_sequence(3, edges3) == [1, 1, 0]

    print("All tests passed!")
