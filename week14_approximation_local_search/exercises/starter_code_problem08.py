"""
Problem 08 - Metric TSP 2-Approximation via MST Preorder
=========================================================

Implement `mst_tsp_tour(points)`: build a minimum spanning tree of the complete
Euclidean graph (Prim's is fine), then return (tour, tour_length), where `tour`
is the preorder DFS order of the MST (point indices, start not repeated) and
`tour_length` is the closed-tour length. Also implement `mst_weight(points)`.
Then `verify_tsp_2approx(num_trials, n, seed)`: check tour_length <= 2 * w(MST).

Use `distance_matrix` / `euclidean` from starter_code.py.

See practical_exercises.pdf, Problem 8.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import distance_matrix, generate_points  # noqa: E402

Point = Tuple[float, float]


def mst_weight(points: List[Point]) -> float:
    """Return the weight of the Euclidean MST of `points`."""
    # TODO: implement this function.
    raise NotImplementedError


def mst_tsp_tour(points: List[Point]) -> Tuple[List[int], float]:
    """Return (tour, tour_length): MST preorder order and closed-tour length."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_tsp_2approx(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff tour_length <= 2 * w(MST) on every random point set."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        square = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)]
        tour, length = mst_tsp_tour(square)
        assert sorted(tour) == [0, 1, 2, 3]
        assert length <= 2 * mst_weight(square) + 1e-9

        line = [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0), (3.0, 0.0)]
        tour, length = mst_tsp_tour(line)
        assert sorted(tour) == [0, 1, 2, 3]
        assert length <= 2 * mst_weight(line) + 1e-9

        assert verify_tsp_2approx(num_trials=50, n=12, seed=1) is True
        assert verify_tsp_2approx(num_trials=30, n=20, seed=99) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
