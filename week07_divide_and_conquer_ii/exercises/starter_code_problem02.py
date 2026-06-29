"""
Problem 02 - Divide-and-Conquer Closest Pair O(n log n)
=======================================================

Implement `closest_pair_dc(points)`, the classic O(n log n) divide-and-conquer
closest-pair algorithm:

  1. Sort the points by x (px) and by y (py).
  2. Split px at the median x into left/right halves; split py accordingly.
  3. Recursively find the closest pairs in the left and right halves; let
     delta be the smaller of the two distances.
  4. Build the "strip" of points within delta of the dividing line, in
     y-order. Compare each strip point only with the next 7 in y-order.
  5. Return the overall minimum distance and the achieving pair.

Return ``(min_distance, (p, q))``; raise ``ValueError`` for fewer than two
points. Use ``euclidean`` from starter_code.py.

See practical_exercises.pdf, Problem 2.
"""

import math
import sys
import os
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import euclidean, generate_distinct_points, brute_force_closest  # noqa: E402

Point = Tuple[float, float]


def closest_pair_dc(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Return (min_distance, (p, q)) using the O(n log n) divide-and-conquer."""
    # TODO: implement this function (a recursive helper is recommended).
    raise NotImplementedError


if __name__ == "__main__":
    try:
        d, (p, q) = closest_pair_dc([(0, 0), (3, 4), (1, 1)])
        assert math.isclose(d, math.sqrt(2)), d

        d, _ = closest_pair_dc([(0, 0), (5, 0)])
        assert math.isclose(d, 5.0)

        for n in (2, 3, 4, 5, 10, 50, 200):
            pts = generate_distinct_points(n, seed=100 + n)
            d_fast, (a, b) = closest_pair_dc(pts)
            d_slow, _ = brute_force_closest(pts)
            assert math.isclose(d_fast, d_slow), (n, d_fast, d_slow)
            assert math.isclose(d_fast, euclidean(a, b))

        try:
            closest_pair_dc([(0, 0)])
            assert False
        except ValueError:
            pass

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
