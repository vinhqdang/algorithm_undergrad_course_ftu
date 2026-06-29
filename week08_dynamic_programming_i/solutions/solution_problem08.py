"""
Problem 08 - Coin Change: Minimum Number of Coins (Unbounded) (SOLUTION)
========================================================================
"""

from typing import List


def coin_change_min(coins: List[int], amount: int) -> int:
    """Return the minimum number of coins (each usable unlimited times) summing
    to `amount`, or -1 if it cannot be made.

    Unbounded-knapsack-style 1-D DP:
        dp[0] = 0
        dp[a] = 1 + min(dp[a - c] for c in coins if c <= a), else infinity.
    """
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return -1 if dp[amount] == INF else int(dp[amount])


if __name__ == "__main__":
    assert coin_change_min([1, 2, 5], 11) == 3      # 5 + 5 + 1
    assert coin_change_min([2], 3) == -1            # odd amount, only even coins
    assert coin_change_min([1], 0) == 0
    assert coin_change_min([1, 3, 4], 6) == 2       # 3 + 3 (greedy would give 3)
    assert coin_change_min([2, 5, 10, 1], 27) == 4  # 10+10+5+2
    assert coin_change_min([5, 10], 3) == -1
    assert coin_change_min([7], 14) == 2

    # Cross-check against brute-force BFS on small amounts.
    from collections import deque

    def brute(coins, amount):
        if amount == 0:
            return 0
        seen = {0}
        q = deque([(0, 0)])
        while q:
            total, steps = q.popleft()
            for c in coins:
                nxt = total + c
                if nxt == amount:
                    return steps + 1
                if nxt < amount and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
        return -1

    import random
    rng = random.Random(2)
    for _ in range(100):
        coins = sorted({rng.randint(1, 9) for _ in range(rng.randint(1, 4))})
        amount = rng.randint(0, 40)
        assert coin_change_min(coins, amount) == brute(coins, amount)

    print("All tests passed!")
