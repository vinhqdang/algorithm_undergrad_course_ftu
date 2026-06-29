"""
Problem 01 - Brute-Force Closest Pair of Points (SOLUTION)
==========================================================
"""

import math
import sys
import os
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import euclidean, generate_distinct_points  # noqa: E402

Point = Tuple[float, float]


def closest_pair_brute(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Return (min_distance, (p, q)) over all pairs, in O(n^2)."""
    n = len(points)
    if n < 2:
        raise ValueError("need at least two points")
    best = math.inf
    best_pair = (points[0], points[1])
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean(points[i], points[j])
            if d < best:
                best = d
                best_pair = (points[i], points[j])
    return best, best_pair


if __name__ == "__main__":
    d, (p, q) = closest_pair_brute([(0, 0), (3, 4), (1, 1)])
    assert math.isclose(d, math.sqrt(2)), d
    assert {p, q} == {(0, 0), (1, 1)}

    # Two points: trivial.
    d, _ = closest_pair_brute([(0, 0), (5, 0)])
    assert math.isclose(d, 5.0)

    # The returned pair really achieves the returned distance.
    pts = generate_distinct_points(40, seed=7)
    d, (p, q) = closest_pair_brute(pts)
    assert math.isclose(d, euclidean(p, q))
    # And no pair is closer.
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            assert euclidean(pts[i], pts[j]) >= d - 1e-9

    try:
        closest_pair_brute([(0, 0)])
        assert False, "expected ValueError"
    except ValueError:
        pass

    print("All tests passed!")
