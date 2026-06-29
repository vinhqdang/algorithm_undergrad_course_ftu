"""
Problem 08 - Coin Change: Minimum Number of Coins (Unbounded)
============================================================

Given coin denominations `coins` (unlimited supply of each) and a target
`amount`, find the MINIMUM number of coins summing to `amount`, or -1 if
impossible. Unlike Week 4's greedy coin change, DP is correct for ANY coin
system (greedy only works for "canonical" systems).

This is the UNBOUNDED knapsack flavor (each coin may be reused). 1-D DP:

    dp[0] = 0
    dp[a] = 1 + min( dp[a - c] for c in coins if c <= a ),  else infinity

Implement `coin_change_min(coins, amount)` returning the minimum coin count or
-1. (Note: iterate a from 1 up to amount; because coins are reusable, you do
NOT reverse the inner loop, unlike 0/1 subset sum in Problem 5.)

See practical_exercises.pdf, Problem 8.
"""

from typing import List


def coin_change_min(coins: List[int], amount: int) -> int:
    """Return the minimum number of coins summing to `amount`, or -1."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert coin_change_min([1, 2, 5], 11) == 3
        assert coin_change_min([2], 3) == -1
        assert coin_change_min([1], 0) == 0
        assert coin_change_min([1, 3, 4], 6) == 2
        assert coin_change_min([2, 5, 10, 1], 27) == 4
        assert coin_change_min([5, 10], 3) == -1
        assert coin_change_min([7], 14) == 2

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
