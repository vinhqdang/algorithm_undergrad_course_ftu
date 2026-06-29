"""
Problem 11 - Hill Climbing with Random Restarts vs. Brute Force (SOLUTION)
=========================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cut_value, generate_graph  # noqa: E402
from solution_problem10 import max_cut_local_search  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def brute_force_max_cut(graph: Graph) -> int:
    """Maximum cut value over all partitions (fix vertex 0 to side 0)."""
    n, _ = graph
    if n == 0:
        return 0
    best = 0
    for mask in range(1 << (n - 1)):
        side = [0] * n
        for v in range(1, n):
            if mask & (1 << (v - 1)):
                side[v] = 1
        best = max(best, cut_value(graph, side))
    return best


def hill_climbing_restarts(graph: Graph, restarts: int, seed: int) -> int:
    """Run max_cut_local_search from `restarts` seeds; return the best cut found."""
    best = 0
    for r in range(restarts):
        _, cut = max_cut_local_search(graph, seed=seed + r)
        best = max(best, cut)
    return best


if __name__ == "__main__":
    # Triangle: optimum 2.
    tri = (3, [(0, 1), (0, 2), (1, 2)])
    assert brute_force_max_cut(tri) == 2
    assert hill_climbing_restarts(tri, restarts=10, seed=0) == 2

    # K4: max cut = 4 (a 2-2 split).
    k4 = (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    assert brute_force_max_cut(k4) == 4
    assert hill_climbing_restarts(k4, restarts=10, seed=0) == 4

    # With enough restarts, hill climbing matches brute force on random small graphs,
    # and never exceeds the optimum.
    for trial in range(30):
        g = generate_graph(10, 0.4, seed=200 + trial)
        opt = brute_force_max_cut(g)
        # A single restart never beats the optimum.
        single = hill_climbing_restarts(g, restarts=1, seed=trial)
        assert single <= opt
        # Many restarts should find the optimum.
        many = hill_climbing_restarts(g, restarts=40, seed=trial)
        assert many <= opt
        assert many == opt

    print("All tests passed!")
