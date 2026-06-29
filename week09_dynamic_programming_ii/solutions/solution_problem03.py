"""
Problem 03 - Reconstruct an Optimal Alignment (SOLUTION)
==========================================================
"""

import os
import sys
from typing import Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def align(x: str, y: str, gap: float, mismatch: float) -> Tuple[float, str, str]:
    """Return (cost, ax, ay): an optimal alignment of x and y with gap symbols '-'."""
    m, n = len(x), len(y)
    dp = [[0.0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i * gap
    for j in range(n + 1):
        dp[0][j] = j * gap
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost_diag = 0.0 if x[i - 1] == y[j - 1] else mismatch
            dp[i][j] = min(
                dp[i - 1][j - 1] + cost_diag,
                dp[i - 1][j] + gap,
                dp[i][j - 1] + gap,
            )

    # Trace back from (m, n) to (0, 0)
    ax_parts, ay_parts = [], []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            cost_diag = 0.0 if x[i - 1] == y[j - 1] else mismatch
            if dp[i][j] == dp[i - 1][j - 1] + cost_diag:
                ax_parts.append(x[i - 1])
                ay_parts.append(y[j - 1])
                i, j = i - 1, j - 1
                continue
        if i > 0 and dp[i][j] == dp[i - 1][j] + gap:
            ax_parts.append(x[i - 1])
            ay_parts.append("-")
            i -= 1
        else:
            ay_parts.append(y[j - 1])
            ax_parts.append("-")
            j -= 1

    ax = "".join(reversed(ax_parts))
    ay = "".join(reversed(ay_parts))
    return dp[m][n], ax, ay


def _check(x, y, gap, mismatch):
    from solution_problem02 import alignment_cost

    cost, ax, ay = align(x, y, gap, mismatch)
    assert len(ax) == len(ay)
    # Aligned strings, with gaps removed, must recover the originals
    assert ax.replace("-", "") == x
    assert ay.replace("-", "") == y
    # No column is two gaps
    assert all(not (a == "-" and b == "-") for a, b in zip(ax, ay))
    # Recompute the cost from the alignment columns and compare to Problem 2
    computed = 0.0
    for a, b in zip(ax, ay):
        if a == "-" or b == "-":
            computed += gap
        elif a != b:
            computed += mismatch
    assert computed == cost == alignment_cost(x, y, gap, mismatch)


if __name__ == "__main__":
    _check("AT", "AAT", 1, 1)
    _check("kitten", "sitting", 1, 1)
    _check("abc", "abc", 5, 5)
    _check("", "abc", 2, 1)
    _check("AGGTAB", "GXTXAYB", 2, 3)
    _check("hello", "world", 1, 1)

    print("All tests passed!")
