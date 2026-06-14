"""
Problem 05 - Brute-Force Enumeration of All Stable Matchings (SOLUTION)
=========================================================================
"""

import os
import sys
from itertools import permutations
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_instance, is_stable


def all_stable_matchings(men: List[str], women: List[str], men_prefs, women_prefs) -> List[Dict[str, str]]:
    """Return a list of all stable perfect matchings (dicts man -> woman)."""
    results = []
    for perm in permutations(women):
        matching = dict(zip(men, perm))
        if is_stable(matching, men_prefs, women_prefs):
            results.append(matching)
    return results


if __name__ == "__main__":
    men, women, men_prefs, women_prefs = generate_instance(4, seed=7)
    stable_matchings = all_stable_matchings(men, women, men_prefs, women_prefs)

    assert len(stable_matchings) >= 1
    for matching in stable_matchings:
        assert is_stable(matching, men_prefs, women_prefs)
        assert set(matching.keys()) == set(men)
        assert sorted(matching.values()) == sorted(women)

    print(f"Found {len(stable_matchings)} stable matching(s) for n=4.")
    print("All tests passed!")
