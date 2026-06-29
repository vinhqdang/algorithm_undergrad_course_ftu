"""
Problem 07 - Verify Edmonds-Karp and Ford-Fulkerson Agree (SOLUTION)
======================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem05 import edmonds_karp
from solution_problem06 import ford_fulkerson
from starter_code import generate_flow_network


def verify_algorithms_agree(num_trials: int = 50, n: int = 8, seed: int = 0) -> bool:
    """Return True iff Edmonds-Karp and DFS Ford-Fulkerson compute the same
    max-flow value on every random network.

    The Max-Flow Min-Cut theorem guarantees the maximum flow value is unique
    (it equals the minimum cut capacity), so *any* correct augmenting-path
    method must agree on the value regardless of the path-selection rule.
    """
    for trial in range(num_trials):
        # Build two independent copies of the SAME network so the in-place
        # flow mutations of one algorithm do not affect the other.
        g1 = generate_flow_network(n, seed=seed + trial)
        g2 = g1.copy()
        if edmonds_karp(g1) != ford_fulkerson(g2):
            return False
    return True


if __name__ == "__main__":
    assert verify_algorithms_agree(num_trials=50, n=8, seed=0) is True
    assert verify_algorithms_agree(num_trials=30, n=12, seed=1000) is True
    assert verify_algorithms_agree(num_trials=20, n=6, seed=7) is True

    print("All tests passed!")
