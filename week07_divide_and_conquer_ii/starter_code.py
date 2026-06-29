"""
Week 07 - Divide and Conquer II
===============================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_points, euclidean, poly_eval, Counter

Conventions
-----------
- A "point" is a tuple ``(x, y)`` of two floats in the plane.
- A "polynomial" is a Python ``list`` of coefficients in increasing order of
  degree: ``[a0, a1, a2, ...]`` represents ``a0 + a1*x + a2*x^2 + ...``.
- A ``Counter`` (defined below) is a tiny mutable box used to count
  "operations" -- multiplications, recursive calls, distance evaluations --
  so the exercises can confirm empirically that an algorithm matches its
  recurrence (e.g. Karatsuba performs 3 recursive multiplications per level).
- Random instances are generated with Python's ``random.Random(seed)`` so
  that results are reproducible across runs.
"""

from __future__ import annotations

import math
import random
from typing import List, Tuple

Point = Tuple[float, float]


class Counter:
    """A tiny mutable counter used to instrument algorithms.

    Pass a single shared ``Counter`` into a recursive routine and call
    ``tick()`` whenever the operation of interest happens (a multiplication, a
    recursive call, a distance evaluation, ...). Read the running total via
    ``count`` or ``int(counter)``.

    Example
    -------
    >>> c = Counter()
    >>> c.tick()
    >>> c.tick(3)
    >>> c.count
    4
    """

    def __init__(self) -> None:
        self.count = 0

    def tick(self, amount: int = 1) -> None:
        """Add ``amount`` (default 1) to the running total."""
        self.count += amount

    def reset(self) -> None:
        """Reset the running total to zero."""
        self.count = 0

    def __int__(self) -> int:
        return self.count

    def __repr__(self) -> str:
        return f"Counter(count={self.count})"


def generate_points(n: int, seed: int | None = None, lo: float = 0.0, hi: float = 1000.0) -> List[Point]:
    """Generate `n` random 2-D points, each coordinate uniform in [lo, hi].

    Uses ``random.Random(seed)`` for reproducibility. Coordinates are floats.
    """
    rng = random.Random(seed)
    return [(rng.uniform(lo, hi), rng.uniform(lo, hi)) for _ in range(n)]


def generate_distinct_points(n: int, seed: int | None = None, grid: int = 100000) -> List[Point]:
    """Generate `n` random points with distinct integer coordinates on a grid.

    Guarantees no two points coincide (useful when a test wants a unique
    closest pair). Each point is ``(x, y)`` with integer coordinates in
    ``[0, grid)``, returned as floats.
    """
    rng = random.Random(seed)
    seen: set[Point] = set()
    pts: List[Point] = []
    while len(pts) < n:
        p = (float(rng.randrange(grid)), float(rng.randrange(grid)))
        if p not in seen:
            seen.add(p)
            pts.append(p)
    return pts


def euclidean(p: Point, q: Point) -> float:
    """Return the Euclidean distance between two points ``p`` and ``q``."""
    return math.hypot(p[0] - q[0], p[1] - q[1])


def brute_force_closest(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Reference O(n^2) closest-pair: return (min_distance, (p, q)).

    The slow but obviously-correct baseline used to check the fast
    O(n log n) divide-and-conquer version in the exercises. Raises
    ``ValueError`` for fewer than two points.
    """
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


def poly_eval(coeffs: List[float], x: float) -> float:
    """Evaluate the polynomial ``coeffs`` (low-to-high degree) at ``x``.

    Uses Horner's rule. ``coeffs = [a0, a1, a2]`` evaluates to
    ``a0 + a1*x + a2*x^2``.
    """
    result = 0.0
    for c in reversed(coeffs):
        result = result * x + c
    return result


def poly_mul_naive(a: List[float], b: List[float]) -> List[float]:
    """Reference O(n*m) polynomial multiplication (coefficient convolution).

    Returns the coefficient list (low-to-high) of the product polynomial.
    Used as the correctness baseline for the FFT-based multiplication.
    """
    if not a or not b:
        return []
    result = [0.0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


def next_power_of_two(n: int) -> int:
    """Return the smallest power of two that is >= n (and >= 1)."""
    p = 1
    while p < n:
        p <<= 1
    return p
