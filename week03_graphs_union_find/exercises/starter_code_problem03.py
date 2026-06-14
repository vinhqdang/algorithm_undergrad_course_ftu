"""
Problem 03 - Converting Between Adjacency Matrix and Adjacency List
=====================================================================

Implement two conversions between the adjacency-matrix and adjacency-list
representations of a SIMPLE undirected graph (no self-loops, no parallel
edges, matrix entries are 0 or 1):

  - `matrix_to_adjacency_list(matrix)`: given an n x n 0/1 matrix, return the
    adjacency list (list of length n, adj[v] sorted in increasing order).
  - `adjacency_list_to_matrix(adj)`: given an adjacency list, return the
    corresponding n x n 0/1 matrix.

Also implement `matrix_density(matrix)`, returning the fraction of possible
edges that are present: `(number of 1-entries in the upper triangle) /
(n * (n-1) / 2)`, as a float. This illustrates the space trade-off between
the two representations: an adjacency matrix uses Theta(n^2) space
regardless of density, while an adjacency list uses Theta(n + m) space,
which is much smaller for sparse graphs (low density).

See practical_exercises.pdf, Problem 3.
"""

import os
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list, edges_to_adjacency_matrix


def matrix_to_adjacency_list(matrix: List[List[int]]) -> List[List[int]]:
    """Convert a 0/1 adjacency matrix to an adjacency list (sorted neighbors)."""
    # TODO: implement this function.
    raise NotImplementedError


def adjacency_list_to_matrix(adj: List[List[int]]) -> List[List[int]]:
    """Convert an adjacency list to a 0/1 adjacency matrix."""
    # TODO: implement this function.
    raise NotImplementedError


def matrix_density(matrix: List[List[int]]) -> float:
    """Return the fraction of possible edges present (upper triangle)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Square graph: 0-1, 1-2, 2-3, 3-0
        edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
        matrix = edges_to_adjacency_matrix(4, edges)

        adj = matrix_to_adjacency_list(matrix)
        assert adj == [[1, 3], [0, 2], [1, 3], [0, 2]]

        matrix2 = adjacency_list_to_matrix(adj)
        assert matrix2 == matrix

        # n=4, possible edges = 6, present = 4 -> density = 4/6
        assert abs(matrix_density(matrix) - 4 / 6) < 1e-9

        # Complete graph K4: density should be 1.0
        all_edges = [(i, j) for i in range(4) for j in range(i + 1, 4)]
        complete_matrix = edges_to_adjacency_matrix(4, all_edges)
        assert matrix_density(complete_matrix) == 1.0

        # Empty graph: density should be 0.0
        empty_matrix = edges_to_adjacency_matrix(4, [])
        assert matrix_density(empty_matrix) == 0.0

        # Round-trip via edges_to_adjacency_list too
        adj_from_helper = edges_to_adjacency_list(4, edges)
        assert matrix_to_adjacency_list(adjacency_list_to_matrix(adj_from_helper)) == adj

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
