"""
Problem 01 - Feasibility Checker for Interval Selections (SOLUTION)
=====================================================================
"""

from typing import List, Tuple

Interval = Tuple[float, float]


def is_feasible_scratch(selection: List[Interval]) -> bool:
    """Return True iff no two intervals in `selection` overlap."""
    sorted_sel = sorted(selection)
    for i in range(len(sorted_sel) - 1):
        _, f_cur = sorted_sel[i]
        s_next, _ = sorted_sel[i + 1]
        if s_next < f_cur:
            return False
    return True


if __name__ == "__main__":
    assert is_feasible_scratch([(0, 2), (2, 4), (5, 7)]) is True
    assert is_feasible_scratch([(0, 3), (2, 5)]) is False
    assert is_feasible_scratch([(1, 3), (3, 6)]) is True
    assert is_feasible_scratch([(0, 1)]) is True
    assert is_feasible_scratch([]) is True
    assert is_feasible_scratch([(0, 10), (2, 4)]) is False

    print("All tests passed!")
