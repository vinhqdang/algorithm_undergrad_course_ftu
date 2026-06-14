"""
Problem 20 - Stable Matching with Incomplete Preference Lists
=================================================================

In practice, not everyone is acceptable to everyone else. Generalize
Gale-Shapley to INCOMPLETE preference lists: `men_prefs[m]` and
`women_prefs[w]` list only the ACCEPTABLE partners, best first (a person may
have an empty list).

Run the men-proposing algorithm: each man proposes down his list. If he runs
out of acceptable women, he remains permanently single. Women only accept
proposals from men on their own list (a man not on a woman's list is treated
as "less preferred than being single", so she would never accept him --
but since lists only contain mutually-considered pairs in our test data,
you don't need special-case logic beyond "skip men not in my list").

Implement `gale_shapley_incomplete(men, women, men_prefs, women_prefs)` ->
dict of man -> woman, containing ONLY the matched pairs (unmatched men/women
are simply absent).

See practical_exercises.pdf, Problem 20.
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
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        men = ["M0", "M1"]
        women = ["W0", "W1"]
        men_prefs = {
            "M0": ["W0"],          # M0 finds only W0 acceptable
            "M1": ["W0", "W1"],
        }
        women_prefs = {
            "W0": ["M1", "M0"],
            "W1": ["M1"],           # W1 finds only M1 acceptable
        }

        matching = gale_shapley_incomplete(men, women, men_prefs, women_prefs)

        # M1 ends up with W0 (W0 prefers M1 over M0); M0 and W1 stay single.
        assert matching == {"M1": "W0"}, matching

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
