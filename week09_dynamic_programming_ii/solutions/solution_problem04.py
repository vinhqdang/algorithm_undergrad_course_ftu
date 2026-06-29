"""
Problem 04 - Longest Common Subsequence (Length + One LCS) (SOLUTION)
======================================================================
"""

from typing import Tuple


def lcs(x: str, y: str) -> Tuple[int, str]:
    """Return (length, subsequence) for a longest common subsequence of x and y."""
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Trace back to build one LCS string
    parts = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            parts.append(x[i - 1])
            i, j = i - 1, j - 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    subseq = "".join(reversed(parts))
    return dp[m][n], subseq


def _is_subsequence(s: str, t: str) -> bool:
    it = iter(t)
    return all(ch in it for ch in s)


if __name__ == "__main__":
    length, sub = lcs("AGGTAB", "GXTXAYB")
    assert length == 4
    assert len(sub) == 4
    assert _is_subsequence(sub, "AGGTAB") and _is_subsequence(sub, "GXTXAYB")

    length, sub = lcs("abc", "abc")
    assert length == 3 and sub == "abc"

    length, sub = lcs("abc", "def")
    assert length == 0 and sub == ""

    length, sub = lcs("", "abc")
    assert length == 0 and sub == ""

    length, sub = lcs("AGCAT", "GAC")
    assert length == 2
    assert _is_subsequence(sub, "AGCAT") and _is_subsequence(sub, "GAC")

    print("All tests passed!")
