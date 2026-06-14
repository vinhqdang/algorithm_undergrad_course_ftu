"""
Problem 20 - Greedy Coin Change for a Canonical Coin System
==============================================================

Implement `greedy_change(amount, denominations)`:

    Repeatedly take the LARGEST denomination that is <= the remaining
    amount, as many times as possible, until the amount reaches 0.

`denominations` is a list of positive integers (assume it always contains 1,
so a solution always exists). Return a dict mapping each denomination used to
the COUNT of coins of that denomination (denominations not used should not
appear in the dict, or may map to 0 -- both are acceptable, but the tests
below check the total value and total coin count).

Then implement `brute_force_min_coins(amount, denominations)` that returns
the MINIMUM possible number of coins needed to make `amount`, using dynamic
programming (a simple bottom-up table `dp[0..amount]` where `dp[0] = 0` and
`dp[a] = 1 + min(dp[a - c] for c in denominations if c <= a)`).

For the Vietnamese-Dong-like canonical system `[1, 2, 5, 10, 20, 50, 100,
200, 500]` (think of these as units of 1000 VND, or just abstract units),
greedy is OPTIMAL: `greedy_change` always uses the minimum number of coins.
Problem 21 explores a NON-canonical system where this fails.

See practical_exercises.pdf, Problem 20.
"""

from typing import Dict, List


def greedy_change(amount: int, denominations: List[int]) -> Dict[int, int]:
    """Return a dict {denomination: count} for the greedy change-making solution."""
    # TODO: implement this function.
    raise NotImplementedError


def brute_force_min_coins(amount: int, denominations: List[int]) -> int:
    """Return the minimum number of coins needed to make `amount` (via DP)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        CANONICAL = [1, 2, 5, 10, 20, 50, 100, 200, 500]

        # 287 = 200 + 50 + 20 + 10 + 5 + 2 -> 6 coins
        result = greedy_change(287, CANONICAL)
        total_value = sum(denom * count for denom, count in result.items())
        total_coins = sum(result.values())
        assert total_value == 287
        assert total_coins == 6

        # Greedy is optimal for the canonical system.
        for amount in [1, 7, 13, 99, 287, 999]:
            greedy_result = greedy_change(amount, CANONICAL)
            greedy_count = sum(greedy_result.values())
            optimal_count = brute_force_min_coins(amount, CANONICAL)
            assert greedy_count == optimal_count, (amount, greedy_count, optimal_count)

        # Amount 0 -> no coins.
        assert sum(greedy_change(0, CANONICAL).values()) == 0
        assert brute_force_min_coins(0, CANONICAL) == 0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
