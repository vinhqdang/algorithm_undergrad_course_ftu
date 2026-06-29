"""
Problem 03 - Reconstruct an Optimal Alignment
==============================================

Implement `align(x, y, gap, mismatch)` returning (cost, ax, ay) where `ax` and
`ay` are the two input strings padded with the gap symbol '-' so they have equal
length and represent an optimal alignment (same cost as Problem 2). Fill the DP
table, then trace back from (m, n) to (0, 0), emitting one column per step.

See practical_exercises.pdf, Problem 3, for the full statement and examples.
"""

from typing import Tuple


def align(x: str, y: str, gap: float, mismatch: float) -> Tuple[float, str, str]:
    """Return (cost, ax, ay): an optimal alignment of x and y with gap symbols '-'."""
    # TODO: implement this function.
    raise NotImplementedError


def _alignment_columns_cost(ax: str, ay: str, gap: float, mismatch: float) -> float:
    """Recompute the cost of an alignment directly from its columns (for testing)."""
    total = 0.0
    for a, b in zip(ax, ay):
        if a == "-" or b == "-":
            total += gap
        elif a != b:
            total += mismatch
    return total


def _check(x, y, gap, mismatch):
    cost, ax, ay = align(x, y, gap, mismatch)
    assert len(ax) == len(ay)
    assert ax.replace("-", "") == x
    assert ay.replace("-", "") == y
    assert all(not (a == "-" and b == "-") for a, b in zip(ax, ay))
    assert _alignment_columns_cost(ax, ay, gap, mismatch) == cost


if __name__ == "__main__":
    try:
        _check("AT", "AAT", 1, 1)
        _check("kitten", "sitting", 1, 1)
        _check("abc", "abc", 5, 5)
        _check("", "abc", 2, 1)
        _check("AGGTAB", "GXTXAYB", 2, 3)
        _check("hello", "world", 1, 1)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
