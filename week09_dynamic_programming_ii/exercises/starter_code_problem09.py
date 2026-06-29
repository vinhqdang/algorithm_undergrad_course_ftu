"""
Problem 09 - Verify Bellman-Ford Agrees with Floyd-Warshall
============================================================

Implement `verify_bf_vs_fw(num_trials, n, m, seed)`: for each of `num_trials`
random graphs (via generate_weighted_graph) that contain NO negative cycle (skip
those that do, using Problem 7's find_negative_cycle), check that for source 0,
bellman_ford(n, edges, 0) equals row 0 of floyd_warshall(n, edges). Return True
iff they always agree.

This problem reuses your solutions to Problems 6, 7 and 8 (imported from the
sibling starter files below).

See practical_exercises.pdf, Problem 9, for the full statement and examples.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from starter_code import generate_weighted_graph

from starter_code_problem06 import bellman_ford
from starter_code_problem07 import find_negative_cycle
from starter_code_problem08 import floyd_warshall


def verify_bf_vs_fw(num_trials: int, n: int, m: int, seed: int) -> bool:
    """On random negative-cycle-free graphs, BF from source 0 must equal FW row 0."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_bf_vs_fw(num_trials=40, n=6, m=10, seed=1) is True
        assert verify_bf_vs_fw(num_trials=40, n=8, m=16, seed=500) is True
        assert verify_bf_vs_fw(num_trials=20, n=5, m=7, seed=42) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
