"""
Problem 03 - Witness Checkers for O, Omega, and Theta
=======================================================

The formal definitions are:

  - f(n) = O(g(n)) iff there exist c > 0, n0 such that f(n) <= c*g(n)
    for all n >= n0.
  - f(n) = Omega(g(n)) iff there exist c > 0, n0 such that f(n) >= c*g(n)
    for all n >= n0.
  - f(n) = Theta(g(n)) iff f(n) = O(g(n)) and f(n) = Omega(g(n)).

Implement `is_big_o(f, g, c, n0, n_values)` that returns True iff
f(n) <= c * g(n) holds for *every* n in `n_values` with n >= n0 (n < n0 are
ignored -- the definition only requires the bound to hold eventually).

Similarly implement `is_big_omega(f, g, c, n0, n_values)` (f(n) >= c*g(n) for
n >= n0), and `is_theta(f, g, c_lo, c_hi, n0, n_values)` which returns True iff
c_lo * g(n) <= f(n) <= c_hi * g(n) for all n in n_values with n >= n0.

These are *witness checkers*: given proposed constants (c, n0) or (c_lo, c_hi,
n0), they verify the inequality holds on a finite sample of n -- a necessary
(but not sufficient) condition for a full proof, useful for sanity-checking
candidate constants before writing a proof.

See practical_exercises.pdf, Problem 3.
"""

from typing import Callable, List


def is_big_o(f: Callable[[int], float], g: Callable[[int], float], c: float, n0: int, n_values: List[int]) -> bool:
    """Check f(n) <= c*g(n) for all n in n_values with n >= n0."""
    # TODO: implement this function.
    raise NotImplementedError


def is_big_omega(f: Callable[[int], float], g: Callable[[int], float], c: float, n0: int, n_values: List[int]) -> bool:
    """Check f(n) >= c*g(n) for all n in n_values with n >= n0."""
    # TODO: implement this function.
    raise NotImplementedError


def is_theta(f: Callable[[int], float], g: Callable[[int], float], c_lo: float, c_hi: float, n0: int, n_values: List[int]) -> bool:
    """Check c_lo*g(n) <= f(n) <= c_hi*g(n) for all n in n_values with n >= n0."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        n_values = list(range(1, 101))

        # f(n) = 3n^2 + 5n + 2 is Theta(n^2).
        f = lambda n: 3 * n * n + 5 * n + 2
        g = lambda n: n * n

        # Upper bound: 3n^2 + 5n + 2 <= 10*n^2 for n >= 1.
        assert is_big_o(f, g, c=10, n0=1, n_values=n_values)
        # Too small a constant should fail for large n.
        assert not is_big_o(f, g, c=3, n0=1, n_values=n_values)

        # Lower bound: 3n^2 + 5n + 2 >= 3*n^2 for n >= 1 (trivially true,
        # since the other terms are positive).
        assert is_big_omega(f, g, c=3, n0=1, n_values=n_values)
        # Too large a constant should fail for small n.
        assert not is_big_omega(f, g, c=10, n0=1, n_values=n_values)

        # Theta with c_lo=3, c_hi=10 should hold for n >= 1.
        assert is_theta(f, g, c_lo=3, c_hi=10, n0=1, n_values=n_values)

        # n is NOT O(log n): for any constant c, n <= c*log2(n) fails for
        # large n.
        import math
        h = lambda n: n
        log_g = lambda n: math.log2(n) if n > 0 else 0.0
        assert not is_big_o(h, log_g, c=1000, n0=1, n_values=n_values)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
