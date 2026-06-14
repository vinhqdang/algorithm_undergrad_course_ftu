"""
Problem 04 - Gale-Shapley Algorithm (Women Propose) (SOLUTION)
================================================================
"""

import os
import sys
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem03 import gale_shapley_men_propose
from starter_code import generate_instance, is_perfect_matching, is_stable


def gale_shapley_women_propose(men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> Dict[str, str]:
    """Run Gale-Shapley with women proposing. Return a dict man -> woman."""
    # Swap roles: women_prefs becomes the "proposer" preference dict.
    woman_optimal_for_women = gale_shapley_men_propose(women_prefs, men_prefs)
    # woman_optimal_for_women maps woman -> man; flip to man -> woman.
    return {m: w for w, m in woman_optimal_for_women.items()}


if __name__ == "__main__":
    men, women, men_prefs, women_prefs = generate_instance(8, seed=42)

    men_optimal = gale_shapley_men_propose(men_prefs, women_prefs)
    women_optimal = gale_shapley_women_propose(men_prefs, women_prefs)

    assert is_perfect_matching(women_optimal, men, women)
    assert is_stable(women_optimal, men_prefs, women_prefs)

    for m in men:
        r_men_optimal = men_prefs[m].index(men_optimal[m])
        r_women_optimal = men_prefs[m].index(women_optimal[m])
        assert r_men_optimal <= r_women_optimal

    print("All tests passed!")
