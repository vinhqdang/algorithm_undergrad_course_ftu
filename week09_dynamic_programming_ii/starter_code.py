"""
Week 09 - Dynamic Programming II
================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import random_string, generate_weighted_graph

Conventions
-----------
- A "string" for the sequence-alignment problems is an ordinary Python ``str``
  built from a small alphabet (default ``"ACGT"``, the DNA bases, which keeps
  examples short and readable).
- A weighted directed graph is represented as ``(n, edges)`` where ``n`` is the
  number of vertices (labelled ``0 .. n-1``) and ``edges`` is a list of
  ``(u, v, w)`` triples meaning a directed edge ``u -> v`` of weight ``w``.
  Weights may be negative (this is the whole point of Bellman-Ford and
  Floyd-Warshall). We use the sentinel ``INF = float("inf")`` for "no path".
- Random instances are generated with Python's ``random.Random(seed)`` so that
  results are reproducible across runs.
"""

from __future__ import annotations

import random
from typing import Dict, List, Optional, Tuple

INF = float("inf")

Edge = Tuple[int, int, float]  # (u, v, weight)


def random_string(length: int, seed: int | None = None, alphabet: str = "ACGT") -> str:
    """Return a random string of the given ``length`` drawn from ``alphabet``.

    Uses ``random.Random(seed)`` so the result is reproducible for a fixed seed.
    """
    rng = random.Random(seed)
    return "".join(rng.choice(alphabet) for _ in range(length))


def generate_weighted_graph(
    n: int,
    m: int,
    seed: int | None = None,
    min_weight: float = -5.0,
    max_weight: float = 10.0,
    allow_negative: bool = True,
) -> Tuple[int, List[Edge]]:
    """Generate a random directed weighted graph ``(n, edges)`` with ``m`` edges.

    Vertices are labelled ``0 .. n-1``. Each edge ``(u, v, w)`` has ``u != v``;
    weights are integers in ``[min_weight, max_weight]``. If ``allow_negative``
    is False, the lower bound is clamped to 0 (useful when you need a graph that
    is guaranteed free of negative edges).

    Note: this generator does NOT guarantee the absence of negative cycles -- on
    the contrary, allowing negative weights makes them possible, which is exactly
    what negative-cycle detection (Problem 7) must cope with.
    """
    rng = random.Random(seed)
    lo = int(min_weight) if allow_negative else max(0, int(min_weight))
    hi = int(max_weight)
    edges: List[Edge] = []
    for _ in range(m):
        u = rng.randrange(n)
        v = rng.randrange(n)
        while v == u:
            v = rng.randrange(n)
        w = float(rng.randint(lo, hi))
        edges.append((u, v, w))
    return n, edges


def generate_dag(
    n: int,
    m: int,
    seed: int | None = None,
    min_weight: float = -5.0,
    max_weight: float = 10.0,
) -> Tuple[int, List[Edge]]:
    """Generate a random *acyclic* directed weighted graph ``(n, edges)``.

    Acyclicity is guaranteed by only ever creating edges ``u -> v`` with
    ``u < v`` (a topological order is then simply ``0, 1, ..., n-1``). Weights
    may be negative; there can be no negative cycles because there are no cycles
    at all.
    """
    rng = random.Random(seed)
    lo, hi = int(min_weight), int(max_weight)
    possible = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(possible)
    chosen = possible[: min(m, len(possible))]
    edges: List[Edge] = [(u, v, float(rng.randint(lo, hi))) for (u, v) in chosen]
    return n, edges


def adjacency_list(n: int, edges: List[Edge]) -> List[List[Tuple[int, float]]]:
    """Convert ``(n, edges)`` into an adjacency list ``adj[u] = [(v, w), ...]``."""
    adj: List[List[Tuple[int, float]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    return adj


def adjacency_matrix(n: int, edges: List[Edge]) -> List[List[float]]:
    """Convert ``(n, edges)`` into a distance matrix.

    ``mat[i][i] = 0`` and ``mat[i][j] = INF`` when there is no direct edge.
    Parallel edges collapse to the minimum weight.
    """
    mat = [[INF] * n for _ in range(n)]
    for i in range(n):
        mat[i][i] = 0.0
    for u, v, w in edges:
        if w < mat[u][v]:
            mat[u][v] = w
    return mat


def reconstruct_path(parent: List[Optional[int]], source: int, target: int) -> Optional[List[int]]:
    """Follow ``parent`` pointers back from ``target`` to ``source``.

    Returns the path ``[source, ..., target]`` as a list of vertices, or
    ``None`` if ``target`` is unreachable (``parent[target] is None`` and
    ``target != source``).
    """
    if target == source:
        return [source]
    if parent[target] is None:
        return None
    path = [target]
    cur: Optional[int] = target
    while cur is not None and cur != source:
        cur = parent[cur]
        if cur is None:
            return None
        path.append(cur)
    path.reverse()
    return path


def grid_from_seed(rows: int, cols: int, seed: int | None = None, max_cost: int = 9) -> List[List[int]]:
    """Return a ``rows x cols`` grid of non-negative integer costs (reproducible)."""
    rng = random.Random(seed)
    return [[rng.randint(0, max_cost) for _ in range(cols)] for _ in range(rows)]
