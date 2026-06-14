"""
Problem 22 - Trace-Based Verification on a Textbook Example
==============================================================

Consider the classic 3x3 instance (Kleinberg & Tardos, Chapter 1):

  Men's preferences (best first):     Women's preferences (best first):
    X: A, B, C                          A: Y, X, Z
    Y: B, A, C                          B: X, Y, Z
    Z: A, B, C                          C: X, Y, Z

Implement `build_instance()` returning (men, women, men_prefs, women_prefs)
for this instance, where men = ["X", "Y", "Z"] and women = ["A", "B", "C"].

Using `gale_shapley_men_propose` from Problem 3, the men-proposing algorithm
on this instance produces the matching {X: A, Y: B, Z: C} (you can verify
this by hand-tracing the algorithm -- see practical_exercises.pdf for the
full trace table). Note that Z, the only man rejected along the way, ends
up with his LAST choice C.

Implement `verify_textbook_example()` that builds the instance, runs
Gale-Shapley, and returns True iff the result equals {"X": "A", "Y": "B", "Z": "C"}.

See practical_exercises.pdf, Problem 22.
"""

import os
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem03 import gale_shapley_men_propose


def build_instance() -> Tuple[List[str], List[str], Dict[str, List[str]], Dict[str, List[str]]]:
    """Return (men, women, men_prefs, women_prefs) for the textbook example."""
    # TODO: implement.
    raise NotImplementedError


def verify_textbook_example() -> bool:
    """Return True iff Gale-Shapley on build_instance() gives {"X": "B", "Y": "A", "Z": "C"}."""
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_textbook_example() is True
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
