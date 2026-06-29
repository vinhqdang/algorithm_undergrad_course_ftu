"""
Problem 07 - Center Selection (Greedy Farthest-Point k-Center) (SOLUTION)
=========================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import euclidean, generate_points  # noqa: E402

Point = Tuple[float, float]


def greedy_k_center(points: List[Point], k: int, seed: int = 0) -> Tuple[List[int], float]:
    """Greedy farthest-point selection for k-center.

    Returns (centers, radius) where centers is a list of point indices and
    radius = max_p min_c d(p, c) is the covering radius.
    """
    n = len(points)
    if k <= 0 or n == 0:
        return [], 0.0
    k = min(k, n)

    # Deterministic first center (index 0); `seed` kept for signature compatibility
    # and reproducibility if a caller wishes to pre-shuffle.
    centers = [0]
    # dist_to_centers[p] = distance from p to its nearest chosen center.
    dist_to_centers = [euclidean(points[p], points[0]) for p in range(n)]

    while len(centers) < k:
        # Choose the point farthest from the current center set.
        farthest = max(range(n), key=lambda p: dist_to_centers[p])
        centers.append(farthest)
        for p in range(n):
            d = euclidean(points[p], points[farthest])
            if d < dist_to_centers[p]:
                dist_to_centers[p] = d

    radius = max(dist_to_centers)
    return centers, radius


if __name__ == "__main__":
    # Two well-separated clusters; k=2 should pick one center per cluster (radius small).
    pts = [(0.0, 0.0), (1.0, 0.0), (100.0, 0.0), (101.0, 0.0)]
    centers, radius = greedy_k_center(pts, k=2, seed=0)
    assert len(centers) == 2
    assert radius <= 1.0 + 1e-9

    # k=1: radius is distance to the farthest point from center 0.
    centers, radius = greedy_k_center(pts, k=1, seed=0)
    assert centers == [0]
    assert abs(radius - 101.0) < 1e-9

    # k >= n: every point is its own center, radius 0.
    centers, radius = greedy_k_center(pts, k=4, seed=0)
    assert set(centers) == {0, 1, 2, 3}
    assert abs(radius) < 1e-9

    # On random points, the greedy radius is within 2x the optimum; here we just
    # sanity-check that the radius is a valid covering radius (non-negative, finite).
    rnd = generate_points(20, seed=3)
    centers, radius = greedy_k_center(rnd, k=4, seed=0)
    assert radius >= 0.0
    # Every point must be within `radius` of some center.
    for p in range(len(rnd)):
        assert min(euclidean(rnd[p], rnd[c]) for c in centers) <= radius + 1e-9

    print("All tests passed!")
