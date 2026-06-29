"""
Problem 05 - Verify Dijkstra and Bellman-Ford Agree on Non-Negative Graphs
==========================================================================

Generate random connected non-negative weighted graphs and confirm that
Dijkstra (Problem 2) and Bellman-Ford (Problem 4) compute identical distances.
See practical_exercises.pdf, Problem 5.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from starter_code import generate_weighted_graph  # noqa: E402

from starter_code_problem02 import dijkstra  # noqa: E402
from starter_code_problem04 import bellman_ford  # noqa: E402


def agree_on_random_graph(n: int, seed: int) -> bool:
    """Return True iff Dijkstra and Bellman-Ford give equal distances on one graph."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_agreement(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff Dijkstra and Bellman-Ford agree on every random trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert agree_on_random_graph(8, seed=1) is True
        assert verify_agreement(num_trials=50, n=10, seed=100) is True
        assert verify_agreement(num_trials=30, n=20, seed=500) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
