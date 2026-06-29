"""
Problem 12 - Fast Modular Exponentiation (Square-and-Multiply)
==============================================================

Implement `power_mod(base, exp, mod, counter=None)` that computes
``(base ** exp) % mod`` in O(log exp) modular multiplications using
square-and-multiply (binary exponentiation):

  result = 1
  while exp > 0:
      if exp is odd: result = result * base % mod
      exp //= 2
      base = base * base % mod   # only when more bits remain

``exp`` must be non-negative and ``mod`` positive. If a ``Counter`` is
supplied, ``tick()`` once per modular multiplication. Verify against Python's
built-in ``pow(base, exp, mod)``.

See practical_exercises.pdf, Problem 12.
"""

import random
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Counter  # noqa: E402


def power_mod(base: int, exp: int, mod: int, counter: Counter | None = None) -> int:
    """Compute (base ** exp) % mod via square-and-multiply in O(log exp)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert power_mod(2, 10, 1000) == 1024 % 1000
        assert power_mod(3, 0, 7) == 1
        assert power_mod(5, 1, 13) == 5
        assert power_mod(7, 100, 1) == 0

        rng = random.Random(1618)
        for _ in range(3000):
            base = rng.randint(0, 10 ** 6)
            exp = rng.randint(0, 5000)
            mod = rng.randint(1, 10 ** 6)
            assert power_mod(base, exp, mod) == pow(base, exp, mod), (base, exp, mod)

        c = Counter()
        power_mod(123, 2 ** 20, 1_000_000_007, c)
        assert c.count <= 2 * 21

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
