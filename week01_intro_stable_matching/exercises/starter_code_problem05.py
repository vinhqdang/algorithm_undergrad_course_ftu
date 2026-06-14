"""
Problem 05 - Brute-Force Enumeration of All Stable Matchings
==============================================================

For small n, implement `all_stable_matchings(men, women, men_prefs, women_prefs)`
that returns a list of ALL stable perfect matchings, by:
  1. Generating every possible perfect matching (every permutation of `women`
     assigned to `men`, i.e. n! candidates).
  2. Keeping only those that are stable (no rogue couples).

This is exponential and only intended for small n (n <= 6 or so) -- it exists
to let us empirically verify properties of Gale-Shapley in later problems.

See practical_exercises.pdf, Problem 5.
"""

import os
import sys
from itertools import permutations
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_instance, is_stable


def all_stable_matchings(men: List[str], women: List[str], men_prefs, women_prefs) -> List[Dict[str, str]]:
    """Return a list of all stable perfect matchings (dicts man -> woman)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        men, women, men_prefs, women_prefs = generate_instance(4, seed=7)
        stable_matchings = all_stable_matchings(men, women, men_prefs, women_prefs)

        # There is always at least one stable matching (Gale-Shapley proves this).
        assert len(stable_matchings) >= 1
        for matching in stable_matchings:
            assert is_stable(matching, men_prefs, women_prefs)
            assert set(matching.keys()) == set(men)
            assert sorted(matching.values()) == sorted(women)

        print(f"Found {len(stable_matchings)} stable matching(s) for n=4.")
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
