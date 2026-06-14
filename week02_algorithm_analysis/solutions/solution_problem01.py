"""
Problem 01 - Ordering Functions by Growth Rate (SOLUTION)
============================================================
"""

import os
import sys
from typing import Callable, Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import GROWTH_FUNCTIONS


def order_by_growth(functions: Dict[str, Callable[[int], float]], n: int) -> List[str]:
    """Return the names in `functions`, sorted by increasing value at n."""
    return sorted(functions.keys(), key=lambda name: functions[name](n))


def dominates(f: Callable[[int], float], g: Callable[[int], float], n_values: List[int]) -> bool:
    """Return True iff f(n) <= g(n) for every n in n_values."""
    return all(f(n) <= g(n) for n in n_values)


if __name__ == "__main__":
    order_small = order_by_growth(GROWTH_FUNCTIONS, n=2)
    order_large = order_by_growth(GROWTH_FUNCTIONS, n=512)

    expected_large = [
        "constant", "logarithmic", "sqrt", "linear",
        "linearithmic", "quadratic", "cubic", "exponential",
    ]
    assert order_large == expected_large, order_large

    n_values = [1, 2, 4, 8, 16, 32, 64, 128]
    assert dominates(GROWTH_FUNCTIONS["logarithmic"], GROWTH_FUNCTIONS["linear"], n_values)
    assert dominates(GROWTH_FUNCTIONS["linear"], GROWTH_FUNCTIONS["quadratic"], n_values)
    assert not dominates(GROWTH_FUNCTIONS["quadratic"], GROWTH_FUNCTIONS["linear"], n_values)

    print(f"Order at n=2:    {order_small}")
    print(f"Order at n=512:  {order_large}")
    print("All tests passed!")
