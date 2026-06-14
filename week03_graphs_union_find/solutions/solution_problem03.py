"""
Problem 03 - Converting Between Adjacency Matrix and Adjacency List (SOLUTION)
================================================================================
"""

import os
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list, edges_to_adjacency_matrix


def matrix_to_adjacency_list(matrix: List[List[int]]) -> List[List[int]]:
    """Convert a 0/1 adjacency matrix to an adjacency list (sorted neighbors)."""
    n = len(matrix)
    adj: List[List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if matrix[u][v]:
                adj[u].append(v)
    return adj


def adjacency_list_to_matrix(adj: List[List[int]]) -> List[List[int]]:
    """Convert an adjacency list to a 0/1 adjacency matrix."""
    n = len(adj)
    matrix = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            matrix[u][v] = 1
    return matrix


def matrix_density(matrix: List[List[int]]) -> float:
    """Return the fraction of possible edges present (upper triangle)."""
    n = len(matrix)
    if n < 2:
        return 0.0
    possible = n * (n - 1) // 2
    present = sum(matrix[u][v] for u in range(n) for v in range(u + 1, n) if matrix[u][v])
    return present / possible


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    matrix = edges_to_adjacency_matrix(4, edges)

    adj = matrix_to_adjacency_list(matrix)
    assert adj == [[1, 3], [0, 2], [1, 3], [0, 2]]

    matrix2 = adjacency_list_to_matrix(adj)
    assert matrix2 == matrix

    assert abs(matrix_density(matrix) - 4 / 6) < 1e-9

    all_edges = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    complete_matrix = edges_to_adjacency_matrix(4, all_edges)
    assert matrix_density(complete_matrix) == 1.0

    empty_matrix = edges_to_adjacency_matrix(4, [])
    assert matrix_density(empty_matrix) == 0.0

    adj_from_helper = edges_to_adjacency_list(4, edges)
    assert matrix_to_adjacency_list(adjacency_list_to_matrix(adj_from_helper)) == adj

    print("All tests passed!")
