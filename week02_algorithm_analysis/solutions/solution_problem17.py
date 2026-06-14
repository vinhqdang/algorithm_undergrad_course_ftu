"""
Problem 17 - Correctness via Induction: Sum and Power (SOLUTION)
====================================================================
"""

from typing import List, Tuple


def iterative_sum(n: int) -> int:
    """Return 0 + 1 + ... + n (0 if n < 0)."""
    if n < 0:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def fast_power(base: int, exp: int) -> int:
    """Return base ** exp using binary exponentiation, for exp >= 0."""
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base


def verify_sum_invariant(n: int) -> int:
    """Like iterative_sum(n), but asserts the loop invariant total == i*(i+1)//2 at every step."""
    if n < 0:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
        assert total == i * (i + 1) // 2
    return total


def verify_fast_power(values: List[Tuple[int, int]]) -> bool:
    """Check fast_power(base, exp) == base ** exp for every (base, exp) in values."""
    return all(fast_power(base, exp) == base ** exp for base, exp in values)


if __name__ == "__main__":
    assert iterative_sum(0) == 0
    assert iterative_sum(1) == 1
    assert iterative_sum(5) == 15
    assert iterative_sum(100) == 5050
    assert iterative_sum(-3) == 0

    assert fast_power(2, 0) == 1
    assert fast_power(2, 10) == 1024
    assert fast_power(3, 5) == 243
    assert fast_power(5, 1) == 5

    for n in [0, 1, 5, 10, 50]:
        assert verify_sum_invariant(n) == n * (n + 1) // 2

    assert verify_fast_power([(2, 0), (2, 10), (3, 5), (10, 6), (1, 100), (7, 7)])

    print("All tests passed!")
