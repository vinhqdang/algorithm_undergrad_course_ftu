"""
Problem 07 - Karger with Amplification (SOLUTION)
==================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from itertools import combinations
from typing import List

from solution_problem06 import karger_min_cut


def brute_force_min_cut(graph) -> int:
    """True global min-cut by trying all vertex bipartitions (small n only)."""
    vertices, edges = graph
    n = len(vertices)
    if n < 2:
        return 0
    v0 = vertices[0]
    rest = vertices[1:]
    best = None
    # Fix v0 on side A; enumerate proper subsets of the rest to join side A.
    # Exclude r == len(rest), which would leave side B empty (not a valid cut).
    for r in range(len(rest)):
        for combo in combinations(rest, r):
            side_a = {v0, *combo}
            cut = sum(1 for u, v in edges if (u in side_a) != (v in side_a))
            if best is None or cut < best:
                best = cut
    return best


def karger_min_cut_amplified(graph, trials: int, seed: int) -> int:
    """Run Karger `trials` times (derived seeds); return the smallest cut found."""
    best = None
    for t in range(trials):
        cut = karger_min_cut(graph, seed=seed + t)
        if best is None or cut < best:
            best = cut
    return best


if __name__ == "__main__":
    from starter_code import generate_graph

    # Hand-checked tiny graph: a square 0-1-2-3-0 has global min-cut 2.
    square = ([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (0, 3)])
    assert brute_force_min_cut(square) == 2
    assert karger_min_cut_amplified(square, trials=100, seed=0) == 2

    # Amplification matches brute force on several small random graphs.
    for trial in range(15):
        g = generate_graph(7, seed=700 + trial, p=0.45)
        true_min = brute_force_min_cut(g)
        # n=7 -> C(7,2)=21; ~21*ln(7) ~ 41 runs gives high success. Use plenty.
        amp = karger_min_cut_amplified(g, trials=300, seed=trial * 13)
        assert amp == true_min, (trial, amp, true_min)

    print("All tests passed!")
