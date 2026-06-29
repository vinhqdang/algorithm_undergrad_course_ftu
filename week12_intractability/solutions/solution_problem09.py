"""
Problem 09 - TSP via Held-Karp Bitmask DP (SOLUTION)
======================================================
"""

import itertools
import random
from typing import List

Matrix = List[List[float]]


def tsp_held_karp(dist: Matrix) -> float:
    """Shortest tour visiting every city once, returning to city 0, via the
    Held-Karp DP. O(n^2 * 2^n)."""
    n = len(dist)
    if n <= 1:
        return 0.0

    INF = float("inf")
    full = 1 << n
    # dp[mask][j]: shortest path starting at 0, visiting exactly the set `mask`,
    # ending at city j. Requires bit 0 in mask and bit j in mask.
    dp = [[INF] * n for _ in range(full)]
    dp[1][0] = 0.0  # only city 0 visited, sitting at 0

    for mask in range(full):
        if not (mask & 1):
            continue  # every valid subset includes the start, city 0
        for j in range(n):
            if dp[mask][j] == INF or not (mask & (1 << j)):
                continue
            for k in range(n):
                if mask & (1 << k):
                    continue
                new_mask = mask | (1 << k)
                cand = dp[mask][j] + dist[j][k]
                if cand < dp[new_mask][k]:
                    dp[new_mask][k] = cand

    best = INF
    for j in range(1, n):
        if dp[full - 1][j] != INF:
            best = min(best, dp[full - 1][j] + dist[j][0])
    return best


def tsp_brute_force(dist: Matrix) -> float:
    """Shortest tour by trying all (n-1)! permutations of the non-start cities."""
    n = len(dist)
    if n <= 1:
        return 0.0
    best = float("inf")
    for perm in itertools.permutations(range(1, n)):
        tour = [0] + list(perm)
        length = sum(dist[tour[i]][tour[(i + 1) % n]] for i in range(n))
        best = min(best, length)
    return best


def verify_tsp(num_trials: int, n: int, seed: int) -> bool:
    """True iff Held-Karp and brute force agree on `num_trials` random matrices."""
    for t in range(num_trials):
        rng = random.Random(seed + t)
        dist = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                d = float(rng.randint(1, 100))
                dist[i][j] = d
                dist[j][i] = d
        if abs(tsp_held_karp(dist) - tsp_brute_force(dist)) > 1e-9:
            return False
    return True


if __name__ == "__main__":
    # Symmetric square: tour 0-1-2-3-0 of cost 4
    square = [
        [0, 1, 2, 1],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [1, 2, 1, 0],
    ]
    assert abs(tsp_held_karp(square) - 4.0) < 1e-9
    assert abs(tsp_brute_force(square) - 4.0) < 1e-9

    # Trivial cases
    assert tsp_held_karp([[0]]) == 0.0
    assert tsp_held_karp([[0, 5], [5, 0]]) == 10.0  # 0->1->0

    # Held-Karp matches brute force on random instances
    assert verify_tsp(num_trials=20, n=5, seed=1)
    assert verify_tsp(num_trials=10, n=7, seed=99)

    print("All tests passed!")
