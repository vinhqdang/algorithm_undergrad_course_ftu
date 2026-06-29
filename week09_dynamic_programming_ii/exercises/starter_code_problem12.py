"""
Problem 12 - Grid Unique Paths and Minimum Path Sum
====================================================

For an r-by-c grid with movement restricted to right and down:
  * Implement `unique_paths(r, c)` returning the number of distinct paths from the
    top-left to the bottom-right corner (P(i,j) = P(i-1,j) + P(i,j-1)).
  * Implement `min_path_sum(grid)` returning (cost, path) where `grid` is a list of
    lists of cell costs, `cost` is the minimum total cost of a top-left-to-
    bottom-right path, and `path` is one optimal path as a list of (row, col)
    coordinates (reconstructed by traceback).

See practical_exercises.pdf, Problem 12, for the full statement and examples.
"""

from typing import List, Tuple


def unique_paths(r: int, c: int) -> int:
    """Number of right/down paths from top-left to bottom-right of an r x c grid."""
    # TODO: implement this function.
    raise NotImplementedError


def min_path_sum(grid: List[List[int]]) -> Tuple[int, List[Tuple[int, int]]]:
    """Return (cost, path) for a minimum-cost right/down path through the grid."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert unique_paths(3, 3) == 6
        assert unique_paths(1, 1) == 1
        assert unique_paths(3, 7) == 28
        assert unique_paths(1, 10) == 1

        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        cost, path = min_path_sum(grid)
        assert cost == 7, cost
        assert path[0] == (0, 0) and path[-1] == (2, 2)
        total = grid[0][0]
        for (pi, pj), (qi, qj) in zip(path, path[1:]):
            assert (qi - pi, qj - pj) in ((1, 0), (0, 1))
            total += grid[qi][qj]
        assert total == cost

        assert min_path_sum([[5]]) == (5, [(0, 0)])

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
