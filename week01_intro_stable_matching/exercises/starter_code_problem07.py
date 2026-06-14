"""
Problem 07 - Verifying the Men-Optimality Theorem
===================================================

Theorem (Kleinberg & Tardos, Thm 1.7): In the matching produced by the
men-proposing Gale-Shapley algorithm, every man receives the best valid
partner he could have in ANY stable matching ("man-optimal").

A woman w is a *valid partner* of man m if there exists SOME stable matching
in which m and w are matched.

Implement `valid_partners(person, all_stable, role)` returning the set of
valid partners of `person`, where `role` is "man" or "woman", using the list
of all stable matchings from Problem 5.

Then implement `verify_men_optimality(men, men_prefs, all_stable, men_optimal)`
that checks, for every man m, that `men_optimal[m]` is m's most-preferred
valid partner.

See practical_exercises.pdf, Problem 7.
"""

import os
import sys
from typing import Dict, List, Set

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem03 import gale_shapley_men_propose
from solution_problem05 import all_stable_matchings
from starter_code import generate_instance


def valid_partners(person: str, all_stable: List[Dict[str, str]], role: str) -> Set[str]:
    """Return the set of valid partners of `person` (role = 'man' or 'woman')."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_men_optimality(men: List[str], men_prefs, all_stable: List[Dict[str, str]], men_optimal: Dict[str, str]) -> bool:
    """Return True iff every man's partner in `men_optimal` is his most
    preferred valid partner."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for seed in range(5):
            men, women, men_prefs, women_prefs = generate_instance(4, seed=seed)
            all_stable = all_stable_matchings(men, women, men_prefs, women_prefs)
            men_optimal = gale_shapley_men_propose(men_prefs, women_prefs)
            assert verify_men_optimality(men, men_prefs, all_stable, men_optimal)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
