"""
Problem 01 - Perfect Matching Checker
======================================

Implement `is_perfect_matching(matching, men, women)` WITHOUT using the
helper from starter_code.py (this is a from-scratch warm-up exercise).

A matching (dict man -> woman) is *perfect* iff:
  1. Every man in `men` appears exactly once as a key.
  2. Every woman in `women` appears exactly once as a value.
  i.e. the matching is a bijection between `men` and `women`.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

from typing import Dict, List


def is_perfect_matching(matching: Dict[str, str], men: List[str], women: List[str]) -> bool:
    """Return True iff `matching` is a perfect matching between men and women."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        men = ["M0", "M1", "M2"]
        women = ["W0", "W1", "W2"]

        perfect = {"M0": "W1", "M1": "W0", "M2": "W2"}
        assert is_perfect_matching(perfect, men, women) is True

        missing_man = {"M0": "W1", "M1": "W0"}
        assert is_perfect_matching(missing_man, men, women) is False

        duplicate_woman = {"M0": "W1", "M1": "W1", "M2": "W2"}
        assert is_perfect_matching(duplicate_woman, men, women) is False

        unknown_woman = {"M0": "W3", "M1": "W0", "M2": "W2"}
        assert is_perfect_matching(unknown_woman, men, women) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
