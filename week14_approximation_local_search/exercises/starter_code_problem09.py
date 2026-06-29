"""
Problem 09 - Knapsack FPTAS (Rounding and Scaling)
===================================================

Implement `knapsack_exact(profits, weights, capacity)` via the standard
weight-indexed DP. Then implement `knapsack_fptas(profits, weights, capacity,
epsilon)`: set mu = epsilon * p_max / n, round each profit down to
floor(p_i / mu), solve exactly on the rounded profits (profit-indexed DP), and
return the TRUE total profit of the chosen items. Then `verify_fptas(num_trials,
n, epsilon, seed)`: check FPTAS value >= (1 - epsilon) * exact optimum.

See practical_exercises.pdf, Problem 9.
"""

import random
from typing import List


def knapsack_exact(profits: List[float], weights: List[int], capacity: int) -> float:
    """Exact 0/1 knapsack via weight-indexed DP. Return optimal total profit."""
    # TODO: implement this function.
    raise NotImplementedError


def knapsack_fptas(profits: List[float], weights: List[int], capacity: int, epsilon: float) -> float:
    """FPTAS: scale/round profits, solve exactly, return TRUE profit of chosen items."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_fptas(num_trials: int, n: int, epsilon: float, seed: int) -> bool:
    """Return True iff FPTAS value >= (1 - epsilon) * exact optimum on every trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        profits = [60, 100, 120]
        weights = [10, 20, 30]
        assert knapsack_exact(profits, weights, 50) == 220

        val = knapsack_fptas(profits, weights, 50, 0.1)
        assert val <= 220 + 1e-9
        assert val >= 0.9 * 220 - 1e-9

        assert knapsack_fptas([10], [100], 5, 0.1) == 0.0

        assert verify_fptas(num_trials=60, n=12, epsilon=0.2, seed=1) is True
        assert verify_fptas(num_trials=60, n=12, epsilon=0.1, seed=500) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
