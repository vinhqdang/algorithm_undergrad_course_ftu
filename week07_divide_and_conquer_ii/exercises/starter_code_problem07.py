"""
Problem 07 - Polynomial Multiplication via FFT
==============================================

Implement `poly_mul_fft(a, b)` that multiplies two integer-coefficient
polynomials (low-to-high degree) in O(n log n) using the FFT:

  1. Let L = len(a) + len(b) - 1, and size = next_power_of_two(L).
  2. Zero-pad a and b to length `size`, take their FFTs (Problem 6).
  3. Multiply the two spectra pointwise.
  4. Inverse-FFT the product, then round each of the first L entries to the
     nearest integer (the exact product is integer-valued).

Return ``[]`` if either input is empty. Verify against ``poly_mul_naive``.

See practical_exercises.pdf, Problem 7.
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from starter_code import next_power_of_two, poly_mul_naive  # noqa: E402
from solution_problem06 import fft, ifft  # noqa: E402


def poly_mul_fft(a: List[int], b: List[int]) -> List[int]:
    """Multiply polynomials ``a`` and ``b`` (low-to-high) in O(n log n)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert poly_mul_fft([1, 1], [1, 1]) == [1, 2, 1]
        assert poly_mul_fft([1, 2, 3], [4, 5]) == [4, 13, 22, 15]
        assert poly_mul_fft([], [1, 2]) == []

        rng = random.Random(321)
        for _ in range(300):
            a = [rng.randint(-20, 20) for _ in range(rng.randint(1, 10))]
            b = [rng.randint(-20, 20) for _ in range(rng.randint(1, 10))]
            fast = poly_mul_fft(a, b)
            slow = [int(round(c)) for c in poly_mul_naive(a, b)]
            assert fast == slow, (a, b, fast, slow)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
