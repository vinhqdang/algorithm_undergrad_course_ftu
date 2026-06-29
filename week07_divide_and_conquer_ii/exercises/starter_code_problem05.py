"""
Problem 05 - Naive Polynomial Multiplication (Coefficient Convolution)
=====================================================================

Implement `poly_mul_naive(a, b)` that multiplies two polynomials given as
coefficient lists in increasing degree order (``[a0, a1, a2, ...]`` means
``a0 + a1*x + a2*x^2 + ...``), in O(n*m) using the convolution formula:

    (a * b)[k] = sum over i + j = k of a[i] * b[j].

The product of an n-term and an m-term polynomial has n + m - 1 coefficients;
return ``[]`` if either input is empty. Use ``poly_eval`` from starter_code.py
in your own testing if you like.

See practical_exercises.pdf, Problem 5.
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import poly_eval  # noqa: E402


def poly_mul_naive(a: List[float], b: List[float]) -> List[float]:
    """Coefficient convolution in O(n*m)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert poly_mul_naive([1, 1], [1, 1]) == [1, 2, 1]
        assert poly_mul_naive([1, 2, 3], [4, 5]) == [4, 13, 22, 15]
        assert poly_mul_naive([], [1, 2]) == []

        rng = random.Random(11)
        for _ in range(200):
            a = [rng.randint(-5, 5) for _ in range(rng.randint(1, 6))]
            b = [rng.randint(-5, 5) for _ in range(rng.randint(1, 6))]
            prod = poly_mul_naive(a, b)
            for x in (-2, -1, 0, 1, 2, 3):
                assert poly_eval(prod, x) == poly_eval(a, x) * poly_eval(b, x)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
