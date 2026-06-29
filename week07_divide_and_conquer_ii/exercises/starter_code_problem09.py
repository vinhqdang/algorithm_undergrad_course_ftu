"""
Problem 09 - Strassen's Matrix Multiplication: 7 vs 8 Mults
==========================================================

The standard recursive 2x2-block matrix multiply uses EIGHT recursive
multiplications: T(n) = 8 T(n/2) -> n^3. Strassen's insight reduces this to
SEVEN: T(n) = 7 T(n/2) -> n^(log2 7) ~ n^2.807.

Implement:
  - `naive_mult_count(n)`: scalar multiplications for the 8-way recurrence
    (base case n=1 costs 1).
  - `strassen_mult_count(n)`: scalar multiplications for the 7-way recurrence
    (base case n=1 costs 1).
  - `strassen_2x2(A, B, counter=None)`: multiply two 2x2 matrices using
    Strassen's seven products; ``tick(7)`` once if a Counter is supplied.

Verify `strassen_2x2` against `naive_2x2` (provided) on random 2x2 matrices.

See practical_exercises.pdf, Problem 9.
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Counter  # noqa: E402

Matrix = List[List[float]]


def naive_mult_count(n: int) -> int:
    """Scalar multiplications used by the standard recursive 2x2 split."""
    # TODO: implement this function.
    raise NotImplementedError


def strassen_mult_count(n: int) -> int:
    """Scalar multiplications used by Strassen's algorithm."""
    # TODO: implement this function.
    raise NotImplementedError


def strassen_2x2(A: Matrix, B: Matrix, counter: Counter | None = None) -> Matrix:
    """Multiply two 2x2 matrices using Strassen's seven products."""
    # TODO: implement this function.
    raise NotImplementedError


def naive_2x2(A: Matrix, B: Matrix) -> Matrix:
    """Standard 2x2 matrix product (the baseline, eight multiplications)."""
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


if __name__ == "__main__":
    try:
        assert naive_mult_count(1) == 1
        assert naive_mult_count(2) == 8
        assert naive_mult_count(4) == 64
        assert naive_mult_count(8) == 512
        assert strassen_mult_count(1) == 1
        assert strassen_mult_count(2) == 7
        assert strassen_mult_count(4) == 49
        assert strassen_mult_count(8) == 343
        for k in range(1, 8):
            n = 2 ** k
            assert strassen_mult_count(n) < naive_mult_count(n)

        rng = random.Random(909)
        for _ in range(500):
            A = [[rng.randint(-9, 9), rng.randint(-9, 9)], [rng.randint(-9, 9), rng.randint(-9, 9)]]
            B = [[rng.randint(-9, 9), rng.randint(-9, 9)], [rng.randint(-9, 9), rng.randint(-9, 9)]]
            c = Counter()
            assert strassen_2x2(A, B, c) == naive_2x2(A, B), (A, B)
            assert c.count == 7

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
