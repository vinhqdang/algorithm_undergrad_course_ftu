"""
Problem 01 - Brute-Force Closest Pair of Points
===============================================

Implement `closest_pair_brute(points)` that returns the minimum Euclidean
distance between any two of the given 2-D points, together with the pair that
achieves it, by checking all O(n^2) pairs.

Return ``(min_distance, (p, q))``. Raise ``ValueError`` if fewer than two
points are given. Use ``euclidean`` from starter_code.py.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
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
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        d, (p, q) = closest_pair_brute([(0, 0), (3, 4), (1, 1)])
        assert math.isclose(d, math.sqrt(2)), d
        assert {p, q} == {(0, 0), (1, 1)}

        d, _ = closest_pair_brute([(0, 0), (5, 0)])
        assert math.isclose(d, 5.0)

        pts = generate_distinct_points(40, seed=7)
        d, (p, q) = closest_pair_brute(pts)
        assert math.isclose(d, euclidean(p, q))
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                assert euclidean(pts[i], pts[j]) >= d - 1e-9

        try:
            closest_pair_brute([(0, 0)])
            assert False, "expected ValueError"
        except ValueError:
            pass

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
