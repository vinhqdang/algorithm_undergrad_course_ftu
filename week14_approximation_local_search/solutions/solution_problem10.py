"""
Problem 10 - Max-Cut Local Search (Vertex Flips) (SOLUTION)
===========================================================
"""

import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cut_value, generate_graph, neighbors  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def max_cut_local_search(graph: Graph, seed: int = 0) -> Tuple[List[int], int]:
    """Local search for Max-Cut via single-vertex flips.

    Start from a seeded random partition; while some vertex has more edges to its
    own side than to the other side, flip it. Returns (side, cut).
    """
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
            if same > cut:  # flipping strictly increases the cut
                side[v] ^= 1
                improved = True
    return side, cut_value(graph, side)


def verify_local_optimum_half(num_trials: int, n: int, p: float, seed: int) -> bool:
    """Check that the local-optimum cut is >= m/2 on random graphs."""
    for trial in range(num_trials):
        g = generate_graph(n, p, seed=seed + trial)
        _, m_edges = g
        _, cut = max_cut_local_search(g, seed=seed + trial)
        if cut < len(m_edges) / 2:
            return False
    return True


if __name__ == "__main__":
    # Triangle: max cut = 2 (any 2-1 split); local search must reach >= m/2 = 1.5 -> >= 2.
    tri = (3, [(0, 1), (0, 2), (1, 2)])
    _, cut = max_cut_local_search(tri, seed=0)
    assert cut >= len(tri[1]) / 2
    assert cut == 2

    # Complete bipartite K_{2,2} -> max cut = all 4 edges.
    k22 = (4, [(0, 2), (0, 3), (1, 2), (1, 3)])
    _, cut = max_cut_local_search(k22, seed=1)
    assert cut == 4

    # Empty graph: cut 0.
    _, cut = max_cut_local_search((5, []), seed=0)
    assert cut == 0

    # Random verification that every local optimum cuts >= m/2.
    assert verify_local_optimum_half(num_trials=100, n=12, p=0.3, seed=10) is True
    assert verify_local_optimum_half(num_trials=100, n=15, p=0.5, seed=99) is True

    print("All tests passed!")
