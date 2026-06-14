"""
Problem 01 - Edge List to Adjacency List/Matrix
=================================================

Implement two graph-representation conversions FROM SCRATCH (without using
the helpers of the same name in starter_code.py -- this is a warm-up
exercise):

  - `edges_to_adjacency_list(n, edges, directed=False)`: return a list of
    length n, where adj[u] is the list of neighbors of u (in the order the
    edges were given). For undirected graphs, each edge (u, v) must appear
    in BOTH adj[u] and adj[v].
  - `edges_to_adjacency_matrix(n, edges, directed=False)`: return an n x n
    matrix (list of lists) where matrix[u][v] is the NUMBER of edges between
    u and v (so parallel edges show up as values > 1).

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

from typing import Iterable, List, Tuple


def edges_to_adjacency_list(n: int, edges: Iterable[Tuple[int, int]], directed: bool = False) -> List[List[int]]:
    """Build an adjacency list of size n from a list of edges."""
    # TODO: implement this function.
    raise NotImplementedError


def edges_to_adjacency_matrix(n: int, edges: Iterable[Tuple[int, int]], directed: bool = False) -> List[List[int]]:
    """Build an n x n adjacency matrix from a list of edges."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Undirected triangle: 0-1, 1-2, 0-2
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

        # Directed path 0 -> 1 -> 2, plus a parallel edge 0 -> 1
        directed_edges = [(0, 1), (1, 2), (0, 1)]
        adj_d = edges_to_adjacency_list(3, directed_edges, directed=True)
        assert sorted(adj_d[0]) == [1, 1]
        assert adj_d[1] == [2]
        assert adj_d[2] == []

        mat_d = edges_to_adjacency_matrix(3, directed_edges, directed=True)
        assert mat_d[0][1] == 2  # parallel edge counted twice
        assert mat_d[1][0] == 0  # not symmetric for directed graphs
        assert mat_d[1][2] == 1

        # Self-loop: 0-0
        self_loop_edges = [(0, 0), (0, 1)]
        adj_sl = edges_to_adjacency_list(2, self_loop_edges)
        assert adj_sl[0].count(0) == 2  # a self-loop appears twice in adj[0]

        mat_sl = edges_to_adjacency_matrix(2, self_loop_edges)
        assert mat_sl[0][0] == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
