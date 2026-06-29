"""
Problem 09 - Strassen's Matrix Multiplication: 7 vs 8 Mults (SOLUTION)
=====================================================================
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Counter  # noqa: E402

Matrix = List[List[float]]


def naive_mult_count(n: int) -> int:
    """Scalar multiplications used by the standard recursive 2x2 split.

    The textbook recurrence is T(n) = 8 T(n/2) with a 1x1 base case costing
    one multiplication, giving T(n) = n^3 for n a power of two.
    """
    if n == 1:
        return 1
    return 8 * naive_mult_count(n // 2)


def strassen_mult_count(n: int) -> int:
    """Scalar multiplications used by Strassen's algorithm.

    The recurrence is T(n) = 7 T(n/2) with a 1x1 base case costing one
    multiplication, giving T(n) = n^(log2 7) = 7^(log2 n) for n a power of two.
    """
    if n == 1:
        return 1
    return 7 * strassen_mult_count(n // 2)


def strassen_2x2(A: Matrix, B: Matrix, counter: Counter | None = None) -> Matrix:
    """Multiply two 2x2 matrices using Strassen's seven products."""
    a, b = A[0]
    c, d = A[1]
    e, f = B[0]
    g, h = B[1]

    if counter is not None:
        counter.tick(7)

    m1 = (a + d) * (e + h)
    m2 = (c + d) * e
    m3 = a * (f - h)
    m4 = d * (g - e)
    m5 = (a + b) * h
    m6 = (c - a) * (e + f)
    m7 = (b - d) * (g + h)

    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6
    return [[c11, c12], [c21, c22]]


def naive_2x2(A: Matrix, B: Matrix) -> Matrix:
    """Standard 2x2 matrix product (the baseline, eight multiplications)."""
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


if __name__ == "__main__":
    # Multiplication counts follow the recurrences.
    assert naive_mult_count(1) == 1
    assert naive_mult_count(2) == 8
    assert naive_mult_count(4) == 64
    assert naive_mult_count(8) == 512  # 8^3
    assert strassen_mult_count(1) == 1
    assert strassen_mult_count(2) == 7
    assert strassen_mult_count(4) == 49
    assert strassen_mult_count(8) == 343  # 7^3
    # Strassen wins for n >= 2.
    for k in range(1, 8):
        n = 2 ** k
        assert strassen_mult_count(n) < naive_mult_count(n)

    # The 2x2 Strassen product matches the naive product, using exactly 7 mults.
    rng = random.Random(909)
    for _ in range(500):
        A = [[rng.randint(-9, 9), rng.randint(-9, 9)], [rng.randint(-9, 9), rng.randint(-9, 9)]]
        B = [[rng.randint(-9, 9), rng.randint(-9, 9)], [rng.randint(-9, 9), rng.randint(-9, 9)]]
        c = Counter()
        assert strassen_2x2(A, B, c) == naive_2x2(A, B), (A, B)
        assert c.count == 7

    print("All tests passed!")
