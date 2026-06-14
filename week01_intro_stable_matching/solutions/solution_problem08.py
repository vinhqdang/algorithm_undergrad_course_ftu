"""
Problem 08 - Verifying the Women-Pessimality Theorem (SOLUTION)
=================================================================
"""

import os
import sys
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem03 import gale_shapley_men_propose
from solution_problem05 import all_stable_matchings
from solution_problem07 import valid_partners
from starter_code import generate_instance


def verify_women_pessimality(women: List[str], women_prefs, all_stable: List[Dict[str, str]], men_optimal: Dict[str, str]) -> bool:
    """Return True iff every woman's partner in `men_optimal` is her least
    preferred valid partner."""
    woman_to_man = {w: m for m, w in men_optimal.items()}
    for w in women:
        valid = valid_partners(w, all_stable, "woman")
        worst_valid = max(valid, key=lambda m: women_prefs[w].index(m))
        if woman_to_man[w] != worst_valid:
            return False
    return True


if __name__ == "__main__":
    for seed in range(5):
        men, women, men_prefs, women_prefs = generate_instance(4, seed=seed)
        all_stable = all_stable_matchings(men, women, men_prefs, women_prefs)
        men_optimal = gale_shapley_men_propose(men_prefs, women_prefs)
        assert verify_women_pessimality(women, women_prefs, all_stable, men_optimal)

    print("All tests passed!")
