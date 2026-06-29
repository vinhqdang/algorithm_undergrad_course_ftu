"""
Problem 04 - Master Theorem Classifier
=======================================

Implement `master_theorem(a, b, d)`: for the recurrence
    T(n) = a * T(n / b) + Theta(n^d)
(with a >= 1, b > 1, d >= 0), return a string naming the Theta-class, by
comparing d with log_b(a):

  - d < log_b(a)  (Case 1): "Theta(n^{e})"      where e = log_b(a), rounded to 3 dp
  - d == log_b(a) (Case 2): "Theta(n^{d} log n)" where d is rounded to 3 dp
  - d > log_b(a)  (Case 3): "Theta(n^{d})"       where d is rounded to 3 dp

Use a tolerance of 1e-9 when comparing d to log_b(a). Format exponents with
`format_exponent` (provided) so that whole numbers print without a trailing
".0" mess -- e.g. 1.0 -> "1", 1.5849625 -> "1.585".

See practical_exercises.pdf, Problem 4.
"""

import math


def format_exponent(value: float) -> str:
    """Format an exponent: integers as "2", non-integers rounded to 3 dp."""
    rounded = round(value, 3)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    return f"{rounded:g}"


def master_theorem(a: float, b: float, d: float) -> str:
    """Return the Theta-class string for T(n) = a T(n/b) + Theta(n^d)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Mergesort: 2 T(n/2) + Theta(n), log_2(2) = 1 = d -> Case 2.
        assert master_theorem(2, 2, 1) == "Theta(n^1 log n)"
        # Binary search: T(n/2) + Theta(1), log_2(1) = 0 = d -> Case 2.
        assert master_theorem(1, 2, 0) == "Theta(n^0 log n)"
        # Karatsuba: 3 T(n/2) + Theta(n), log_2(3) ~ 1.585 > 1 -> Case 1.
        assert master_theorem(3, 2, 1) == "Theta(n^1.585)"
        # Grade-school D&C: 4 T(n/2) + Theta(n), log_2(4) = 2 > 1 -> Case 1.
        assert master_theorem(4, 2, 1) == "Theta(n^2)"
        # Root-dominated: 2 T(n/2) + Theta(n^2), log_2(2) = 1 < 2 -> Case 3.
        assert master_theorem(2, 2, 2) == "Theta(n^2)"
        # 9 T(n/3) + Theta(n), log_3(9) = 2 > 1 -> Case 1.
        assert master_theorem(9, 3, 1) == "Theta(n^2)"
        # 8 T(n/2) + Theta(n^3), log_2(8) = 3 = d -> Case 2.
        assert master_theorem(8, 2, 3) == "Theta(n^3 log n)"

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
