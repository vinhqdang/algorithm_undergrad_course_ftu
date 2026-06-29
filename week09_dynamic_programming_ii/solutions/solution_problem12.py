"""
Problem 12 - Grid Unique Paths and Minimum Path Sum (SOLUTION)
================================================================
"""

from typing import List, Tuple


def unique_paths(r: int, c: int) -> int:
    """Number of right/down paths from top-left to bottom-right of an r x c grid."""
    dp = [[1] * c for _ in range(r)]
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[r - 1][c - 1]


def min_path_sum(grid: List[List[int]]) -> Tuple[int, List[Tuple[int, int]]]:
    """Return (cost, path) for a minimum-cost right/down path through the grid."""
    r, c = len(grid), len(grid[0])
    dp = [[0] * c for _ in range(r)]
    dp[0][0] = grid[0][0]
    for j in range(1, c):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, r):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    # Trace back from (r-1, c-1) to (0, 0)
    path = []
    i, j = r - 1, c - 1
    while (i, j) != (0, 0):
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif dp[i - 1][j] <= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    path.append((0, 0))
    path.reverse()
    return dp[r - 1][c - 1], path


if __name__ == "__main__":
    assert unique_paths(3, 3) == 6
    assert unique_paths(1, 1) == 1
    assert unique_paths(3, 7) == 28
    assert unique_paths(1, 10) == 1

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    cost, path = min_path_sum(grid)
    assert cost == 7, cost
    assert path[0] == (0, 0) and path[-1] == (2, 2)
    # Path is a valid right/down walk and its costs sum to `cost`
    total = grid[0][0]
    for (pi, pj), (qi, qj) in zip(path, path[1:]):
        assert (qi - pi, qj - pj) in ((1, 0), (0, 1))
        total += grid[qi][qj]
    assert total == cost

    assert min_path_sum([[5]]) == (5, [(0, 0)])

    print("All tests passed!")
