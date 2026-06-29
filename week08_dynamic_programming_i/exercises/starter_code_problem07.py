"""
Problem 07 - 0/1 Knapsack: Item Reconstruction
==============================================

Knowing the optimal VALUE (Problem 6) does not tell us WHICH items to pack.
After building the dp table dp[i][w], trace back from dp[n][W]:

    item i-1 was TAKEN iff dp[i][w] != dp[i-1][w]
    (the value with item i differs from the value without it).

When an item is taken, subtract its weight (w -= weights[i-1]) and continue to
row i-1; otherwise just move to row i-1 with the same w.

Implement `knapsack_solution(weights, values, capacity)` returning
`(best_value, chosen_indices)` (indices into the original lists, ascending).
The chosen items must have distinct indices, fit within capacity, and have
total value equal to the optimum.

See practical_exercises.pdf, Problem 7.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem06 import knapsack_value  # noqa: F401


def knapsack_solution(
    weights: List[int], values: List[int], capacity: int
) -> Tuple[int, List[int]]:
    """Return (best_value, chosen_indices) for the 0/1 knapsack."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        val, items = knapsack_solution([1, 3, 4, 5], [1, 4, 5, 7], 7)
        assert val == 9
        assert sorted(items) == [1, 2]

        val, items = knapsack_solution([5], [10], 4)
        assert val == 0 and items == []

        from starter_code import generate_knapsack_instance
        for trial in range(100):
            w, v, cap = generate_knapsack_instance(10, seed=trial)
            val, items = knapsack_solution(w, v, cap)
            assert len(set(items)) == len(items)
            assert sum(w[i] for i in items) <= cap
            assert sum(v[i] for i in items) == val

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
