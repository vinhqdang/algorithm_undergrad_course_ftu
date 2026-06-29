"""
Problem 06 - Recursive Radix-2 FFT and Inverse FFT (SOLUTION)
=============================================================
"""

import cmath
import math
import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import next_power_of_two  # noqa: E402


def fft(a: List[complex]) -> List[complex]:
    """Recursive radix-2 Cooley-Tukey FFT.

    Pads ``a`` with zeros up to the next power of two, then returns the DFT
    (a list of complex values) of that padded sequence.
    """
    a = [complex(x) for x in a]
    n = next_power_of_two(len(a))
    a = a + [0j] * (n - len(a))
    return _fft_rec(a, invert=False)


def _fft_rec(a: List[complex], invert: bool) -> List[complex]:
    n = len(a)
    if n == 1:
        return a[:]
    even = _fft_rec(a[0::2], invert)
    odd = _fft_rec(a[1::2], invert)
    sign = 1 if invert else -1
    result = [0j] * n
    for k in range(n // 2):
        w = cmath.exp(sign * 2j * math.pi * k / n)
        t = w * odd[k]
        result[k] = even[k] + t
        result[k + n // 2] = even[k] - t
    return result


def ifft(a: List[complex]) -> List[complex]:
    """Inverse FFT. ``len(a)`` must already be a power of two.

    Returns the inverse DFT (complex values); for a true inverse of ``fft``
    the result is divided by n.
    """
    n = len(a)
    if n & (n - 1) != 0:
        raise ValueError("ifft input length must be a power of two")
    res = _fft_rec([complex(x) for x in a], invert=True)
    return [x / n for x in res]


if __name__ == "__main__":
    # FFT of a constant signal: only the DC (k=0) bin is non-zero.
    out = fft([1, 1, 1, 1])
    assert math.isclose(out[0].real, 4.0, abs_tol=1e-9)
    for k in (1, 2, 3):
        assert abs(out[k]) < 1e-9

    # ifft(fft(x)) == x (after padding) for random signals.
    rng = random.Random(5)
    for _ in range(100):
        n = rng.randint(1, 20)
        x = [rng.uniform(-10, 10) for _ in range(n)]
        m = next_power_of_two(n)
        padded = x + [0.0] * (m - n)
        recovered = ifft(fft(x))
        assert len(recovered) == m
        for orig, got in zip(padded, recovered):
            assert math.isclose(orig, got.real, abs_tol=1e-6)
            assert abs(got.imag) < 1e-6

    # Cross-check against the naive DFT definition on a power-of-two input.
    x = [1, 2, 3, 4]
    naive = [sum(x[t] * cmath.exp(-2j * math.pi * k * t / 4) for t in range(4)) for k in range(4)]
    got = fft(x)
    for a_, b_ in zip(naive, got):
        assert abs(a_ - b_) < 1e-9

    print("All tests passed!")
