"""
Problem 01 - Feasibility Checker for Interval Selections
==========================================================

Implement `is_feasible_scratch(selection)` WITHOUT using `is_feasible` from
starter_code.py (this is a from-scratch warm-up exercise).

A list of intervals `selection` (each a tuple (start, finish)) is *feasible*
iff no two intervals overlap. Two intervals (s1, f1) and (s2, f2) overlap iff
s1 < f2 and s2 < f1. Intervals that merely touch at an endpoint (one finishes
exactly when the other starts) do NOT count as overlapping.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

from typing import List, Tuple

Interval = Tuple[float, float]


def is_feasible_scratch(selection: List[Interval]) -> bool:
    """Return True iff no two intervals in `selection` overlap."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Disjoint intervals
        assert is_feasible_scratch([(0, 2), (2, 4), (5, 7)]) is True

        # Overlapping intervals
        assert is_feasible_scratch([(0, 3), (2, 5)]) is False

        # Touching at an endpoint is fine
        assert is_feasible_scratch([(1, 3), (3, 6)]) is True

        # Single interval, empty selection
        assert is_feasible_scratch([(0, 1)]) is True
        assert is_feasible_scratch([]) is True

        # Nested intervals overlap
        assert is_feasible_scratch([(0, 10), (2, 4)]) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
