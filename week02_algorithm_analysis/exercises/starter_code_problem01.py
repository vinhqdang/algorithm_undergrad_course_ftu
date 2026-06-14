"""
Problem 01 - Ordering Functions by Growth Rate
================================================

Implement `order_by_growth(functions, n)` that takes a dict mapping names to
callables of n (see `GROWTH_FUNCTIONS` in starter_code.py) and returns the
list of names sorted by *increasing* value at the given n (slowest- to
fastest-growing, at that particular n).

Then implement `dominates(f, g, n_values)` that returns True iff, for every n
in `n_values` (an increasing list of positive integers), f(n) <= g(n). This is
a simple empirical proxy for "f is O(g)" (it does not prove it, but a
violation immediately disproves it).

See practical_exercises.pdf, Problem 1.
"""

import os
import sys
from typing import Callable, Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import GROWTH_FUNCTIONS


def order_by_growth(functions: Dict[str, Callable[[int], float]], n: int) -> List[str]:
    """Return the names in `functions`, sorted by increasing value at n."""
    # TODO: implement this function.
    raise NotImplementedError


def dominates(f: Callable[[int], float], g: Callable[[int], float], n_values: List[int]) -> bool:
    """Return True iff f(n) <= g(n) for every n in n_values."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        order_small = order_by_growth(GROWTH_FUNCTIONS, n=2)
        order_large = order_by_growth(GROWTH_FUNCTIONS, n=512)

        # At large n, the textbook hierarchy should hold exactly.
        expected_large = [
            "constant", "logarithmic", "sqrt", "linear",
            "linearithmic", "quadratic", "cubic", "exponential",
        ]
        assert order_large == expected_large, order_large

        # constant and logarithmic functions are dominated by linear ones.
        n_values = [1, 2, 4, 8, 16, 32, 64, 128]
        assert dominates(GROWTH_FUNCTIONS["logarithmic"], GROWTH_FUNCTIONS["linear"], n_values)
        assert dominates(GROWTH_FUNCTIONS["linear"], GROWTH_FUNCTIONS["quadratic"], n_values)
        assert not dominates(GROWTH_FUNCTIONS["quadratic"], GROWTH_FUNCTIONS["linear"], n_values)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
