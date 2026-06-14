"""
Problem 02 - Stability Checker (SOLUTION)
==========================================
"""

from typing import Dict, List, Tuple


def find_rogue_couples(
    matching: Dict[str, str],
    men_prefs: Dict[str, List[str]],
    women_prefs: Dict[str, List[str]],
) -> List[Tuple[str, str]]:
    """Return a list of (man, woman) rogue couples for `matching`."""
    woman_to_man = {w: m for m, w in matching.items()}
    rogues = []
    for m, w_current in matching.items():
        m_rank_current = men_prefs[m].index(w_current)
        for w in men_prefs[m][:m_rank_current]:  # women m prefers to w_current
            m_alt = woman_to_man[w]
            if women_prefs[w].index(m) < women_prefs[w].index(m_alt):
                rogues.append((m, w))
    return rogues


def is_stable(matching, men_prefs, women_prefs) -> bool:
    """Return True iff `matching` has no rogue couples."""
    return len(find_rogue_couples(matching, men_prefs, women_prefs)) == 0


if __name__ == "__main__":
    men_prefs = {
        "M0": ["W0", "W1"],
        "M1": ["W0", "W1"],
    }
    women_prefs = {
        "W0": ["M0", "M1"],
        "W1": ["M0", "M1"],
    }

    stable_matching = {"M0": "W0", "M1": "W1"}
    assert find_rogue_couples(stable_matching, men_prefs, women_prefs) == []
    assert is_stable(stable_matching, men_prefs, women_prefs) is True

    unstable_matching = {"M0": "W1", "M1": "W0"}
    rogues = find_rogue_couples(unstable_matching, men_prefs, women_prefs)
    assert ("M0", "W0") in rogues
    assert is_stable(unstable_matching, men_prefs, women_prefs) is False

    print("All tests passed!")
