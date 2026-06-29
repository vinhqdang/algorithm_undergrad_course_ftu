"""
Problem 05 - Verify the LCS / Edit-Distance Relation (SOLUTION)
================================================================

Insert/delete-only edit distance satisfies  d(x, y) = |x| + |y| - 2 * LCS(x, y).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import random_string

from solution_problem04 import lcs


def indel_distance(x: str, y: str) -> int:
    """Minimum number of insertions + deletions to turn x into y (no substitutions).

    The recurrence only allows match (when x[i]==y[j]) or a gap (insert/delete);
    a mismatch column is forbidden.
    """
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def verify_lcs_relation(num_trials: int, length: int, seed: int) -> bool:
    """Check indel_distance(x, y) == |x| + |y| - 2*LCS(x, y) on random pairs."""
    for trial in range(num_trials):
        x = random_string(length, seed=seed + 2 * trial)
        y = random_string(length, seed=seed + 2 * trial + 1)
        l, _ = lcs(x, y)
        if indel_distance(x, y) != len(x) + len(y) - 2 * l:
            return False
    return True


if __name__ == "__main__":
    assert indel_distance("AT", "AAT") == 1
    assert indel_distance("abc", "abc") == 0
    assert indel_distance("sea", "eat") == 2  # delete 's', delete 'a', insert 't' -> wait check
    # "sea" -> "eat": LCS is "ea" (len 2); 3 + 3 - 4 = 2
    assert indel_distance("sea", "eat") == len("sea") + len("eat") - 2 * lcs("sea", "eat")[0]

    assert verify_lcs_relation(num_trials=50, length=8, seed=1) is True
    assert verify_lcs_relation(num_trials=30, length=12, seed=99) is True

    print("All tests passed!")
