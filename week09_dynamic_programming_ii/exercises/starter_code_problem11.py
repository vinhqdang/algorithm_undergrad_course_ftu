"""
Problem 11 - Matrix Chain Multiplication
=========================================

Given dimensions `dims` (a list of length n+1, so matrix A_i is dims[i-1] by
dims[i] for i = 1..n), implement `matrix_chain(dims)` returning
(min_cost, parenthesization) where `min_cost` is the minimum number of scalar
multiplications and `parenthesization` is a string such as "((A1A2)A3)" describing
one optimal order. Use the interval DP

    M(i, j) = min over i <= k < j of  M(i, k) + M(k+1, j) + dims[i-1]*dims[k]*dims[j],

storing the optimal split point to reconstruct the parenthesisation.

See practical_exercises.pdf, Problem 11, for the full statement and examples.
"""

from typing import List, Tuple


def matrix_chain(dims: List[int]) -> Tuple[int, str]:
    """Return (min_cost, parenthesization) for the matrix chain with given dims."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        cost, paren = matrix_chain([10, 30, 5, 60])
        assert cost == 4500, cost
        assert paren == "((A1A2)A3)", paren

        cost, paren = matrix_chain([30, 35, 15, 5, 10, 20, 25])
        assert cost == 15125, cost
        assert paren == "((A1(A2A3))((A4A5)A6))", paren

        assert matrix_chain([10, 20]) == (0, "A1")
        assert matrix_chain([10, 20, 30]) == (6000, "(A1A2)")

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
