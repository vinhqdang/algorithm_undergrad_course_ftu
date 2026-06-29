"""
Problem 09 - Verify Bellman-Ford Agrees with Floyd-Warshall (SOLUTION)
=======================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_weighted_graph

from solution_problem06 import bellman_ford
from solution_problem07 import find_negative_cycle
from solution_problem08 import floyd_warshall


def verify_bf_vs_fw(num_trials: int, n: int, m: int, seed: int) -> bool:
    """On random negative-cycle-free graphs, BF from source 0 must equal FW row 0."""
    checked = 0
    trial = 0
    max_attempts = 100000  # safety guard against pathological parameters
    while checked < num_trials and trial < max_attempts:
        _, edges = generate_weighted_graph(n, m, seed=seed + trial)
        trial += 1
        if find_negative_cycle(n, edges) is not None:
            continue  # skip graphs with a negative cycle
        bf = bellman_ford(n, edges, 0)
        fw = floyd_warshall(n, edges)[0]
        if bf != fw:
            return False
        checked += 1
    return checked == num_trials


if __name__ == "__main__":
    assert verify_bf_vs_fw(num_trials=40, n=6, m=10, seed=1) is True
    assert verify_bf_vs_fw(num_trials=40, n=8, m=16, seed=500) is True
    assert verify_bf_vs_fw(num_trials=20, n=5, m=7, seed=42) is True

    print("All tests passed!")
