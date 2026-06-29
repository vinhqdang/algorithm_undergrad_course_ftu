"""
Problem 12 - Integrality of the Computed Flow (SOLUTION)
=========================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem05 import edmonds_karp
from starter_code import generate_flow_network


def flow_is_integral(network, tol: float = 1e-9) -> bool:
    """Return True iff every edge of `network` carries an integer flow.

    Assumes a flow has already been computed (e.g. by edmonds_karp). Checks
    only the original forward edges (the reverse residual edges carry the
    negated flow, which is integral iff the forward flow is).
    """
    for e in network.forward_edges():
        if abs(e.flow - round(e.flow)) > tol:
            return False
    return True


def verify_integrality(num_trials: int = 50, n: int = 8, seed: int = 0) -> bool:
    """Integrality Theorem check: with integer capacities, the max flow found
    by an augmenting-path algorithm is integral on every edge.

    Each augmentation pushes the bottleneck residual capacity, which (starting
    from the all-zero integral flow, with integer capacities) is always an
    integer; hence the flow stays integral throughout. Returns True iff every
    edge carries an integer flow on every random instance, AND the total value
    is itself an integer.
    """
    for trial in range(num_trials):
        g = generate_flow_network(n, seed=seed + trial, max_capacity=12)
        value = edmonds_karp(g)
        if not flow_is_integral(g):
            return False
        if abs(value - round(value)) > 1e-9:
            return False
    return True


if __name__ == "__main__":
    # Direct check on a fixed instance.
    g = generate_flow_network(8, seed=3)
    edmonds_karp(g)
    assert flow_is_integral(g) is True
    for e in g.forward_edges():
        assert float(e.flow).is_integer(), e

    # Many random instances.
    assert verify_integrality(num_trials=50, n=8, seed=0) is True
    assert verify_integrality(num_trials=30, n=12, seed=999) is True
    assert verify_integrality(num_trials=20, n=6, seed=42) is True

    print("All tests passed!")
