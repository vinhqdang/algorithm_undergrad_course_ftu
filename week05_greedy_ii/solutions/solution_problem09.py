"""
Problem 09 - Verify Kruskal and Prim Agree on MST Weight (SOLUTION)
===================================================================
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_weighted_graph  # noqa: E402

from solution_problem07 import kruskal  # noqa: E402
from solution_problem08 import prim  # noqa: E402


def kruskal_equals_prim(n: int, seed: int) -> bool:
    """Return True iff Kruskal and Prim give equal MST weight on one instance."""
    graph = generate_weighted_graph(n, seed=seed, edge_prob=0.4, max_weight=20, connected=True)
    _, kw = kruskal(graph)
    pw = prim(graph)
    return abs(kw - pw) <= 1e-9


def verify_mst_agreement(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff Kruskal and Prim agree on every random connected trial."""
    return all(kruskal_equals_prim(n, seed=seed + t) for t in range(num_trials))


if __name__ == "__main__":
    assert kruskal_equals_prim(8, seed=1) is True
    assert verify_mst_agreement(num_trials=50, n=12, seed=200) is True
    assert verify_mst_agreement(num_trials=30, n=25, seed=900) is True

    print("All tests passed!")
