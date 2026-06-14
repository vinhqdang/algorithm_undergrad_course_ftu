"""
Problem 18 - Empirical Running Time of Gale-Shapley
=====================================================

Implement `count_proposals(men_prefs, women_prefs)`, a variant of the
men-proposing Gale-Shapley algorithm (Problem 3) that returns the TOTAL
number of proposals made (instead of the final matching).

The Kleinberg-Tardos textbook proves this is at most n^2. Implement
`average_proposals(n, num_trials, seed)` returning the average number of
proposals over `num_trials` random instances of size n, and verify it never
exceeds n^2.

See practical_exercises.pdf, Problem 18.
"""

import os
import sys
from collections import deque
from statistics import mean
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_instance


def count_proposals(men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> int:
    """Run men-proposing Gale-Shapley and return the total number of proposals made."""
    # TODO: implement (same algorithm as Problem 3, but count proposals).
    raise NotImplementedError


def average_proposals(n: int, num_trials: int = 20, seed: int = 0) -> float:
    """Average number of proposals over `num_trials` random instances of size n."""
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for n in [4, 8, 16, 32]:
            avg = average_proposals(n, num_trials=30, seed=0)
            assert n - 1 <= avg <= n * n, (n, avg)
            print(f"n={n}: average proposals = {avg:.1f} (n^2 = {n * n})")

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
