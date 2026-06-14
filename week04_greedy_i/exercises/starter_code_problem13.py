"""
Problem 13 - Verifying Optimality of Earliest-Deadline-First
================================================================

Implement `verify_edf_optimal(num_trials, n, seed)`:

For each of `num_trials` random instances of `n` jobs (use
`generate_jobs(n, seed=seed + trial)` from starter_code.py), compute:
  - the max lateness achieved by `earliest_deadline_first` (Problem 11), and
  - the optimal max lateness via `brute_force_min_lateness` (Problem 12).

Return True iff these two values are equal (up to floating-point tolerance,
e.g. `abs(a - b) < 1e-9`) for every trial.

Keep `n` small (e.g. <= 7) since brute force is factorial-time.

See practical_exercises.pdf, Problem 13.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem11 import earliest_deadline_first
from solution_problem12 import brute_force_min_lateness
from starter_code import generate_jobs


def verify_edf_optimal(num_trials: int = 30, n: int = 6, seed: int = 0) -> bool:
    """Return True iff EDF's max lateness equals the brute-force optimum, for every trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_edf_optimal(num_trials=30, n=6, seed=0) is True
        assert verify_edf_optimal(num_trials=10, n=7, seed=100) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
