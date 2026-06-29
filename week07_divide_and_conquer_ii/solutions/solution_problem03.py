"""
Problem 03 - Verify D&C Closest Pair Equals Brute Force (SOLUTION)
=================================================================
"""

import math
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter_code import generate_distinct_points, brute_force_closest  # noqa: E402
from solution_problem02 import closest_pair_dc  # noqa: E402


def verify_closest_pair(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff the D&C and brute-force minimum distances agree.

    Runs ``num_trials`` random instances of ``n`` distinct points, using
    ``generate_distinct_points(n, seed=seed + trial)``.
    """
    for trial in range(num_trials):
        pts = generate_distinct_points(n, seed=seed + trial)
        d_fast, _ = closest_pair_dc(pts)
        d_slow, _ = brute_force_closest(pts)
        if not math.isclose(d_fast, d_slow, rel_tol=1e-12, abs_tol=1e-12):
            return False
    return True


if __name__ == "__main__":
    assert verify_closest_pair(num_trials=30, n=2, seed=1) is True
    assert verify_closest_pair(num_trials=30, n=3, seed=1) is True
    assert verify_closest_pair(num_trials=30, n=15, seed=1) is True
    assert verify_closest_pair(num_trials=20, n=60, seed=999) is True

    print("All tests passed!")
