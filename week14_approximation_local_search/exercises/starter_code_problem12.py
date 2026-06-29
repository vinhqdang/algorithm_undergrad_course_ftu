"""
Problem 12 - Simulated-Annealing-Style Randomized Max-Cut
==========================================================

Implement `simulated_annealing_max_cut(graph, seed, iterations, t_start,
t_end)`: starting from a seeded random partition, on each iteration pick a
random vertex and consider flipping it; if the flip improves the cut, accept it;
otherwise accept it with probability exp(-Delta / T) where Delta >= 0 is the
decrease in cut value and T is the current temperature (cooled geometrically
from t_start to t_end). Return (best_side, best_cut) -- the best partition EVER
seen.

The annealing result must never be worse than the plain hill-climbing local
optimum baseline (Problem 10) on the tested seeded instances. Seed all
randomness so the test is deterministic.

You may reuse `max_cut_local_search` from Problem 10 (re-implemented here).

See practical_exercises.pdf, Problem 12.
"""

import math
import os
import sys
from random import Random
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cut_value, generate_graph, neighbors  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def max_cut_local_search(graph: Graph, seed: int = 0) -> Tuple[List[int], int]:
    """Max-Cut local search baseline (copied from Problem 10)."""
    n, _ = graph
    rng = Random(seed)
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


def simulated_annealing_max_cut(
    graph: Graph,
    seed: int = 0,
    iterations: int = 2000,
    t_start: float = 2.0,
    t_end: float = 0.01,
) -> Tuple[List[int], int]:
    """Simulated-annealing-style Max-Cut. Return (best_side, best_cut)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        tri = (3, [(0, 1), (0, 2), (1, 2)])
        _, cut = simulated_annealing_max_cut(tri, seed=0)
        assert cut == 2

        k4 = (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
        _, cut = simulated_annealing_max_cut(k4, seed=0)
        assert cut == 4

        for trial in range(30):
            g = generate_graph(14, 0.4, seed=300 + trial)
            _, baseline = max_cut_local_search(g, seed=trial)
            _, annealed = simulated_annealing_max_cut(g, seed=trial, iterations=3000)
            assert annealed >= baseline

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
