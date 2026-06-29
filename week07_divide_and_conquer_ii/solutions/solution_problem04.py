"""
Problem 04 - Karatsuba Integer Multiplication (SOLUTION)
========================================================
"""

import random
import sys
import os
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Counter  # noqa: E402


def karatsuba(x: int, y: int, counter: Optional[Counter] = None) -> int:
    """Multiply two non-negative integers using Karatsuba's algorithm.

    Performs three recursive multiplications per level (not four). If a
    ``Counter`` is supplied, ``tick()`` is called once per base-case
    single-"digit" multiplication.
    """
    if x < 0 or y < 0:
        raise ValueError("inputs must be non-negative")

    # Base case: small numbers multiplied directly.
    if x < 10 or y < 10:
        if counter is not None:
            counter.tick()
        return x * y

    # Split each number into high and low halves in base 10.
    m = max(len(str(x)), len(str(y)))
    half = m // 2
    base = 10 ** half

    x_high, x_low = divmod(x, base)
    y_high, y_low = divmod(y, base)

    # Three recursive multiplications.
    z0 = karatsuba(x_low, y_low, counter)
    z2 = karatsuba(x_high, y_high, counter)
    z1 = karatsuba(x_low + x_high, y_low + y_high, counter) - z0 - z2

    return z2 * base * base + z1 * base + z0


if __name__ == "__main__":
    assert karatsuba(0, 0) == 0
    assert karatsuba(7, 6) == 42
    assert karatsuba(1234, 5678) == 1234 * 5678
    assert karatsuba(99999, 99999) == 99999 * 99999

    rng = random.Random(2024)
    for _ in range(300):
        a = rng.randint(0, 10 ** rng.randint(1, 40))
        b = rng.randint(0, 10 ** rng.randint(1, 40))
        assert karatsuba(a, b) == a * b, (a, b)

    # The counter confirms only base-case multiplications are charged, and the
    # result is unaffected by instrumentation.
    c = Counter()
    assert karatsuba(31415926, 27182818, c) == 31415926 * 27182818
    assert c.count > 0

    print("All tests passed!")
