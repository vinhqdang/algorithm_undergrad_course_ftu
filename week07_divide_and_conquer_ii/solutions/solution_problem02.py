"""
Problem 02 - Divide-and-Conquer Closest Pair O(n log n) (SOLUTION)
==================================================================
"""

import math
import sys
import os
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import euclidean, generate_distinct_points, brute_force_closest  # noqa: E402

Point = Tuple[float, float]


def _closest_rec(px: List[Point], py: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Recurse on points sorted by x (px) and the same points sorted by y (py)."""
    n = len(px)
    if n <= 3:
        # Base case: brute force on this tiny set.
        best = math.inf
        best_pair = (px[0], px[1])
        for i in range(n):
            for j in range(i + 1, n):
                d = euclidean(px[i], px[j])
                if d < best:
                    best = d
                    best_pair = (px[i], px[j])
        return best, best_pair

    mid = n // 2
    midpoint = px[mid]
    lx = px[:mid]
    rx = px[mid:]

    # Split py into left/right preserving y-order. Ties on x are broken by
    # comparing the full point so that left and right partition exactly.
    left_set = set(lx)
    ly = [p for p in py if p in left_set]
    ry = [p for p in py if p not in left_set]

    dl, pair_l = _closest_rec(lx, ly)
    dr, pair_r = _closest_rec(rx, ry)
    if dl <= dr:
        delta, best_pair = dl, pair_l
    else:
        delta, best_pair = dr, pair_r

    # Build the strip: points within delta of the dividing line, in y-order.
    strip = [p for p in py if abs(p[0] - midpoint[0]) < delta]

    # Each point need only be compared with the next 7 points in y-order.
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            d = euclidean(strip[i], strip[j])
            if d < delta:
                delta = d
                best_pair = (strip[i], strip[j])
    return delta, best_pair


def closest_pair_dc(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Return (min_distance, (p, q)) using the O(n log n) divide-and-conquer."""
    if len(points) < 2:
        raise ValueError("need at least two points")
    px = sorted(points, key=lambda p: (p[0], p[1]))
    py = sorted(points, key=lambda p: (p[1], p[0]))
    return _closest_rec(px, py)


if __name__ == "__main__":
    d, (p, q) = closest_pair_dc([(0, 0), (3, 4), (1, 1)])
    assert math.isclose(d, math.sqrt(2)), d

    d, _ = closest_pair_dc([(0, 0), (5, 0)])
    assert math.isclose(d, 5.0)

    # Agreement with the brute-force baseline across sizes.
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
