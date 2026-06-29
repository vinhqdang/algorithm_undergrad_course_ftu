"""
Problem 12 - Simulated-Annealing-Style Randomized Max-Cut (SOLUTION)
====================================================================
"""

import math
import os
import sys
from random import Random
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cut_value, generate_graph, neighbors  # noqa: E402
from solution_problem10 import max_cut_local_search  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def simulated_annealing_max_cut(
    graph: Graph,
    seed: int = 0,
    iterations: int = 2000,
    t_start: float = 2.0,
    t_end: float = 0.01,
) -> Tuple[List[int], int]:
    """Simulated-annealing-style local search for Max-Cut.

    Each iteration picks a random vertex and considers flipping it: improving flips
    are always accepted, worsening flips (decreasing the cut by Delta >= 0) are
    accepted with probability exp(-Delta / T), where T cools geometrically from
    t_start to t_end. Returns (best_side, best_cut), the best partition ever seen.
    """
    n, _ = graph
    rng = Random(seed)
    adj = neighbors(graph)

    side = [rng.randint(0, 1) for _ in range(n)]
    cur_cut = cut_value(graph, side)
    best_side = list(side)
    best_cut = cur_cut

    if n == 0 or iterations <= 0:
        return best_side, best_cut

    # Geometric cooling factor.
    ratio = (t_end / t_start) ** (1.0 / max(1, iterations - 1)) if t_start > 0 else 1.0
    T = t_start

    for _ in range(iterations):
        v = rng.randrange(n)
        same = sum(1 for u in adj[v] if side[u] == side[v])
        cut_edges = len(adj[v]) - same
        # Flipping v changes the cut by (same - cut_edges).
        delta = same - cut_edges  # > 0 means improvement
        accept = False
        if delta >= 0:
            accept = True
        else:
            # worsening move: accept with probability exp(-|delta| / T)
            if T > 0 and rng.random() < math.exp(delta / T):
                accept = True
        if accept:
            side[v] ^= 1
            cur_cut += delta
            if cur_cut > best_cut:
                best_cut = cur_cut
                best_side = list(side)
        T *= ratio

    return best_side, best_cut


if __name__ == "__main__":
    # Triangle: best cut 2.
    tri = (3, [(0, 1), (0, 2), (1, 2)])
    _, cut = simulated_annealing_max_cut(tri, seed=0)
    assert cut == 2

    # K4: best cut 4.
    k4 = (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    _, cut = simulated_annealing_max_cut(k4, seed=0)
    assert cut == 4

    # Annealing is never worse than the plain hill-climbing local optimum baseline
    # on the tested seeded instances.
    for trial in range(30):
        g = generate_graph(14, 0.4, seed=300 + trial)
        _, baseline = max_cut_local_search(g, seed=trial)
        _, annealed = simulated_annealing_max_cut(g, seed=trial, iterations=3000)
        assert annealed >= baseline

    print("All tests passed!")
