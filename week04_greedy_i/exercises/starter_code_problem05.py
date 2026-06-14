"""
Problem 05 - Verifying Optimality of Earliest-Finish-Time-First
==================================================================

Implement `verify_eft_optimal(num_trials, n, seed)`:

For each of `num_trials` random instances of `n` intervals (use
`generate_intervals(n, seed=seed + trial)` from starter_code.py), compute:
  - the greedy result via `earliest_finish_time_first` (Problem 3), and
  - the brute-force optimum via `brute_force_max_independent_set` (Problem 4).

Return True iff, for every trial, the greedy result has the SAME SIZE as the
brute-force optimum (the greedy is optimal in terms of the number of
intervals selected -- it need not be the *same set*, since multiple optima
may exist).

Keep `n` small (e.g. <= 10) since brute force is exponential.

See practical_exercises.pdf, Problem 5.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem03 import earliest_finish_time_first
from solution_problem04 import brute_force_max_independent_set
from starter_code import generate_intervals


def verify_eft_optimal(num_trials: int = 30, n: int = 8, seed: int = 0) -> bool:
    """Return True iff EFT matches the brute-force optimum size on every trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_eft_optimal(num_trials=30, n=8, seed=0) is True
        # Also test on slightly larger instances.
        assert verify_eft_optimal(num_trials=10, n=10, seed=100) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
