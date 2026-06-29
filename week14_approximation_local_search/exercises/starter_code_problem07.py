"""
Problem 07 - Center Selection (Greedy Farthest-Point k-Center)
==============================================================

Implement `greedy_k_center(points, k, seed)`: pick a first center (index 0),
then repeatedly add the point FARTHEST from the current center set until k
centers are chosen. Return (centers, radius) where centers is a list of point
INDICES and radius = max_p min_c d(p, c) is the covering radius.

Use `euclidean` from starter_code.py.

See practical_exercises.pdf, Problem 7.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import euclidean, generate_points  # noqa: E402

Point = Tuple[float, float]


def greedy_k_center(points: List[Point], k: int, seed: int = 0) -> Tuple[List[int], float]:
    """Greedy farthest-point k-center. Return (centers, radius)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        pts = [(0.0, 0.0), (1.0, 0.0), (100.0, 0.0), (101.0, 0.0)]
        centers, radius = greedy_k_center(pts, k=2, seed=0)
        assert len(centers) == 2
        assert radius <= 1.0 + 1e-9

        centers, radius = greedy_k_center(pts, k=1, seed=0)
        assert centers == [0]
        assert abs(radius - 101.0) < 1e-9

        centers, radius = greedy_k_center(pts, k=4, seed=0)
        assert set(centers) == {0, 1, 2, 3}
        assert abs(radius) < 1e-9

        rnd = generate_points(20, seed=3)
        centers, radius = greedy_k_center(rnd, k=4, seed=0)
        assert radius >= 0.0
        for p in range(len(rnd)):
            assert min(euclidean(rnd[p], rnd[c]) for c in centers) <= radius + 1e-9

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
