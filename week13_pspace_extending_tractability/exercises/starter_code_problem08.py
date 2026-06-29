"""
Problem 08 - Branch-and-Bound 0/1 Knapsack
===========================================

Implement `knapsack_branch_and_bound(values, weights, capacity)` returning the
maximum total value of a 0/1 knapsack, using branch and bound:

  - Sort items by value/weight ratio (descending) so the relaxation is tight.
  - Explore the include/exclude binary tree.
  - At each node, compute the FRACTIONAL (LP-relaxation) upper bound
    (`fractional_bound`, provided): greedily take whole remaining items, then a
    fraction of the next to fill capacity. Prune a subtree when its bound does
    not exceed the best value found so far.

The optimum must equal the standard DP knapsack (`dp_knapsack`, provided).

See practical_exercises.pdf, Problem 8.
"""

from typing import List


def fractional_bound(values, weights, capacity, idx, cur_value, cur_weight) -> float:
    """Upper bound via the LP relaxation; provided for you."""
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


def dp_knapsack(values: List[int], weights: List[int], capacity: int) -> int:
    """Standard O(n * capacity) DP for the 0/1 knapsack optimum; provided."""
    dp = [0] * (capacity + 1)
    for val, wt in zip(values, weights):
        for c in range(capacity, wt - 1, -1):
            dp[c] = max(dp[c], dp[c - wt] + val)
    return dp[capacity]


def knapsack_branch_and_bound(values: List[int], weights: List[int], capacity: int) -> int:
    """Return the maximum 0/1 knapsack value via branch and bound."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        import random

        values = [60, 100, 120]
        weights = [10, 20, 30]
        cap = 50
        assert knapsack_branch_and_bound(values, weights, cap) == 220
        assert dp_knapsack(values, weights, cap) == 220

        rng = random.Random(2024)
        for _ in range(200):
            n = rng.randint(1, 12)
            vals = [rng.randint(1, 50) for _ in range(n)]
            wts = [rng.randint(1, 20) for _ in range(n)]
            cap = rng.randint(1, 60)
            assert knapsack_branch_and_bound(vals, wts, cap) == dp_knapsack(vals, wts, cap)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
