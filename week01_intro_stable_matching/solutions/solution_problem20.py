"""
Problem 20 - Stable Matching with Incomplete Preference Lists (SOLUTION)
===========================================================================
"""

from collections import deque
from typing import Dict, List


def gale_shapley_incomplete(
    men: List[str],
    women: List[str],
    men_prefs: Dict[str, List[str]],
    women_prefs: Dict[str, List[str]],
) -> Dict[str, str]:
    """Return a stable matching (man -> woman) allowing some to remain single."""
    free_men = deque(men)
    next_proposal = {m: 0 for m in men}
    woman_partner: Dict[str, str] = {}

    while free_men:
        m = free_men.popleft()
        if next_proposal[m] >= len(men_prefs[m]):
            continue  # m has exhausted his list; stays single

        w = men_prefs[m][next_proposal[m]]
        next_proposal[m] += 1

        if m not in women_prefs.get(w, []):
            free_men.append(m)  # w does not consider m acceptable
            continue

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
    men = ["M0", "M1"]
    women = ["W0", "W1"]
    men_prefs = {
        "M0": ["W0"],
        "M1": ["W0", "W1"],
    }
    women_prefs = {
        "W0": ["M1", "M0"],
        "W1": ["M1"],
    }

    matching = gale_shapley_incomplete(men, women, men_prefs, women_prefs)
    assert matching == {"M1": "W0"}, matching

    print("All tests passed!")
