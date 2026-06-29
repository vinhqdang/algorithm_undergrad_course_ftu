"""
Problem 11 - Min-Cut Success-Probability Empirical Check (SOLUTION)
===================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from math import comb

from solution_problem06 import karger_min_cut
from solution_problem07 import brute_force_min_cut


def single_run_success_rate(graph, num_runs: int, seed: int) -> float:
    """Fraction of single Karger runs whose cut equals the true global min-cut."""
    true_min = brute_force_min_cut(graph)
    successes = 0
    for t in range(num_runs):
        if karger_min_cut(graph, seed=seed + t) == true_min:
            successes += 1
    return successes / num_runs


if __name__ == "__main__":
    # Square graph: n=4, C(4,2)=6, theoretical floor 1/6 ~ 0.1667.
    square = ([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (0, 3)])
    n = len(square[0])
    floor = 1.0 / comb(n, 2)
    rate = single_run_success_rate(square, num_runs=5000, seed=0)
    assert rate >= floor, (rate, floor)

    # A second small graph (n=5).
    from starter_code import generate_graph

    g = generate_graph(5, seed=11, p=0.5)
    floor5 = 1.0 / comb(5, 2)
    rate5 = single_run_success_rate(g, num_runs=5000, seed=123)
    assert rate5 >= floor5, (rate5, floor5)

    print("All tests passed!")
