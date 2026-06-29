"""
Problem 05 - Verify the LCS / Edit-Distance Relation
=====================================================

The insert/delete-only edit distance (no substitutions) satisfies

    d(x, y) = |x| + |y| - 2 * LCS(x, y).

Implement `indel_distance(x, y)` computing the minimum number of insertions and
deletions to turn `x` into `y` via DP (substitution forbidden: only matches and
gaps are allowed). Then implement `verify_lcs_relation(num_trials, length, seed)`
that, for `num_trials` random string pairs (via `random_string`), checks
`indel_distance(x, y) == len(x) + len(y) - 2 * lcs_length(x, y)` for every pair,
returning True iff the identity always holds.

A reference `lcs_length` helper is provided below so this problem is independent
of Problem 4.

See practical_exercises.pdf, Problem 5, for the full statement and examples.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import random_string


def lcs_length(x: str, y: str) -> int:
    """Length of a longest common subsequence of x and y (reference helper)."""
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def indel_distance(x: str, y: str) -> int:
    """Minimum number of insertions + deletions to turn x into y (no substitutions)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_lcs_relation(num_trials: int, length: int, seed: int) -> bool:
    """Check indel_distance(x, y) == |x| + |y| - 2*LCS(x, y) on random pairs."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert indel_distance("AT", "AAT") == 1
        assert indel_distance("abc", "abc") == 0
        assert indel_distance("sea", "eat") == len("sea") + len("eat") - 2 * lcs_length("sea", "eat")

        assert verify_lcs_relation(num_trials=50, length=8, seed=1) is True
        assert verify_lcs_relation(num_trials=30, length=12, seed=99) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
