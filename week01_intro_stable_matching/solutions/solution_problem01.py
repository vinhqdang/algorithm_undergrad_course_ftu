"""
Problem 01 - Perfect Matching Checker (SOLUTION)
=================================================
"""

from typing import Dict, List


def is_perfect_matching(matching: Dict[str, str], men: List[str], women: List[str]) -> bool:
    """Return True iff `matching` is a perfect matching between men and women."""
    if set(matching.keys()) != set(men):
        return False
    if sorted(matching.values()) != sorted(women):
        return False
    return True


if __name__ == "__main__":
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
