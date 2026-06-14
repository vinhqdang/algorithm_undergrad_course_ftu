"""
Problem 22 - Trace-Based Verification on a Textbook Example (SOLUTION)
=========================================================================
"""

from typing import Dict, List, Tuple

from solution_problem03 import gale_shapley_men_propose


def build_instance() -> Tuple[List[str], List[str], Dict[str, List[str]], Dict[str, List[str]]]:
    """Return (men, women, men_prefs, women_prefs) for the textbook example."""
    men = ["X", "Y", "Z"]
    women = ["A", "B", "C"]
    men_prefs = {
        "X": ["A", "B", "C"],
        "Y": ["B", "A", "C"],
        "Z": ["A", "B", "C"],
    }
    women_prefs = {
        "A": ["Y", "X", "Z"],
        "B": ["X", "Y", "Z"],
        "C": ["X", "Y", "Z"],
    }
    return men, women, men_prefs, women_prefs


def verify_textbook_example() -> bool:
    """Return True iff Gale-Shapley on build_instance() gives {"X": "A", "Y": "B", "Z": "C"}."""
    _, _, men_prefs, women_prefs = build_instance()
    matching = gale_shapley_men_propose(men_prefs, women_prefs)
    return matching == {"X": "A", "Y": "B", "Z": "C"}


if __name__ == "__main__":
    assert verify_textbook_example() is True
    print("All tests passed!")
