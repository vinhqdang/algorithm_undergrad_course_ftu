"""
Problem 07 - Polynomial Multiplication via FFT (SOLUTION)
=========================================================
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter_code import next_power_of_two, poly_mul_naive  # noqa: E402
from solution_problem06 import fft, ifft  # noqa: E402


def poly_mul_fft(a: List[int], b: List[int]) -> List[int]:
    """Multiply polynomials ``a`` and ``b`` (low-to-high) in O(n log n).

    Evaluate both at the same roots of unity via FFT, multiply pointwise,
    interpolate via inverse FFT, and round to the nearest integer (inputs are
    assumed integer-valued, so the exact product is integer).
    """
    if not a or not b:
        return []
    result_len = len(a) + len(b) - 1
    size = next_power_of_two(result_len)

    fa = fft(a + [0] * (size - len(a)))
    fb = fft(b + [0] * (size - len(b)))
    fc = [x * y for x, y in zip(fa, fb)]
    c = ifft(fc)
    return [int(round(c[i].real)) for i in range(result_len)]


if __name__ == "__main__":
    assert poly_mul_fft([1, 1], [1, 1]) == [1, 2, 1]
    assert poly_mul_fft([1, 2, 3], [4, 5]) == [4, 13, 22, 15]
    assert poly_mul_fft([], [1, 2]) == []

    # Agreement with the naive multiplication on many random instances.
    rng = random.Random(321)
    for _ in range(300):
        a = [rng.randint(-20, 20) for _ in range(rng.randint(1, 10))]
        b = [rng.randint(-20, 20) for _ in range(rng.randint(1, 10))]
        fast = poly_mul_fft(a, b)
        slow = [int(round(c)) for c in poly_mul_naive(a, b)]
        assert fast == slow, (a, b, fast, slow)

    print("All tests passed!")
