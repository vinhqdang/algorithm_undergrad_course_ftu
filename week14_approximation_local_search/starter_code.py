"""
Week 14 - Approximation Algorithms and Local Search
===================================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_graph, generate_points, generate_jobs

Conventions
-----------
- A "graph" is represented as ``(n, edges)`` where ``n`` is the number of
  vertices (labelled ``0 .. n-1``) and ``edges`` is a list of unordered pairs
  ``(u, v)`` with ``u < v`` and no duplicates or self-loops.
- A "point" is a tuple ``(x, y)`` of floats in the plane; distances are
  Euclidean (a metric, so the triangle inequality holds -- relevant for the
  metric TSP and k-center exercises).
- A "job" for the load-balancing problems is a non-negative processing time
  (a float); an instance is a list of such times.
- A weighted complete graph (for metric TSP) is given by a distance matrix
  ``dist`` with ``dist[i][j]`` the distance between points i and j.
- Random instances are generated with Python's ``random.Random(seed)`` so that
  results are reproducible across runs.

Throughout, an *approximation ratio* of ``rho`` for a minimization problem
means ``ALG <= rho * OPT`` on every instance; for a maximization problem it
means ``ALG >= OPT / rho`` (equivalently ``ALG >= (1/rho) * OPT``).
"""

from __future__ import annotations

import math
import random
from typing import Dict, List, Tuple

Graph = Tuple[int, List[Tuple[int, int]]]
Point = Tuple[float, float]


def generate_graph(n: int, p: float = 0.3, seed: int | None = None) -> Graph:
    """Generate a random undirected graph on `n` vertices (Erdos-Renyi G(n, p)).

    Each unordered pair (u, v) with u < v is included as an edge independently
    with probability `p`. Returns ``(n, edges)`` with edges sorted and each
    stored as ``(u, v)`` with u < v.
    """
    rng = random.Random(seed)
    edges: List[Tuple[int, int]] = []
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < p:
                edges.append((u, v))
    return (n, edges)


def generate_points(n: int, seed: int | None = None, span: float = 100.0) -> List[Point]:
    """Generate `n` random points uniformly in the square [0, span) x [0, span)."""
    rng = random.Random(seed)
    return [(rng.uniform(0, span), rng.uniform(0, span)) for _ in range(n)]


def generate_jobs(n: int, seed: int | None = None, max_len: float = 10.0) -> List[float]:
    """Generate `n` random job processing times, each uniform in (0, max_len]."""
    rng = random.Random(seed)
    return [rng.uniform(0.5, max_len) for _ in range(n)]


def euclidean(a: Point, b: Point) -> float:
    """Euclidean distance between two points in the plane."""
    return math.hypot(a[0] - b[0], a[1] - b[1])


def distance_matrix(points: List[Point]) -> List[List[float]]:
    """Return the full Euclidean distance matrix for a list of points.

    The result is a metric (symmetric, zero diagonal, triangle inequality),
    which is what the metric-TSP and k-center approximation guarantees require.
    """
    n = len(points)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean(points[i], points[j])
            dist[i][j] = d
            dist[j][i] = d
    return dist


def neighbors(graph: Graph) -> Dict[int, List[int]]:
    """Return an adjacency-list representation ``{vertex: [neighbours]}``."""
    n, edges = graph
    adj: Dict[int, List[int]] = {v: [] for v in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def is_vertex_cover(graph: Graph, cover: set) -> bool:
    """Return True iff `cover` (a set of vertices) covers every edge of `graph`,
    i.e. every edge has at least one endpoint in `cover`."""
    _, edges = graph
    return all(u in cover or v in cover for (u, v) in edges)


def cut_value(graph: Graph, side: List[int]) -> int:
    """Return the number of edges crossing the cut defined by `side`.

    `side[v]` is 0 or 1, assigning vertex v to one of the two sides. An edge
    crosses the cut iff its endpoints are on different sides.
    """
    _, edges = graph
    return sum(1 for (u, v) in edges if side[u] != side[v])
