"""
Problem 05 - Verify Dijkstra and Bellman-Ford Agree on Non-Negative Graphs (SOLUTION)
=====================================================================================
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_weighted_graph  # noqa: E402

from solution_problem02 import dijkstra  # noqa: E402
from solution_problem04 import bellman_ford  # noqa: E402


def agree_on_random_graph(n: int, seed: int) -> bool:
    """Return True iff Dijkstra and Bellman-Ford give equal distances.

    Generates a random connected non-negative weighted graph (so both
    algorithms are valid) and compares the distance dict from source 0.
    """
    graph = generate_weighted_graph(n, seed=seed, edge_prob=0.4, max_weight=15)
    d_dij = dijkstra(graph, 0)
    d_bf = bellman_ford(graph, 0)
    if d_bf is None:
        return False  # non-negative graph never has a negative cycle
    for v in graph:
        if abs(d_dij[v] - d_bf[v]) > 1e-9:
            return False
    return True


def verify_agreement(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff Dijkstra and Bellman-Ford agree on every random trial."""
    return all(agree_on_random_graph(n, seed=seed + t) for t in range(num_trials))


if __name__ == "__main__":
    assert agree_on_random_graph(8, seed=1) is True
    assert verify_agreement(num_trials=50, n=10, seed=100) is True
    assert verify_agreement(num_trials=30, n=20, seed=500) is True

    print("All tests passed!")
