"""
Problem 06 - 0/1 Knapsack: Maximum Value (2-D DP)
=================================================

In the 0/1 Knapsack problem we have n items, item i with integer weight w_i and
value v_i, and a knapsack of integer capacity W. Each item is either taken
(once) or left -- we cannot take fractions or duplicates. Maximize total value
subject to total weight <= W.

2-D DP over (items considered, capacity used). Let dp[i][w] be the best value
achievable using the first i items with capacity exactly w available:

    dp[0][w] = 0
    dp[i][w] = dp[i-1][w]                                  if w_i > w
    dp[i][w] = max( dp[i-1][w],                            # skip item i
                    v_i + dp[i-1][w - w_i] )               # take item i

Implement `knapsack_value(weights, values, capacity)` returning dp[n][W]. This
runs in O(nW) time -- PSEUDO-polynomial (see the notes on why).

See practical_exercises.pdf, Problem 6.
"""

from typing import List


def knapsack_value(weights: List[int], values: List[int], capacity: int) -> int:
    """Return the maximum total value of items fitting within `capacity` (0/1)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert knapsack_value([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
        assert knapsack_value([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
        assert knapsack_value([], [], 10) == 0
        assert knapsack_value([5], [10], 4) == 0
        assert knapsack_value([5], [10], 5) == 10

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
