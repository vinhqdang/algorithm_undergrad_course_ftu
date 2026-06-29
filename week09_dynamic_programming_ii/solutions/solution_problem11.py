"""
Problem 11 - Matrix Chain Multiplication (SOLUTION)
====================================================
"""

from typing import List, Tuple


def matrix_chain(dims: List[int]) -> Tuple[int, str]:
    """Return (min_cost, parenthesization) for the matrix chain with given dims.

    dims has length n+1; matrix A_i is dims[i-1] x dims[i] for i = 1..n.
    """
    n = len(dims) - 1
    if n == 1:
        return 0, "A1"
    # m[i][j] = min cost to multiply A_i..A_j (1-indexed); split[i][j] = best k
    INF = float("inf")
    m = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = INF
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    split[i][j] = k

    def build(i: int, j: int) -> str:
        if i == j:
            return f"A{i}"
        k = split[i][j]
        return "(" + build(i, k) + build(k + 1, j) + ")"

    return m[1][n], build(1, n)


if __name__ == "__main__":
    cost, paren = matrix_chain([10, 30, 5, 60])
    assert cost == 4500, cost
    assert paren == "((A1A2)A3)", paren

    # Classic CLRS example: dims 30,35,15,5,10,20,25 -> 15125
    cost, paren = matrix_chain([30, 35, 15, 5, 10, 20, 25])
    assert cost == 15125, cost
    assert paren == "((A1(A2A3))((A4A5)A6))", paren

    # Single matrix
    assert matrix_chain([10, 20]) == (0, "A1")

    # Two matrices
    assert matrix_chain([10, 20, 30]) == (6000, "(A1A2)")

    print("All tests passed!")
