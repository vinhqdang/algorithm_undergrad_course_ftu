"""
Problem 09 - Branch-and-Bound TSP (SOLUTION)
=============================================

Solve the metric/symmetric Travelling Salesman Problem (find the shortest
Hamiltonian cycle starting and ending at city 0) via branch and bound with a
simple lower bound: cost so far + (minimum outgoing edge from each unvisited
city, plus the city we are currently at). We verify against Held-Karp DP.
"""

import os
import random
import sys
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa: E402


def _lower_bound(dist, visited, current, cost_so_far, n) -> float:
    """Admissible lower bound: cost so far + cheapest way each remaining city
    (and current) can still be left. Never overestimates the true completion."""
    bound = cost_so_far
    unvisited = [c for c in range(n) if not visited[c]]
    nodes = unvisited + [current]
    for u in nodes:
        # Cheapest edge leaving u toward an unvisited city or back to 0.
        best = min(
            (dist[u][w] for w in unvisited + [0] if w != u),
            default=0,
        )
        bound += best
    return bound


def tsp_branch_and_bound(dist: List[List[float]]) -> float:
    """Return the length of the shortest Hamiltonian cycle through all cities,
    starting/ending at city 0. ``dist`` is a symmetric n x n matrix."""
    n = len(dist)
    if n <= 1:
        return 0.0
    best = float("inf")
    visited = [False] * n
    visited[0] = True

    def explore(current, count, cost):
        nonlocal best
        if cost >= best:
            return
        if count == n:
            best = min(best, cost + dist[current][0])
            return
        if _lower_bound(dist, visited, current, cost, n) >= best:
            return
        # Branch over next unvisited city.
        for nxt in range(n):
            if not visited[nxt]:
                visited[nxt] = True
                explore(nxt, count + 1, cost + dist[current][nxt])
                visited[nxt] = False

    explore(0, 1, 0.0)
    return best


def held_karp(dist: List[List[float]]) -> float:
    """Exact TSP via Held-Karp DP in O(2^n * n^2)."""
    n = len(dist)
    if n <= 1:
        return 0.0
    INF = float("inf")
    # dp[mask][j] = min cost path starting at 0, visiting exactly mask, ending at j.
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0.0
    for mask in range(1 << n):
        if not (mask & 1):
            continue
        for j in range(n):
            if dp[mask][j] == INF:
                continue
            for k in range(n):
                if mask & (1 << k):
                    continue
                nm = mask | (1 << k)
                cand = dp[mask][j] + dist[j][k]
                if cand < dp[nm][k]:
                    dp[nm][k] = cand
    full = (1 << n) - 1
    return min(dp[full][j] + dist[j][0] for j in range(n))


def random_distance_matrix(n, rng) -> List[List[float]]:
    pts = [(rng.uniform(0, 100), rng.uniform(0, 100)) for _ in range(n)]
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dx = pts[i][0] - pts[j][0]
            dy = pts[i][1] - pts[j][1]
            dist[i][j] = (dx * dx + dy * dy) ** 0.5
    return dist


if __name__ == "__main__":
    # Square: 4 cities at corners of a unit square; optimal tour length 4.
    dist = [
        [0, 1, 2 ** 0.5, 1],
        [1, 0, 1, 2 ** 0.5],
        [2 ** 0.5, 1, 0, 1],
        [1, 2 ** 0.5, 1, 0],
    ]
    bb = tsp_branch_and_bound(dist)
    assert abs(bb - 4.0) < 1e-9, bb

    # Randomized agreement with Held-Karp.
    rng = random.Random(31)
    for _ in range(40):
        n = rng.randint(2, 8)
        d = random_distance_matrix(n, rng)
        bb = tsp_branch_and_bound(d)
        hk = held_karp(d)
        assert abs(bb - hk) < 1e-6, (n, bb, hk)

    print("All tests passed!")
