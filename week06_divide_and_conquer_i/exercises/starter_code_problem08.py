"""
Problem 08 - Fast Exponentiation (Exponentiation by Squaring)
==============================================================

Implement `fast_pow(x, n, counter=None)`: compute x ** n for an integer base x
and non-negative integer exponent n, using exponentiation by squaring. If a
`Counter` (from starter_code.py) is passed, call `counter.tick()` once per
integer multiplication, so the total is Theta(log n) (at most ~ 2 log2 n).

Use the identity:
    x^0 = 1
    x^n = (x^(n/2))^2            if n is even
    x^n = x * (x^((n-1)/2))^2    if n is odd
computing x^(n/2) ONCE and squaring it.

See practical_exercises.pdf, Problem 8.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Optional

from starter_code import Counter


def fast_pow(x: int, n: int, counter: Optional[Counter] = None) -> int:
    """Return x ** n using exponentiation by squaring; count multiplications."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    import math

    try:
        assert fast_pow(2, 10) == 1024
        assert fast_pow(2, 0) == 1
        assert fast_pow(5, 1) == 5
        assert fast_pow(3, 5) == 243
        assert fast_pow(7, 8) == 7 ** 8
        assert fast_pow(-2, 3) == -8

        for x in range(-3, 4):
            for n in range(0, 20):
                assert fast_pow(x, n) == x ** n

        # Multiplication count is O(log n): bounded by ~ 2 * log2(n).
        for n in (16, 100, 1000, 100000):
            c = Counter()
            fast_pow(2, n, c)
            assert c.count <= 2 * (math.floor(math.log2(n)) + 1)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
