"""
Problem 12 - Integrality of the Computed Flow
===============================================

The Integrality Theorem states: if all edge capacities are integers, then the
max flow found by an augmenting-path algorithm assigns an INTEGER flow to every
edge (each augmentation pushes an integer bottleneck, starting from the all-zero
integral flow).

Implement ``flow_is_integral(network)``: assuming a flow has been computed,
return True iff every original forward edge carries an integer flow.

Implement ``verify_integrality(num_trials, n, seed)``: for each random network
(integer capacities), compute the max flow, then check the flow is integral on
every edge and the total value is itself an integer. Return True iff this holds
on every trial.

See practical_exercises.pdf, Problem 12, for the full statement and examples.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_flow_network

# from starter_code_problem05 import edmonds_karp


def flow_is_integral(network, tol: float = 1e-9) -> bool:
    """Return True iff every original forward edge carries an integer flow."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_integrality(num_trials: int = 50, n: int = 8, seed: int = 0) -> bool:
    """Return True iff the computed max flow is integral on every edge of every
    random network."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_integrality(num_trials=50, n=8, seed=0) is True
        assert verify_integrality(num_trials=30, n=12, seed=999) is True
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
