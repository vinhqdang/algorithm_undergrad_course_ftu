"""
Problem 12 - Fast Modular Exponentiation (SOLUTION)
===================================================
"""

import random
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Counter  # noqa: E402


def power_mod(base: int, exp: int, mod: int, counter: Counter | None = None) -> int:
    """Compute (base ** exp) % mod via square-and-multiply in O(log exp).

    ``exp`` must be non-negative; ``mod`` must be positive. If a ``Counter`` is
    supplied, ``tick()`` is called once per modular multiplication performed.
    """
    if exp < 0:
        raise ValueError("exponent must be non-negative")
    if mod <= 0:
        raise ValueError("modulus must be positive")
    result = 1 % mod
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
            if counter is not None:
                counter.tick()
        exp >>= 1
        if exp > 0:
            base = (base * base) % mod
            if counter is not None:
                counter.tick()
    return result


if __name__ == "__main__":
    assert power_mod(2, 10, 1000) == 1024 % 1000
    assert power_mod(3, 0, 7) == 1
    assert power_mod(5, 1, 13) == 5
    assert power_mod(7, 100, 1) == 0  # everything is 0 mod 1

    rng = random.Random(1618)
    for _ in range(3000):
        base = rng.randint(0, 10 ** 6)
        exp = rng.randint(0, 5000)
        mod = rng.randint(1, 10 ** 6)
        assert power_mod(base, exp, mod) == pow(base, exp, mod), (base, exp, mod)

    # The number of multiplications is logarithmic in the exponent.
    c = Counter()
    power_mod(123, 2 ** 20, 1_000_000_007, c)
    assert c.count <= 2 * 21

    print("All tests passed!")
