"""
Problem 03 - Witness Checkers for O, Omega, and Theta (SOLUTION)
===================================================================
"""

from typing import Callable, List


def is_big_o(f: Callable[[int], float], g: Callable[[int], float], c: float, n0: int, n_values: List[int]) -> bool:
    """Check f(n) <= c*g(n) for all n in n_values with n >= n0."""
    return all(f(n) <= c * g(n) for n in n_values if n >= n0)


def is_big_omega(f: Callable[[int], float], g: Callable[[int], float], c: float, n0: int, n_values: List[int]) -> bool:
    """Check f(n) >= c*g(n) for all n in n_values with n >= n0."""
    return all(f(n) >= c * g(n) for n in n_values if n >= n0)


def is_theta(f: Callable[[int], float], g: Callable[[int], float], c_lo: float, c_hi: float, n0: int, n_values: List[int]) -> bool:
    """Check c_lo*g(n) <= f(n) <= c_hi*g(n) for all n in n_values with n >= n0."""
    return all(c_lo * g(n) <= f(n) <= c_hi * g(n) for n in n_values if n >= n0)


if __name__ == "__main__":
    n_values = list(range(1, 101))

    f = lambda n: 3 * n * n + 5 * n + 2
    g = lambda n: n * n

    assert is_big_o(f, g, c=10, n0=1, n_values=n_values)
    assert not is_big_o(f, g, c=3, n0=1, n_values=n_values)

    assert is_big_omega(f, g, c=3, n0=1, n_values=n_values)
    assert not is_big_omega(f, g, c=10, n0=1, n_values=n_values)

    assert is_theta(f, g, c_lo=3, c_hi=10, n0=1, n_values=n_values)

    import math
    h = lambda n: n
    log_g = lambda n: math.log2(n) if n > 0 else 0.0
    assert not is_big_o(h, log_g, c=1000, n0=1, n_values=n_values)

    print("All tests passed!")
