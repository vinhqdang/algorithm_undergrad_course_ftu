"""
Problem 05 - Verify FPT Vertex Cover vs Brute-Force Minimum (SOLUTION)
======================================================================
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import brute_force_vertex_cover, generate_graph  # noqa: E402
from solution_problem04 import vertex_cover_fpt  # noqa: E402


def min_vertex_cover_via_fpt(n, edges):
    """Find the minimum cover size by trying k = 0, 1, 2, ... with the FPT decider."""
    for k in range(n + 1):
        cover = vertex_cover_fpt(n, edges, k)
        if cover is not None:
            return cover
    return set(range(n))  # unreachable


def verify_fpt_vertex_cover(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff FPT and brute force agree on the minimum cover size,
    and the FPT decision threshold matches that size, for every trial."""
    for trial in range(num_trials):
        _, edges = generate_graph(n, p=0.4, seed=seed + trial)
        bf = brute_force_vertex_cover(n, edges)
        fpt = min_vertex_cover_via_fpt(n, edges)
        if len(bf) != len(fpt):
            return False
        opt = len(bf)
        # A cover of size opt must exist; of size opt-1 must not.
        if vertex_cover_fpt(n, edges, opt) is None:
            return False
        if opt > 0 and vertex_cover_fpt(n, edges, opt - 1) is not None:
            return False
    return True


if __name__ == "__main__":
    assert verify_fpt_vertex_cover(num_trials=30, n=8, seed=1) is True
    assert verify_fpt_vertex_cover(num_trials=20, n=10, seed=100) is True
    assert verify_fpt_vertex_cover(num_trials=15, n=6, seed=999) is True

    print("All tests passed!")
