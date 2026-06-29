"""
Problem 09 - Coin Change: Number of Distinct Ways (SOLUTION)
============================================================
"""

from typing import List


def coin_change_ways(coins: List[int], amount: int) -> int:
    """Return the number of distinct multisets of coins summing to `amount`.

    Counting unbounded knapsack. To count COMBINATIONS (order does not matter),
    loop over coins on the OUTSIDE and amounts on the inside:
        ways[0] = 1
        for c in coins:
            for a in c..amount:
                ways[a] += ways[a - c]
    Putting the coin loop outside guarantees each combination is counted once
    (coins are "committed" in a fixed order), avoiding counting permutations.
    """
    ways = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            ways[a] += ways[a - c]
    return ways[amount]


if __name__ == "__main__":
    assert coin_change_ways([1, 2, 5], 5) == 4   # 5; 2+2+1; 2+1+1+1; 1*5
    assert coin_change_ways([2], 3) == 0
    assert coin_change_ways([], 0) == 1          # one way to make 0: take nothing
    assert coin_change_ways([1, 2, 3], 4) == 4   # 1+3; 2+2; 1+1+2; 1+1+1+1
    assert coin_change_ways([7], 14) == 1        # 7+7
    assert coin_change_ways([1], 0) == 1

    # Cross-check against brute force (count non-decreasing coin multisets).
    def brute(coins, amount):
        coins = sorted(set(coins))
        def rec(i, remaining):
            if remaining == 0:
                return 1
            if i == len(coins) or remaining < 0:
                return 0
            # take coins[i] zero or more times
            total = 0
            k = 0
            while coins[i] * k <= remaining:
                total += rec(i + 1, remaining - coins[i] * k)
                k += 1
            return total
        return rec(0, amount)

    import random
    rng = random.Random(3)
    for _ in range(100):
        coins = sorted({rng.randint(1, 6) for _ in range(rng.randint(1, 4))})
        amount = rng.randint(0, 25)
        assert coin_change_ways(coins, amount) == brute(coins, amount)

    print("All tests passed!")
