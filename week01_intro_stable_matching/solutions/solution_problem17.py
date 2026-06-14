"""
Problem 17 - Asymptotic Growth Classification (SOLUTION)
===========================================================
"""

import math
from typing import Callable, Dict, List


FUNCTIONS: Dict[str, Callable[[int], float]] = {
    "constant": lambda n: 1,
    "logarithmic": lambda n: math.log2(n),
    "sqrt": lambda n: math.sqrt(n),
    "linear": lambda n: n,
    "linearithmic": lambda n: n * math.log2(n),
    "quadratic": lambda n: n ** 2,
    "cubic": lambda n: n ** 3,
    "exponential": lambda n: 2 ** n,
}


def order_by_growth(functions: Dict[str, Callable[[int], float]], n: int) -> List[str]:
    """Return function names sorted by increasing value at `n`."""
    return sorted(functions, key=lambda name: functions[name](n))


def dominates(f: Callable[[int], float], g: Callable[[int], float], n_values: List[int]) -> bool:
    """Return True iff f(n) <= g(n) for every n in n_values."""
    return all(f(n) <= g(n) for n in n_values)


if __name__ == "__main__":
    order = order_by_growth(FUNCTIONS, n=16)
    expected = ["constant", "logarithmic", "sqrt", "linear", "linearithmic", "quadratic", "cubic", "exponential"]
    assert order == expected, order

    n_values = [2, 4, 8, 16, 32, 64]
    assert dominates(FUNCTIONS["linear"], FUNCTIONS["quadratic"], n_values) is True
    assert dominates(FUNCTIONS["quadratic"], FUNCTIONS["linear"], n_values) is False
    assert dominates(FUNCTIONS["linearithmic"], FUNCTIONS["quadratic"], n_values) is True

    print("All tests passed!")
