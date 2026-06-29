"""
Problem 04 - Master Theorem Classifier (SOLUTION)
==================================================
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
    crit = math.log(a) / math.log(b)  # log_b(a)
    tol = 1e-9
    if d < crit - tol:
        # Case 1: leaves dominate.
        return f"Theta(n^{format_exponent(crit)})"
    elif abs(d - crit) <= tol:
        # Case 2: every level does equal work.
        return f"Theta(n^{format_exponent(d)} log n)"
    else:
        # Case 3: root dominates.
        return f"Theta(n^{format_exponent(d)})"


if __name__ == "__main__":
    assert master_theorem(2, 2, 1) == "Theta(n^1 log n)"
    assert master_theorem(1, 2, 0) == "Theta(n^0 log n)"
    assert master_theorem(3, 2, 1) == "Theta(n^1.585)"
    assert master_theorem(4, 2, 1) == "Theta(n^2)"
    assert master_theorem(2, 2, 2) == "Theta(n^2)"
    assert master_theorem(9, 3, 1) == "Theta(n^2)"
    assert master_theorem(8, 2, 3) == "Theta(n^3 log n)"

    print("All tests passed!")
