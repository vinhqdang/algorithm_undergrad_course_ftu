"""
Problem 10 - Stress-Testing Interval Partitioning on Random Instances
========================================================================

Implement `random_partitioning_is_valid(n, seed)`:

1. Generate `n` random intervals via `generate_intervals(n, seed=seed)`.
2. Run `interval_partitioning` (Problem 7) to get an assignment of intervals
   to resource ids.
3. Check TWO properties:
   a. For every pair of distinct intervals assigned to the SAME resource,
      they do not overlap.
   b. The set of resource ids used is exactly `{0, 1, ..., k-1}` where `k` is
      the number of distinct resources used (i.e. ids are contiguous from 0,
      no "gaps").

Return True iff both properties hold.

Then implement `stress_test(num_trials, n, seed)` that calls
`random_partitioning_is_valid` for `num_trials` different seeds (e.g.
`seed + trial` for trial in range(num_trials)) and returns True iff ALL of
them return True.

See practical_exercises.pdf, Problem 10.
"""

import os
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem07 import interval_partitioning
from starter_code import generate_intervals

Interval = Tuple[float, float]


def random_partitioning_is_valid(n: int, seed: int) -> bool:
    """Return True iff a random instance's partitioning has no same-resource overlaps and contiguous ids."""
    # TODO: implement this function.
    raise NotImplementedError


def stress_test(num_trials: int = 50, n: int = 15, seed: int = 0) -> bool:
    """Return True iff random_partitioning_is_valid holds for all of num_trials random instances."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert random_partitioning_is_valid(10, seed=1) is True
        assert stress_test(num_trials=50, n=15, seed=0) is True
        assert stress_test(num_trials=20, n=30, seed=200) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
