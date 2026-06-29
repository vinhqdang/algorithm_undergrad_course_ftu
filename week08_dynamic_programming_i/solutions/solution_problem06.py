"""
Problem 06 - 0/1 Knapsack: Maximum Value (2-D DP) (SOLUTION)
============================================================
"""

from typing import List


def knapsack_value(weights: List[int], values: List[int], capacity: int) -> int:
    """Return the maximum total value of items fitting in `capacity`, each item
    used at most once (0/1 knapsack).

    2-D DP: dp[i][w] = best value using the first i items with capacity w.
        dp[0][w] = 0
        dp[i][w] = dp[i-1][w]                                 if w_i > w
        dp[i][w] = max(dp[i-1][w], v_i + dp[i-1][w - w_i])    otherwise
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wi = weights[i - 1]
        vi = values[i - 1]
        for w in range(capacity + 1):
            best = dp[i - 1][w]  # skip item i-1
            if wi <= w:
                best = max(best, vi + dp[i - 1][w - wi])  # take item i-1
            dp[i][w] = best
    return dp[n][capacity]


if __name__ == "__main__":
    # Classic instance.
    assert knapsack_value([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9   # items 2+3 (w=3+4, v=4+5)
    assert knapsack_value([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7   # items 0+1
    assert knapsack_value([], [], 10) == 0
    assert knapsack_value([5], [10], 4) == 0   # too heavy
    assert knapsack_value([5], [10], 5) == 10

    # Cross-check against brute force on small random instances.
    import itertools
    import random
    rng = random.Random(1)
    for _ in range(200):
        n = rng.randint(0, 8)
        w = [rng.randint(1, 8) for _ in range(n)]
        v = [rng.randint(1, 15) for _ in range(n)]
        cap = rng.randint(0, 20)
        brute = 0
        for r in range(n + 1):
            for combo in itertools.combinations(range(n), r):
                if sum(w[i] for i in combo) <= cap:
                    brute = max(brute, sum(v[i] for i in combo))
        assert knapsack_value(w, v, cap) == brute

    print("All tests passed!")
