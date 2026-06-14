"""
Problem 03 - Gale-Shapley Algorithm (Men Propose)
===================================================

Implement the classic Gale-Shapley algorithm where men propose:

  Initialize all m in M and w in W to free.
  While some man m is free and hasn't proposed to every woman:
      w = first woman on m's list to whom m has not yet proposed
      if w is free:
          (m, w) become engaged
      else if w prefers m to her current partner m':
          m' becomes free; (m, w) become engaged
      else:
          w rejects m

Return the resulting matching as a dict man -> woman.

See practical_exercises.pdf, Problem 3.
"""

import os
import sys
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_instance, is_perfect_matching, is_stable


def gale_shapley_men_propose(men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> Dict[str, str]:
    """Run Gale-Shapley with men proposing. Return a dict man -> woman."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        men, women, men_prefs, women_prefs = generate_instance(6, seed=1)
        matching = gale_shapley_men_propose(men_prefs, women_prefs)

        assert is_perfect_matching(matching, men, women), "matching must be perfect"
        assert is_stable(matching, men_prefs, women_prefs), "matching must be stable"

        # Run on a few more random instances for good measure.
        for seed in range(2, 10):
            men, women, men_prefs, women_prefs = generate_instance(8, seed=seed)
            matching = gale_shapley_men_propose(men_prefs, women_prefs)
            assert is_perfect_matching(matching, men, women)
            assert is_stable(matching, men_prefs, women_prefs)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
