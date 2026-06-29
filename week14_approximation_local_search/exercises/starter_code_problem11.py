"""
Problem 11 - Hill Climbing with Random Restarts vs. Brute Force
===============================================================

Implement `brute_force_max_cut(graph)` returning the maximum cut over all
partitions (fix vertex 0 on side 0 to avoid the symmetric double-count). Then
`hill_climbing_restarts(graph, restarts, seed)`: run `max_cut_local_search` from
`restarts` different seeds and return the best cut found.

With enough restarts the best cut found should match the brute-force optimum on
small graphs; a single restart never exceeds the optimum. Intended for n <= 12.

You may reuse `max_cut_local_search` from Problem 10 (re-implemented here).

See practical_exercises.pdf, Problem 11.
"""

import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cut_value, generate_graph, neighbors  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def max_cut_local_search(graph: Graph, seed: int = 0) -> Tuple[List[int], int]:
    """Max-Cut local search (copied from Problem 10)."""
    n, _ = graph
    rng = random.Random(seed)
    side = [rng.randint(0, 1) for _ in range(n)]
    adj = neighbors(graph)
    improved = True
    while improved:
        improved = False
        for v in range(n):
            same = sum(1 for u in adj[v] if side[u] == side[v])
            cut = len(adj[v]) - same
            if same > cut:
                side[v] ^= 1
                improved = True
    return side, cut_value(graph, side)


def brute_force_max_cut(graph: Graph) -> int:
    """Return the maximum cut value over all partitions (fix vertex 0 to side 0)."""
    # TODO: implement this function.
    raise NotImplementedError


def hill_climbing_restarts(graph: Graph, restarts: int, seed: int) -> int:
    """Run local search from `restarts` seeds; return the best cut found."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        tri = (3, [(0, 1), (0, 2), (1, 2)])
        assert brute_force_max_cut(tri) == 2
        assert hill_climbing_restarts(tri, restarts=10, seed=0) == 2

        k4 = (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
        assert brute_force_max_cut(k4) == 4
        assert hill_climbing_restarts(k4, restarts=10, seed=0) == 4

        for trial in range(30):
            g = generate_graph(10, 0.4, seed=200 + trial)
            opt = brute_force_max_cut(g)
            single = hill_climbing_restarts(g, restarts=1, seed=trial)
            assert single <= opt
            many = hill_climbing_restarts(g, restarts=40, seed=trial)
            assert many <= opt
            assert many == opt

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
