"""
Problem 03 - Gale-Shapley Algorithm (Men Propose) (SOLUTION)
==============================================================
"""

import os
import sys
from collections import deque
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_instance, is_perfect_matching, is_stable


def gale_shapley_men_propose(men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> Dict[str, str]:
    """Run Gale-Shapley with men proposing. Return a dict man -> woman."""
    free_men = deque(men_prefs.keys())
    next_proposal = {m: 0 for m in men_prefs}  # index of next woman to propose to
    woman_partner: Dict[str, str] = {}  # woman -> current fiance (if engaged)

    while free_men:
        m = free_men.popleft()
        w = men_prefs[m][next_proposal[m]]
        next_proposal[m] += 1

        if w not in woman_partner:
            woman_partner[w] = m
        else:
            m_current = woman_partner[w]
            if women_prefs[w].index(m) < women_prefs[w].index(m_current):
                woman_partner[w] = m
                free_men.append(m_current)
            else:
                free_men.append(m)

    return {m: w for w, m in woman_partner.items()}


if __name__ == "__main__":
    men, women, men_prefs, women_prefs = generate_instance(6, seed=1)
    matching = gale_shapley_men_propose(men_prefs, women_prefs)

    assert is_perfect_matching(matching, men, women), "matching must be perfect"
    assert is_stable(matching, men_prefs, women_prefs), "matching must be stable"

    for seed in range(2, 10):
        men, women, men_prefs, women_prefs = generate_instance(8, seed=seed)
        matching = gale_shapley_men_propose(men_prefs, women_prefs)
        assert is_perfect_matching(matching, men, women)
        assert is_stable(matching, men_prefs, women_prefs)

    print("All tests passed!")
