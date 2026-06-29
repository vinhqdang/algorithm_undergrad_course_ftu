"""
Problem 10 - Rod Cutting: Maximum Revenue and the Cut List (SOLUTION)
=====================================================================
"""

from typing import List, Tuple


def rod_cutting(prices: List[int]) -> Tuple[int, List[int]]:
    """Given `prices` where prices[i] is the price of a piece of length i+1,
    cut a rod of length n = len(prices) to maximize total revenue.

    Returns (best_revenue, cuts) where `cuts` is a list of piece lengths
    (summing to n) achieving the optimum.

    Unbounded-knapsack-style DP:
        rev[0] = 0
        rev[L] = max over cut length k in 1..L of prices[k-1] + rev[L-k]
    Record the first cut to reconstruct the piece lengths.
    """
    n = len(prices)
    rev = [0] * (n + 1)
    first_cut = [0] * (n + 1)
    for L in range(1, n + 1):
        best = float("-inf")
        for k in range(1, L + 1):
            candidate = prices[k - 1] + rev[L - k]
            if candidate > best:
                best = candidate
                first_cut[L] = k
        rev[L] = int(best)

    cuts: List[int] = []
    L = n
    while L > 0:
        cuts.append(first_cut[L])
        L -= first_cut[L]
    return rev[n], cuts


if __name__ == "__main__":
    # Classic CLRS price table for lengths 1..8.
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rev, cuts = rod_cutting(prices)
    assert rev == 22                 # length 8 -> 2 + 6 gives 5 + 17 = 22
    assert sum(cuts) == 8
    assert sum(prices[k - 1] for k in cuts) == rev

    # No cutting beneficial: linear price.
    rev, cuts = rod_cutting([2, 4, 6])
    assert rev == 6
    assert sum(cuts) == 3
    assert sum([2, 4, 6][k - 1] for k in cuts) == rev

    rev, cuts = rod_cutting([])
    assert rev == 0 and cuts == []

    rev, cuts = rod_cutting([3])
    assert rev == 3 and cuts == [1]

    # Cross-check revenue against brute-force compositions on small n.
    def brute(prices):
        n = len(prices)
        best = [0] * (n + 1)
        for L in range(1, n + 1):
            best[L] = max(prices[k - 1] + best[L - k] for k in range(1, L + 1))
        return best[n]

    import random
    rng = random.Random(4)
    for _ in range(100):
        n = rng.randint(0, 8)
        prices = [rng.randint(1, 12) for _ in range(n)]
        rev, cuts = rod_cutting(prices)
        assert rev == brute(prices)
        assert sum(cuts) == n
        assert sum(prices[k - 1] for k in cuts) == rev

    print("All tests passed!")
