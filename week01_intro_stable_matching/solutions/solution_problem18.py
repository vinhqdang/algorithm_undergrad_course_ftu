"""
Problem 18 - Empirical Running Time of Gale-Shapley (SOLUTION)
=================================================================
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
    free_men = deque(men_prefs.keys())
    next_proposal = {m: 0 for m in men_prefs}
    woman_partner: Dict[str, str] = {}
    proposals = 0

    while free_men:
        m = free_men.popleft()
        w = men_prefs[m][next_proposal[m]]
        next_proposal[m] += 1
        proposals += 1

        if w not in woman_partner:
            woman_partner[w] = m
        else:
            m_current = woman_partner[w]
            if women_prefs[w].index(m) < women_prefs[w].index(m_current):
                woman_partner[w] = m
                free_men.append(m_current)
            else:
                free_men.append(m)

    return proposals


def average_proposals(n: int, num_trials: int = 20, seed: int = 0) -> float:
    """Average number of proposals over `num_trials` random instances of size n."""
    totals = []
    for trial in range(num_trials):
        _, _, men_prefs, women_prefs = generate_instance(n, seed=seed + trial)
        totals.append(count_proposals(men_prefs, women_prefs))
    return mean(totals)


if __name__ == "__main__":
    for n in [4, 8, 16, 32]:
        avg = average_proposals(n, num_trials=30, seed=0)
        assert n - 1 <= avg <= n * n, (n, avg)
        print(f"n={n}: average proposals = {avg:.1f} (n^2 = {n * n})")

    print("All tests passed!")
