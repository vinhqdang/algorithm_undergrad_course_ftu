"""
Problem 05 - Naive Polynomial Multiplication (SOLUTION)
=======================================================
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import poly_eval  # noqa: E402


def poly_mul_naive(a: List[float], b: List[float]) -> List[float]:
    """Coefficient convolution in O(n*m): (a * b)[k] = sum_{i+j=k} a[i] b[j].

    Coefficient lists are low-to-high degree. The product of an n-term and an
    m-term polynomial has n + m - 1 coefficients (or 0 if either is empty).
    """
    if not a or not b:
        return []
    result = [0.0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


if __name__ == "__main__":
    # (1 + x)(1 + x) = 1 + 2x + x^2
    assert poly_mul_naive([1, 1], [1, 1]) == [1, 2, 1]

    # (1 + 2x + 3x^2)(4 + 5x) = 4 + 13x + 22x^2 + 15x^3
    assert poly_mul_naive([1, 2, 3], [4, 5]) == [4, 13, 22, 15]

    # Empty operands.
    assert poly_mul_naive([], [1, 2]) == []

    # The product evaluates correctly at several points (since p*q at x equals
    # p(x) * q(x)).
    rng = random.Random(11)
    for _ in range(200):
        a = [rng.randint(-5, 5) for _ in range(rng.randint(1, 6))]
        b = [rng.randint(-5, 5) for _ in range(rng.randint(1, 6))]
        prod = poly_mul_naive(a, b)
        for x in (-2, -1, 0, 1, 2, 3):
            assert poly_eval(prod, x) == poly_eval(a, x) * poly_eval(b, x)

    print("All tests passed!")
