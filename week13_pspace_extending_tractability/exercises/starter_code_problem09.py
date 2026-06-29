"""
Problem 09 - Branch-and-Bound TSP
==================================

Implement `tsp_branch_and_bound(dist)` returning the length of the shortest
Hamiltonian cycle through all cities, starting and ending at city 0, where
``dist`` is a symmetric n x n distance matrix.

Use branch and bound over the order in which cities are visited, pruning a
partial tour when ``cost_so_far + lower_bound`` >= the best complete tour found
so far. The provided `_lower_bound` adds, for the current city and each
unvisited city, the cheapest edge that could still leave it -- an admissible
(never-overestimating) bound.

The optimum must equal Held-Karp DP (`held_karp`, provided).

See practical_exercises.pdf, Problem 9.
"""

from typing import List


def _lower_bound(dist, visited, current, cost_so_far, n) -> float:
    """Admissible lower bound on the cost to complete the tour; provided."""
    bound = cost_so_far
    unvisited = [c for c in range(n) if not visited[c]]
    nodes = unvisited + [current]
    for u in nodes:
        best = min((dist[u][w] for w in unvisited + [0] if w != u), default=0)
        bound += best
    return bound


def held_karp(dist: List[List[float]]) -> float:
    """Exact TSP via Held-Karp DP in O(2^n * n^2); provided for verification."""
    n = len(dist)
    if n <= 1:
        return 0.0
    INF = float("inf")
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


def tsp_branch_and_bound(dist: List[List[float]]) -> float:
    """Return the length of the shortest Hamiltonian cycle from/to city 0."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        import random

        dist = [
            [0, 1, 2 ** 0.5, 1],
            [1, 0, 1, 2 ** 0.5],
            [2 ** 0.5, 1, 0, 1],
            [1, 2 ** 0.5, 1, 0],
        ]
        assert abs(tsp_branch_and_bound(dist) - 4.0) < 1e-9

        def random_distance_matrix(n, rng):
            pts = [(rng.uniform(0, 100), rng.uniform(0, 100)) for _ in range(n)]
            d = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    dx, dy = pts[i][0] - pts[j][0], pts[i][1] - pts[j][1]
                    d[i][j] = (dx * dx + dy * dy) ** 0.5
            return d

        rng = random.Random(31)
        for _ in range(40):
            n = rng.randint(2, 8)
            d = random_distance_matrix(n, rng)
            assert abs(tsp_branch_and_bound(d) - held_karp(d)) < 1e-6

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
