"""
Problem 06 - Recursive Radix-2 FFT and Inverse FFT
==================================================

Implement the recursive radix-2 Cooley-Tukey FFT and its inverse.

`fft(a)`:
  - Pad ``a`` with zeros up to the next power of two.
  - Return the DFT as a list of complex numbers. The recursive step splits the
    input into even- and odd-indexed elements, recurses on each, and combines
    using the roots of unity omega_n^k = exp(-2*pi*i*k/n).

`ifft(a)`:
  - The inverse DFT. ``len(a)`` must be a power of two. Use the same recursion
    with the conjugate root exp(+2*pi*i*k/n), then divide every entry by n, so
    that ``ifft(fft(x))`` recovers ``x`` (after zero-padding).

Use ``cmath``/``math`` (both standard library) and ``next_power_of_two`` from
starter_code.py.

See practical_exercises.pdf, Problem 6.
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
    """Recursive radix-2 FFT (pads to the next power of two)."""
    # TODO: implement this function (a recursive helper is recommended).
    raise NotImplementedError


def ifft(a: List[complex]) -> List[complex]:
    """Inverse FFT; ``len(a)`` must be a power of two."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        out = fft([1, 1, 1, 1])
        assert math.isclose(out[0].real, 4.0, abs_tol=1e-9)
        for k in (1, 2, 3):
            assert abs(out[k]) < 1e-9

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

        x = [1, 2, 3, 4]
        naive = [sum(x[t] * cmath.exp(-2j * math.pi * k * t / 4) for t in range(4)) for k in range(4)]
        got = fft(x)
        for a_, b_ in zip(naive, got):
            assert abs(a_ - b_) < 1e-9

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
