"""
Problem 09 - Verify Kruskal and Prim Agree on MST Weight
========================================================

Generate random connected weighted graphs and confirm Kruskal (Problem 7) and
Prim (Problem 8) produce the same total MST weight. See practical_exercises.pdf,
Problem 9.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from starter_code import generate_weighted_graph  # noqa: E402

from starter_code_problem07 import kruskal  # noqa: E402
from starter_code_problem08 import prim  # noqa: E402


def kruskal_equals_prim(n: int, seed: int) -> bool:
    """Return True iff Kruskal and Prim give equal MST weight on one instance."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_mst_agreement(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff Kruskal and Prim agree on every random connected trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert kruskal_equals_prim(8, seed=1) is True
        assert verify_mst_agreement(num_trials=50, n=12, seed=200) is True
        assert verify_mst_agreement(num_trials=30, n=25, seed=900) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
