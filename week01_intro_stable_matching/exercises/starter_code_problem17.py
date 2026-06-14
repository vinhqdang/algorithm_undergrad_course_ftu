"""
Problem 17 - Asymptotic Growth Classification
================================================

You are given a dictionary mapping function names to callables of `n`:

    FUNCTIONS = {
        "constant":    lambda n: 1,
        "logarithmic": lambda n: math.log2(n),
        "sqrt":        lambda n: math.sqrt(n),
        "linear":      lambda n: n,
        "linearithmic":lambda n: n * math.log2(n),
        "quadratic":   lambda n: n ** 2,
        "cubic":       lambda n: n ** 3,
        "exponential": lambda n: 2 ** n,
    }

Implement `order_by_growth(functions, n)` that returns the list of function
names sorted by INCREASING value at the given `n` (i.e. from slowest- to
fastest-growing at that `n`).

Then implement `dominates(f, g, n_values)` that returns True iff, for every
`n` in `n_values` (a list of increasing positive integers), `f(n) <= g(n)`
(i.e. g grows at least as fast as f on this sample of points) -- a simple
empirical proxy for "f is O(g)".

See practical_exercises.pdf, Problem 17.
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
    # TODO: implement.
    raise NotImplementedError


def dominates(f: Callable[[int], float], g: Callable[[int], float], n_values: List[int]) -> bool:
    """Return True iff f(n) <= g(n) for every n in n_values."""
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        order = order_by_growth(FUNCTIONS, n=16)
        expected = ["constant", "logarithmic", "sqrt", "linear", "linearithmic", "quadratic", "cubic", "exponential"]
        assert order == expected, order

        n_values = [2, 4, 8, 16, 32, 64]
        assert dominates(FUNCTIONS["linear"], FUNCTIONS["quadratic"], n_values) is True
        assert dominates(FUNCTIONS["quadratic"], FUNCTIONS["linear"], n_values) is False
        assert dominates(FUNCTIONS["linearithmic"], FUNCTIONS["quadratic"], n_values) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
