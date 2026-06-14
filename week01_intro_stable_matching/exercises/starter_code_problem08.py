"""
Problem 08 - Verifying the Women-Pessimality Theorem
======================================================

Theorem (Kleinberg & Tardos, Thm 1.8): In the matching produced by the
men-proposing Gale-Shapley algorithm, every woman is matched with her LEAST
preferred valid partner ("woman-pessimal").

Using `valid_partners` from Problem 7, implement
`verify_women_pessimality(women, women_prefs, all_stable, men_optimal)` that
checks, for every woman w, that her partner in `men_optimal` is her LEAST
preferred valid partner.

See practical_exercises.pdf, Problem 8.
"""

import os
import sys
from typing import Dict, List

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem03 import gale_shapley_men_propose
from solution_problem05 import all_stable_matchings
from solution_problem07 import valid_partners
from starter_code import generate_instance


def verify_women_pessimality(women: List[str], women_prefs, all_stable: List[Dict[str, str]], men_optimal: Dict[str, str]) -> bool:
    """Return True iff every woman's partner in `men_optimal` is her least
    preferred valid partner."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for seed in range(5):
            men, women, men_prefs, women_prefs = generate_instance(4, seed=seed)
            all_stable = all_stable_matchings(men, women, men_prefs, women_prefs)
            men_optimal = gale_shapley_men_propose(men_prefs, women_prefs)
            assert verify_women_pessimality(women, women_prefs, all_stable, men_optimal)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
