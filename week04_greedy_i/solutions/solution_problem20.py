"""
Problem 20 - Greedy Coin Change for a Canonical Coin System (SOLUTION)
==========================================================================
"""

from typing import Dict, List


def greedy_change(amount: int, denominations: List[int]) -> Dict[int, int]:
    """Return a dict {denomination: count} for the greedy change-making solution."""
    result: Dict[int, int] = {}
    remaining = amount
    for denom in sorted(denominations, reverse=True):
        if denom <= remaining:
            count, remaining = divmod(remaining, denom)
            if count > 0:
                result[denom] = count
    return result


def brute_force_min_coins(amount: int, denominations: List[int]) -> int:
    """Return the minimum number of coins needed to make `amount` (via DP)."""
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in denominations:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount]


if __name__ == "__main__":
    CANONICAL = [1, 2, 5, 10, 20, 50, 100, 200, 500]

    result = greedy_change(287, CANONICAL)
    total_value = sum(denom * count for denom, count in result.items())
    total_coins = sum(result.values())
    assert total_value == 287
    assert total_coins == 6

    for amount in [1, 7, 13, 99, 287, 999]:
        greedy_result = greedy_change(amount, CANONICAL)
        greedy_count = sum(greedy_result.values())
        optimal_count = brute_force_min_coins(amount, CANONICAL)
        assert greedy_count == optimal_count, (amount, greedy_count, optimal_count)

    assert sum(greedy_change(0, CANONICAL).values()) == 0
    assert brute_force_min_coins(0, CANONICAL) == 0

    print("All tests passed!")
