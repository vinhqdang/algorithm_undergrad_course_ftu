"""
Problem 08 - Verifying Interval Partitioning Uses the Minimum Number of Resources
====================================================================================

Implement `verify_partitioning_optimal(num_trials, n, seed)`:

For each of `num_trials` random instances of `n` intervals (use
`generate_intervals(n, seed=seed + trial)`), compute:
  - the number of distinct resources used by `interval_partitioning`
    (Problem 7), and
  - the depth of the intervals via `interval_depth` (starter_code.py).

Return True iff these two numbers are EQUAL for every trial. This confirms
the theorem that earliest-start-time-first interval partitioning always uses
exactly `depth` resources, which is provably the minimum possible (no
schedule can use fewer than `depth` resources, since `depth` intervals are
pairwise overlapping at some instant and therefore need `depth` distinct
resources).

See practical_exercises.pdf, Problem 8.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem07 import interval_partitioning
from starter_code import generate_intervals, interval_depth


def verify_partitioning_optimal(num_trials: int = 30, n: int = 10, seed: int = 0) -> bool:
    """Return True iff #resources used by interval_partitioning equals interval_depth, for every trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_partitioning_optimal(num_trials=30, n=10, seed=0) is True
        assert verify_partitioning_optimal(num_trials=10, n=20, seed=100) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
