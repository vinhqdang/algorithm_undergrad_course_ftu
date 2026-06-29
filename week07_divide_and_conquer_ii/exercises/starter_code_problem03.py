"""
Problem 03 - Verify D&C Closest Pair Equals Brute Force
=======================================================

Implement `verify_closest_pair(num_trials, n, seed)`: for each of
``num_trials`` random instances of ``n`` distinct points
(``generate_distinct_points(n, seed=seed + trial)``), compute the minimum
distance from the divide-and-conquer algorithm (Problem 2) and from the
brute-force baseline (``brute_force_closest`` in starter_code.py). Return
``True`` iff they agree on every trial.

This is the standard "fast vs. slow" empirical correctness check.

See practical_exercises.pdf, Problem 3.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from starter_code import generate_distinct_points, brute_force_closest  # noqa: E402
from solution_problem02 import closest_pair_dc  # noqa: E402


def verify_closest_pair(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff the D&C and brute-force minimum distances agree."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_closest_pair(num_trials=30, n=2, seed=1) is True
        assert verify_closest_pair(num_trials=30, n=3, seed=1) is True
        assert verify_closest_pair(num_trials=30, n=15, seed=1) is True
        assert verify_closest_pair(num_trials=20, n=60, seed=999) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
