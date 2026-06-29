"""
Problem 09 - TSP via Held-Karp Bitmask DP
=========================================

Implement:
  - tsp_held_karp(dist): shortest tour visiting every city once and returning
    to city 0, via the Held-Karp DP over subsets:
        dp[S][j] = shortest path from 0, visiting exactly S, ending at j.
        answer   = min over j != 0 of dp[FULL][j] + dist[j][0].
    O(n^2 * 2^n).
  - tsp_brute_force(dist): try all (n-1)! permutations of the non-start cities.
  - verify_tsp(num_trials, n, seed): True iff Held-Karp and brute force agree
    (within 1e-9) on num_trials random symmetric matrices.

See practical_exercises.pdf, Problem 9.
"""

import itertools
import random
from typing import List

Matrix = List[List[float]]


def tsp_held_karp(dist: Matrix) -> float:
    """Shortest tour via Held-Karp DP. O(n^2 * 2^n)."""
    # TODO: implement this function.
    raise NotImplementedError


def tsp_brute_force(dist: Matrix) -> float:
    """Shortest tour by trying all (n-1)! permutations of the non-start cities."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_tsp(num_trials: int, n: int, seed: int) -> bool:
    """True iff Held-Karp and brute force agree on `num_trials` random matrices."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        square = [
            [0, 1, 2, 1],
            [1, 0, 1, 2],
            [2, 1, 0, 1],
            [1, 2, 1, 0],
        ]
        assert abs(tsp_held_karp(square) - 4.0) < 1e-9
        assert abs(tsp_brute_force(square) - 4.0) < 1e-9

        assert tsp_held_karp([[0]]) == 0.0
        assert tsp_held_karp([[0, 5], [5, 0]]) == 10.0

        assert verify_tsp(num_trials=20, n=5, seed=1)
        assert verify_tsp(num_trials=10, n=7, seed=99)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
