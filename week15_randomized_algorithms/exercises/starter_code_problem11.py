"""
Problem 11 - Min-Cut Success-Probability Empirical Check
=========================================================

Implement `single_run_success_rate(graph, num_runs, seed)`: run Problem 6's single
Karger contraction `num_runs` times (derived seeds), and return the fraction of
runs whose cut equals the true global min-cut (use `brute_force_min_cut` from
Problem 7).

See practical_exercises.pdf, Problem 11.
"""

import os
import sys
from math import comb

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions")
)

from solution_problem06 import karger_min_cut
from solution_problem07 import brute_force_min_cut


def single_run_success_rate(graph, num_runs: int, seed: int) -> float:
    """Fraction of single Karger runs whose cut equals the true global min-cut."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        from starter_code import generate_graph

        square = ([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (0, 3)])
        n = len(square[0])
        floor = 1.0 / comb(n, 2)
        rate = single_run_success_rate(square, num_runs=5000, seed=0)
        assert rate >= floor, (rate, floor)

        g = generate_graph(5, seed=11, p=0.5)
        floor5 = 1.0 / comb(5, 2)
        rate5 = single_run_success_rate(g, num_runs=5000, seed=123)
        assert rate5 >= floor5, (rate5, floor5)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
