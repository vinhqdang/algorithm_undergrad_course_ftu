"""
Problem 04 - Karatsuba Integer Multiplication
=============================================

Implement `karatsuba(x, y, counter=None)` that multiplies two non-negative
integers using Karatsuba's algorithm with only THREE recursive
multiplications per level (not four):

  Split x = x_high * B + x_low and y = y_high * B + y_low (B = 10^half).
  z0 = karatsuba(x_low,  y_low)
  z2 = karatsuba(x_high, y_high)
  z1 = karatsuba(x_low + x_high, y_low + y_high) - z0 - z2
  return z2 * B^2 + z1 * B + z0

Use a small base case (multiply directly when either operand is a single
digit). If a ``Counter`` is supplied, ``tick()`` once per base-case
multiplication. Raise ``ValueError`` on negative inputs.

See practical_exercises.pdf, Problem 4.
"""

import random
import sys
import os
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Counter  # noqa: E402


def karatsuba(x: int, y: int, counter: Optional[Counter] = None) -> int:
    """Multiply two non-negative integers using Karatsuba's algorithm."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert karatsuba(0, 0) == 0
        assert karatsuba(7, 6) == 42
        assert karatsuba(1234, 5678) == 1234 * 5678
        assert karatsuba(99999, 99999) == 99999 * 99999

        rng = random.Random(2024)
        for _ in range(300):
            a = rng.randint(0, 10 ** rng.randint(1, 40))
            b = rng.randint(0, 10 ** rng.randint(1, 40))
            assert karatsuba(a, b) == a * b, (a, b)

        c = Counter()
        assert karatsuba(31415926, 27182818, c) == 31415926 * 27182818
        assert c.count > 0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
