"""
Problem 02 - Stability Checker
================================

Implement `find_rogue_couples(matching, men_prefs, women_prefs)` WITHOUT using
the helper from starter_code.py (from-scratch warm-up exercise).

A pair (m, w) is a *rogue couple* (a.k.a. blocking pair) for `matching` if:
  - m and w are NOT matched to each other, AND
  - m prefers w to his current partner, AND
  - w prefers m to her current partner.

`find_rogue_couples` should return a list of all such (m, w) pairs.
A matching is *stable* iff this list is empty.

See practical_exercises.pdf, Problem 2, for the full statement and examples.
"""

from typing import Dict, List, Tuple


def find_rogue_couples(
    matching: Dict[str, str],
    men_prefs: Dict[str, List[str]],
    women_prefs: Dict[str, List[str]],
) -> List[Tuple[str, str]]:
    """Return a list of (man, woman) rogue couples for `matching`."""
    # TODO: implement this function.
    raise NotImplementedError


def is_stable(matching, men_prefs, women_prefs) -> bool:
    """Return True iff `matching` has no rogue couples."""
    return len(find_rogue_couples(matching, men_prefs, women_prefs)) == 0


if __name__ == "__main__":
    try:
        # Both men and both women agree W0 > W1 and M0 > M1 respectively.
        men_prefs = {
            "M0": ["W0", "W1"],
            "M1": ["W0", "W1"],
        }
        women_prefs = {
            "W0": ["M0", "M1"],
            "W1": ["M0", "M1"],
        }

        # The unique stable matching: everyone gets their top choice.
        stable_matching = {"M0": "W0", "M1": "W1"}
        assert find_rogue_couples(stable_matching, men_prefs, women_prefs) == []
        assert is_stable(stable_matching, men_prefs, women_prefs) is True

        # Swapped: M0 and W0 both prefer each other to their current partners.
        unstable_matching = {"M0": "W1", "M1": "W0"}
        rogues = find_rogue_couples(unstable_matching, men_prefs, women_prefs)
        assert ("M0", "W0") in rogues
        assert is_stable(unstable_matching, men_prefs, women_prefs) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
