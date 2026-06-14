"""
Problem 07 - Verifying the Men-Optimality Theorem (SOLUTION)
==============================================================
"""

import os
import sys
from typing import Dict, List, Set

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem03 import gale_shapley_men_propose
from solution_problem05 import all_stable_matchings
from starter_code import generate_instance


def valid_partners(person: str, all_stable: List[Dict[str, str]], role: str) -> Set[str]:
    """Return the set of valid partners of `person` (role = 'man' or 'woman')."""
    partners = set()
    for matching in all_stable:
        if role == "man":
            partners.add(matching[person])
        else:  # role == "woman"
            woman_to_man = {w: m for m, w in matching.items()}
            partners.add(woman_to_man[person])
    return partners


def verify_men_optimality(men: List[str], men_prefs, all_stable: List[Dict[str, str]], men_optimal: Dict[str, str]) -> bool:
    """Return True iff every man's partner in `men_optimal` is his most
    preferred valid partner."""
    for m in men:
        valid = valid_partners(m, all_stable, "man")
        best_valid = min(valid, key=lambda w: men_prefs[m].index(w))
        if men_optimal[m] != best_valid:
            return False
    return True


if __name__ == "__main__":
    for seed in range(5):
        men, women, men_prefs, women_prefs = generate_instance(4, seed=seed)
        all_stable = all_stable_matchings(men, women, men_prefs, women_prefs)
        men_optimal = gale_shapley_men_propose(men_prefs, women_prefs)
        assert verify_men_optimality(men, men_prefs, all_stable, men_optimal)

    print("All tests passed!")
