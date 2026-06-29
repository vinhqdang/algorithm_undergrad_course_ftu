"""
Problem 07 - 0/1 Knapsack: Item Reconstruction (SOLUTION)
=========================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution_problem06 import knapsack_value


def knapsack_solution(
    weights: List[int], values: List[int], capacity: int
) -> Tuple[int, List[int]]:
    """Return (best_value, chosen_indices) for the 0/1 knapsack.

    Build the dp table, then trace back: item i-1 was taken iff
    dp[i][w] != dp[i-1][w] (taking it strictly contributed); subtract its
    weight and continue.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wi = weights[i - 1]
        vi = values[i - 1]
        for w in range(capacity + 1):
            best = dp[i - 1][w]
            if wi <= w:
                best = max(best, vi + dp[i - 1][w - wi])
            dp[i][w] = best

    chosen: List[int] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= weights[i - 1]
    chosen.reverse()
    return dp[n][capacity], chosen


if __name__ == "__main__":
    val, items = knapsack_solution([1, 3, 4, 5], [1, 4, 5, 7], 7)
    assert val == 9
    assert sum(1 * (i == 1) + 1 * (i == 2) for i in items) == 2  # items 1 and 2
    assert sorted(items) == [1, 2]

    val, items = knapsack_solution([5], [10], 4)
    assert val == 0 and items == []

    # The reconstructed set must respect capacity and have the right total value,
    # cross-checked against the value-only routine on random instances.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from starter_code import generate_knapsack_instance

    for trial in range(100):
        w, v, cap = generate_knapsack_instance(10, seed=trial)
        val, items = knapsack_solution(w, v, cap)
        assert len(set(items)) == len(items)               # no duplicates
        assert sum(w[i] for i in items) <= cap             # fits capacity
        assert sum(v[i] for i in items) == val             # value matches
        assert val == knapsack_value(w, v, cap)            # value is optimal

    print("All tests passed!")
