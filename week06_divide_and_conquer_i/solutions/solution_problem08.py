"""
Problem 08 - Fast Exponentiation (Exponentiation by Squaring) (SOLUTION)
========================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Optional

from starter_code import Counter


def fast_pow(x: int, n: int, counter: Optional[Counter] = None) -> int:
    """Return x ** n using exponentiation by squaring; count multiplications."""
    if n == 0:
        return 1
    half = fast_pow(x, n // 2, counter)
    result = half * half
    if counter is not None:
        counter.tick()  # one multiplication for the square
    if n % 2 == 1:
        result = result * x
        if counter is not None:
            counter.tick()  # one extra multiplication for the odd case
    return result


if __name__ == "__main__":
    import math

    assert fast_pow(2, 10) == 1024
    assert fast_pow(2, 0) == 1
    assert fast_pow(5, 1) == 5
    assert fast_pow(3, 5) == 243
    assert fast_pow(7, 8) == 7 ** 8
    assert fast_pow(-2, 3) == -8

    for x in range(-3, 4):
        for n in range(0, 20):
            assert fast_pow(x, n) == x ** n

    for n in (16, 100, 1000, 100000):
        c = Counter()
        fast_pow(2, n, c)
        assert c.count <= 2 * (math.floor(math.log2(n)) + 1)

    print("All tests passed!")
