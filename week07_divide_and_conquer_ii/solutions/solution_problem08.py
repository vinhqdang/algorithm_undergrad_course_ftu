"""
Problem 08 - Linear Convolution / Cross-Correlation via FFT (SOLUTION)
=====================================================================
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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


def convolve_fft(a: List[int], b: List[int]) -> List[int]:
    """Linear convolution of two integer sequences via FFT.

    Linear convolution is exactly polynomial multiplication, so this delegates
    to ``poly_mul_fft``.
    """
    return poly_mul_fft(a, b)


def cross_correlation(a: List[int], b: List[int]) -> List[int]:
    """Cross-correlation of ``a`` and ``b`` via FFT.

    Cross-correlation is the convolution of ``a`` with the reversed ``b``;
    output index k = sum_i a[i] * b[i - k] over the valid range.
    """
    return convolve_fft(a, list(reversed(b)))


def cross_correlation_direct(a: List[int], b: List[int]) -> List[int]:
    """Direct-definition cross-correlation (baseline for verification)."""
    return convolve_direct(a, list(reversed(b)))


if __name__ == "__main__":
    # Convolution matches the direct definition.
    assert convolve_fft([1, 2, 3], [0, 1, 1]) == convolve_direct([1, 2, 3], [0, 1, 1])
    assert convolve_fft([1, 1, 1], [1, 1, 1]) == [1, 2, 3, 2, 1]

    rng = random.Random(77)
    for _ in range(300):
        a = [rng.randint(-15, 15) for _ in range(rng.randint(1, 12))]
        b = [rng.randint(-15, 15) for _ in range(rng.randint(1, 12))]
        assert convolve_fft(a, b) == convolve_direct(a, b), (a, b)
        assert cross_correlation(a, b) == cross_correlation_direct(a, b), (a, b)

    print("All tests passed!")
