"""
Problem 08 - Linear Convolution / Cross-Correlation via FFT
===========================================================

Linear convolution of two integer sequences is exactly polynomial
multiplication, so it can be computed in O(n log n) via FFT.

Implement:
  - `convolve_fft(a, b)`: the linear convolution (delegate to your FFT-based
    polynomial multiplication from Problem 7).
  - `cross_correlation(a, b)`: the cross-correlation, equal to the convolution
    of ``a`` with the reversed ``b``.

Verify both against the direct O(n*m) definitions provided below
(`convolve_direct`, `cross_correlation_direct`).

See practical_exercises.pdf, Problem 8.
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem07 import poly_mul_fft  # noqa: E402


def convolve_direct(a: List[int], b: List[int]) -> List[int]:
    """Linear convolution by the direct definition (the slow baseline)."""
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def cross_correlation_direct(a: List[int], b: List[int]) -> List[int]:
    """Direct-definition cross-correlation (baseline for verification)."""
    return convolve_direct(a, list(reversed(b)))


def convolve_fft(a: List[int], b: List[int]) -> List[int]:
    """Linear convolution of two integer sequences via FFT."""
    # TODO: implement this function.
    raise NotImplementedError


def cross_correlation(a: List[int], b: List[int]) -> List[int]:
    """Cross-correlation of ``a`` and ``b`` via FFT."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert convolve_fft([1, 2, 3], [0, 1, 1]) == convolve_direct([1, 2, 3], [0, 1, 1])
        assert convolve_fft([1, 1, 1], [1, 1, 1]) == [1, 2, 3, 2, 1]

        rng = random.Random(77)
        for _ in range(300):
            a = [rng.randint(-15, 15) for _ in range(rng.randint(1, 12))]
            b = [rng.randint(-15, 15) for _ in range(rng.randint(1, 12))]
            assert convolve_fft(a, b) == convolve_direct(a, b), (a, b)
            assert cross_correlation(a, b) == cross_correlation_direct(a, b), (a, b)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
