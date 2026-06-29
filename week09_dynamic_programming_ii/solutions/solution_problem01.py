"""
Problem 01 - Edit Distance (Levenshtein) (SOLUTION)
=====================================================
"""


def edit_distance(x: str, y: str) -> int:
    """Return the Levenshtein edit distance between x and y."""
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sub = 0 if x[i - 1] == y[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j - 1] + sub,
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
            )
    return dp[m][n]


if __name__ == "__main__":
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "") == 0
    assert edit_distance("abc", "") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "abc") == 0
    assert edit_distance("flaw", "lawn") == 2
    assert edit_distance("intention", "execution") == 5

    print("All tests passed!")
