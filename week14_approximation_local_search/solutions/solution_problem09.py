"""
Problem 09 - Knapsack FPTAS (Rounding and Scaling) (SOLUTION)
=============================================================
"""

import random
from typing import List


def knapsack_exact(profits: List[float], weights: List[int], capacity: int) -> float:
    """Exact 0/1 knapsack via the weight-indexed DP. Returns the optimal total profit."""
    n = len(profits)
    dp = [0.0] * (capacity + 1)
    for i in range(n):
        w_i = weights[i]
        p_i = profits[i]
        # Iterate capacities downward so each item is used at most once.
        for cap in range(capacity, w_i - 1, -1):
            cand = dp[cap - w_i] + p_i
            if cand > dp[cap]:
                dp[cap] = cand
    return dp[capacity]


def knapsack_fptas(profits: List[float], weights: List[int], capacity: int, epsilon: float) -> float:
    """FPTAS for knapsack: scale/round profits, solve exactly, return TRUE profit of the
    chosen items.
    """
    n = len(profits)
    # Discard items that do not fit at all.
    feasible = [(p, w, i) for i, (p, w) in enumerate(zip(profits, weights)) if w <= capacity]
    if not feasible:
        return 0.0

    p_max = max(p for p, _, _ in feasible)
    if p_max <= 0:
        return 0.0
    mu = epsilon * p_max / n
    if mu <= 0:
        # Degenerate epsilon -> fall back to exact.
        return knapsack_exact(profits, weights, capacity)

    rounded = [int(p / mu) for p, _, _ in feasible]
    weights_f = [w for _, w, _ in feasible]
    true_profits = [p for p, _, _ in feasible]
    total_rounded = sum(rounded)

    # Profit-indexed DP: min_weight[p] = minimum weight achieving rounded profit exactly p.
    INF = float("inf")
    min_weight = [INF] * (total_rounded + 1)
    min_weight[0] = 0
    # Track which items are chosen is unnecessary; we recover true profit via a
    # parallel DP that maximizes TRUE profit among item sets with weight <= capacity
    # achieving a given rounded profit. Simpler: do a max-true-profit DP keyed by weight,
    # but to honor "round profits then solve", we use the rounded DP and then map back.
    best_true = [-1.0] * (total_rounded + 1)
    best_true[0] = 0.0
    for idx in range(len(feasible)):
        rp = rounded[idx]
        w = weights_f[idx]
        tp = true_profits[idx]
        # iterate rounded profit downward to keep 0/1 semantics
        for P in range(total_rounded, rp - 1, -1):
            if min_weight[P - rp] + w < min_weight[P]:
                min_weight[P] = min_weight[P - rp] + w
                best_true[P] = best_true[P - rp] + tp
            elif min_weight[P - rp] + w == min_weight[P] and best_true[P - rp] + tp > best_true[P]:
                best_true[P] = best_true[P - rp] + tp

    # Among all achievable rounded profits with weight <= capacity, return the largest
    # corresponding TRUE profit.
    best = 0.0
    for P in range(total_rounded + 1):
        if min_weight[P] <= capacity and best_true[P] > best:
            best = best_true[P]
    return best


def verify_fptas(num_trials: int, n: int, epsilon: float, seed: int) -> bool:
    """Check FPTAS value >= (1 - epsilon) * exact optimum on random instances."""
    for trial in range(num_trials):
        rng = random.Random(seed + trial)
        profits = [rng.randint(1, 100) for _ in range(n)]
        weights = [rng.randint(1, 20) for _ in range(n)]
        capacity = rng.randint(10, 40)
        opt = knapsack_exact(profits, weights, capacity)
        approx = knapsack_fptas(profits, weights, capacity, epsilon)
        if approx < (1 - epsilon) * opt - 1e-9:
            return False
        if approx > opt + 1e-9:  # the FPTAS can never beat the exact optimum
            return False
    return True


if __name__ == "__main__":
    # Small exact check.
    profits = [60, 100, 120]
    weights = [10, 20, 30]
    assert knapsack_exact(profits, weights, 50) == 220  # items 2 and 3

    # FPTAS returns a feasible value not exceeding the optimum and within (1-eps).
    val = knapsack_fptas(profits, weights, 50, 0.1)
    assert val <= 220 + 1e-9
    assert val >= 0.9 * 220 - 1e-9

    # Nothing fits.
    assert knapsack_fptas([10], [100], 5, 0.1) == 0.0

    # Random verification of the (1-epsilon) guarantee at two epsilons.
    assert verify_fptas(num_trials=60, n=12, epsilon=0.2, seed=1) is True
    assert verify_fptas(num_trials=60, n=12, epsilon=0.1, seed=500) is True

    print("All tests passed!")
