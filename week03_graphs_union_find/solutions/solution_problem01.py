"""
Problem 01 - Edge List to Adjacency List/Matrix (SOLUTION)
============================================================
"""

from typing import Iterable, List, Tuple


def edges_to_adjacency_list(n: int, edges: Iterable[Tuple[int, int]], directed: bool = False) -> List[List[int]]:
    """Build an adjacency list of size n from a list of edges."""
    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def edges_to_adjacency_matrix(n: int, edges: Iterable[Tuple[int, int]], directed: bool = False) -> List[List[int]]:
    """Build an n x n adjacency matrix from a list of edges."""
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] += 1
        if not directed and u != v:
            matrix[v][u] += 1
    return matrix


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (0, 2)]
    adj = edges_to_adjacency_list(3, edges)
    assert sorted(adj[0]) == [1, 2]
    assert sorted(adj[1]) == [0, 2]
    assert sorted(adj[2]) == [0, 1]

    mat = edges_to_adjacency_matrix(3, edges)
    assert mat[0][1] == 1 and mat[1][0] == 1
    assert mat[0][2] == 1 and mat[2][0] == 1
    assert mat[1][2] == 1 and mat[2][1] == 1
    assert mat[0][0] == 0

    directed_edges = [(0, 1), (1, 2), (0, 1)]
    adj_d = edges_to_adjacency_list(3, directed_edges, directed=True)
    assert sorted(adj_d[0]) == [1, 1]
    assert adj_d[1] == [2]
    assert adj_d[2] == []

    mat_d = edges_to_adjacency_matrix(3, directed_edges, directed=True)
    assert mat_d[0][1] == 2
    assert mat_d[1][0] == 0
    assert mat_d[1][2] == 1

    self_loop_edges = [(0, 0), (0, 1)]
    adj_sl = edges_to_adjacency_list(2, self_loop_edges)
    assert adj_sl[0].count(0) == 2

    mat_sl = edges_to_adjacency_matrix(2, self_loop_edges)
    assert mat_sl[0][0] == 1

    print("All tests passed!")
