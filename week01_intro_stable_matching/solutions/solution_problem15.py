"""
Problem 15 - Karatsuba Multiplication (SOLUTION)
===================================================
"""


def karatsuba(x: int, y: int) -> int:
    """Multiply two non-negative integers using Karatsuba's algorithm."""
    if x < 10 or y < 10:
        return x * y

    m = max(len(str(x)), len(str(y)))
    m_half = m // 2

    high_x, low_x = divmod(x, 10 ** m_half)
    high_y, low_y = divmod(y, 10 ** m_half)

    z0 = karatsuba(low_x, low_y)
    z2 = karatsuba(high_x, high_y)
    z1 = karatsuba(low_x + high_x, low_y + high_y) - z2 - z0

    return z2 * 10 ** (2 * m_half) + z1 * 10 ** m_half + z0


def naive_multiply_op_count(x: int, y: int) -> int:
    """Number of single-digit multiplications grade-school multiplication needs."""
    return len(str(x)) * len(str(y))


if __name__ == "__main__":
    import random

    rng = random.Random(0)
    for _ in range(50):
        x = rng.randint(0, 10**6)
        y = rng.randint(0, 10**6)
        assert karatsuba(x, y) == x * y, (x, y)

    assert karatsuba(0, 12345) == 0
    assert karatsuba(5, 7) == 35
    assert karatsuba(1234, 5678) == 1234 * 5678

    assert naive_multiply_op_count(1234, 5678) == 16
    assert naive_multiply_op_count(12, 345) == 6

    print("All tests passed!")
