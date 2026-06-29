"""
Problem 07 - Karger with Amplification
=======================================

Implement `brute_force_min_cut(graph)` computing the true global min-cut by trying
all vertex bipartitions (small n only), and `karger_min_cut_amplified(graph,
trials, seed)` that runs Problem 6's single contraction `trials` times (with
derived seeds) and returns the smallest cut found.

See practical_exercises.pdf, Problem 7.
"""

import os
import sys
from itertools import combinations
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions")
)

from solution_problem06 import karger_min_cut


def brute_force_min_cut(graph) -> int:
    """True global min-cut by trying all vertex bipartitions (small n only)."""
    # TODO: implement this function.
    raise NotImplementedError


def karger_min_cut_amplified(graph, trials: int, seed: int) -> int:
    """Run Karger `trials` times (derived seeds); return the smallest cut found."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        from starter_code import generate_graph

        square = ([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (0, 3)])
        assert brute_force_min_cut(square) == 2
        assert karger_min_cut_amplified(square, trials=100, seed=0) == 2

        for trial in range(15):
            g = generate_graph(7, seed=700 + trial, p=0.45)
            true_min = brute_force_min_cut(g)
            amp = karger_min_cut_amplified(g, trials=300, seed=trial * 13)
            assert amp == true_min, (trial, amp, true_min)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
