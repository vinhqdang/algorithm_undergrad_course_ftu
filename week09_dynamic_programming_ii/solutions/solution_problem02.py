"""
Problem 02 - Sequence Alignment with Custom Gap and Mismatch Costs (SOLUTION)
==============================================================================
"""


def alignment_cost(x: str, y: str, gap: float, mismatch: float) -> float:
    """Return the minimum-cost alignment of x and y under given gap/mismatch costs."""
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
    return dp[m][n]


if __name__ == "__main__":
    # gap == mismatch == 1 reduces to Levenshtein
    assert alignment_cost("kitten", "sitting", gap=1, mismatch=1) == 3
    assert alignment_cost("AT", "AAT", gap=2, mismatch=3) == 2
    assert alignment_cost("abc", "abc", gap=5, mismatch=5) == 0
    assert alignment_cost("", "abc", gap=2, mismatch=1) == 6
    # When mismatch is very expensive, prefer gaps: "a" vs "b" -> 2 gaps not 1 mismatch
    assert alignment_cost("a", "b", gap=1, mismatch=5) == 2
    assert alignment_cost("a", "b", gap=5, mismatch=1) == 1

    print("All tests passed!")
