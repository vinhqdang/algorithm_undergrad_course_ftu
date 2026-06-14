"""
Problem 15 - Karatsuba Multiplication
=======================================

Implement `karatsuba(x, y)`, multiplying two non-negative integers using the
Karatsuba divide-and-conquer algorithm:

  Given x, y with m digits each, split x = a*10^(m/2) + b and
  y = c*10^(m/2) + d. Then:
      ac = a * c
      bd = b * d
      ad_plus_bc = (a + b) * (c + d) - ac - bd     (3 multiplications instead of 4)
      x * y = ac * 10^m + ad_plus_bc * 10^(m/2) + bd

  Base case: if x < 10 or y < 10, return x * y directly.

Also implement `naive_multiply_op_count(x, y)` that returns the number of
single-digit multiplications a grade-school algorithm would need:
roughly `len(str(x)) * len(str(y))`.

See practical_exercises.pdf, Problem 15.
"""


def karatsuba(x: int, y: int) -> int:
    """Multiply two non-negative integers using Karatsuba's algorithm."""
    # TODO: implement.
    raise NotImplementedError


def naive_multiply_op_count(x: int, y: int) -> int:
    """Number of single-digit multiplications grade-school multiplication needs."""
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        import random

        rng = random.Random(0)
        for _ in range(50):
            x = rng.randint(0, 10**6)
            y = rng.randint(0, 10**6)
            assert karatsuba(x, y) == x * y, (x, y)

        assert karatsuba(0, 12345) == 0
        assert karatsuba(5, 7) == 35
        assert karatsuba(1234, 5678) == 1234 * 5678

        assert naive_multiply_op_count(1234, 5678) == 16  # 4 digits * 4 digits
        assert naive_multiply_op_count(12, 345) == 6      # 2 digits * 3 digits

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
