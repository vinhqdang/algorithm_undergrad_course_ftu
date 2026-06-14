"""
Problem 04 - Gale-Shapley Algorithm (Women Propose)
=====================================================

By symmetry with Problem 3, implement `gale_shapley_women_propose`, where the
roles of men and women are swapped: women propose to men, and men hold the
best offer received so far.

Return the resulting matching as a dict man -> woman (same orientation as
Problem 3, to make the two results directly comparable).

See practical_exercises.pdf, Problem 4.
"""

import os
import sys
from typing import Dict, List

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem03 import gale_shapley_men_propose
from starter_code import generate_instance, is_perfect_matching, is_stable


def gale_shapley_women_propose(men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> Dict[str, str]:
    """Run Gale-Shapley with women proposing. Return a dict man -> woman."""
    # TODO: implement this function (hint: reuse gale_shapley_men_propose with
    # the roles of men_prefs and women_prefs swapped, then flip the result).
    raise NotImplementedError


if __name__ == "__main__":
    try:
        men, women, men_prefs, women_prefs = generate_instance(8, seed=42)

        men_optimal = gale_shapley_men_propose(men_prefs, women_prefs)
        women_optimal = gale_shapley_women_propose(men_prefs, women_prefs)

        assert is_perfect_matching(women_optimal, men, women)
        assert is_stable(women_optimal, men_prefs, women_prefs)

        # Every man should do at least as well under men_optimal as under
        # women_optimal (lower rank number = more preferred).
        for m in men:
            r_men_optimal = men_prefs[m].index(men_optimal[m])
            r_women_optimal = men_prefs[m].index(women_optimal[m])
            assert r_men_optimal <= r_women_optimal

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
