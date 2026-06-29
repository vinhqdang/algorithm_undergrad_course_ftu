"""
Problem 08 - Branch-and-Bound 0/1 Knapsack (SOLUTION)
======================================================

Branch-and-bound explores the binary include/exclude tree for items, using the
fractional (LP relaxation) bound to prune subtrees that cannot beat the best
solution found so far. The optimum must equal the standard DP knapsack value.
"""

import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa: E402


def fractional_bound(values, weights, capacity, idx, cur_value, cur_weight) -> float:
    """Upper bound: take whole items greedily by value/weight from idx on,
    then a fraction of the next item to fill the remaining capacity."""
    bound = cur_value
    w = cur_weight
    for i in range(idx, len(values)):
        if w + weights[i] <= capacity:
            w += weights[i]
            bound += values[i]
        else:
            remaining = capacity - w
            if weights[i] > 0:
                bound += values[i] * (remaining / weights[i])
            break
    return bound


def knapsack_branch_and_bound(values: List[int], weights: List[int], capacity: int) -> int:
    """Return the maximum total value of a 0/1 knapsack via branch and bound."""
    n = len(values)
    # Sort items by value/weight ratio descending for a tight relaxation.
    order = sorted(range(n), key=lambda i: values[i] / weights[i] if weights[i] else float("inf"),
                   reverse=True)
    v = [values[i] for i in order]
    w = [weights[i] for i in order]

    best = 0

    def explore(idx, cur_value, cur_weight):
        nonlocal best
        if cur_value > best:
            best = cur_value
        if idx == n:
            return
        # Prune if even the optimistic fractional bound cannot beat best.
        if fractional_bound(v, w, capacity, idx, cur_value, cur_weight) <= best:
            return
        # Branch 1: include item idx if it fits.
        if cur_weight + w[idx] <= capacity:
            explore(idx + 1, cur_value + v[idx], cur_weight + w[idx])
        # Branch 2: exclude item idx.
        explore(idx + 1, cur_value, cur_weight)

    explore(0, 0, 0)
    return best


def dp_knapsack(values: List[int], weights: List[int], capacity: int) -> int:
    """Standard O(n * capacity) DP for the 0/1 knapsack optimum."""
    dp = [0] * (capacity + 1)
    for val, wt in zip(values, weights):
        for c in range(capacity, wt - 1, -1):
            dp[c] = max(dp[c], dp[c - wt] + val)
    return dp[capacity]


if __name__ == "__main__":
    # Small fixed instance.
    values = [60, 100, 120]
    weights = [10, 20, 30]
    cap = 50
    assert knapsack_branch_and_bound(values, weights, cap) == 220
    assert dp_knapsack(values, weights, cap) == 220

    # Randomized agreement with DP.
    rng = random.Random(2024)
    for _ in range(200):
        n = rng.randint(1, 12)
        vals = [rng.randint(1, 50) for _ in range(n)]
        wts = [rng.randint(1, 20) for _ in range(n)]
        cap = rng.randint(1, 60)
        bb = knapsack_branch_and_bound(vals, wts, cap)
        dp = dp_knapsack(vals, wts, cap)
        assert bb == dp, (vals, wts, cap, bb, dp)

    print("All tests passed!")
