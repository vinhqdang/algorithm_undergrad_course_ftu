"""
Week 15 - Randomized Algorithms
===============================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import make_rng, generate_array, generate_graph

Conventions
-----------
- Every source of randomness goes through ``random.Random(seed)`` (never the
  global ``random`` module) so that results are fully reproducible. The helper
  ``make_rng(seed)`` exists to make this explicit at every call site.
- An "array" is a plain Python ``list`` of numbers.
- A "graph" is an undirected multigraph represented as ``(vertices, edges)``
  where ``vertices`` is a list of vertex labels and ``edges`` is a list of
  ``(u, v)`` tuples (parallel edges are allowed, which Karger's contraction
  algorithm relies on).
- All statistical tests in the exercises seed their RNGs and assert on LOOSE
  bounds chosen so that a correct implementation never flakes.
"""

from __future__ import annotations

import random
from typing import Hashable, List, Tuple

Graph = Tuple[List[Hashable], List[Tuple[Hashable, Hashable]]]


def make_rng(seed: int | None = None) -> random.Random:
    """Return a fresh, independently-seeded pseudo-random generator.

    Always prefer this (or ``random.Random(seed)`` directly) over the global
    ``random`` functions, so that every randomized routine is reproducible.
    """
    return random.Random(seed)


def generate_array(n: int, seed: int | None = None, lo: int = 0, hi: int = 1000) -> List[int]:
    """Generate a list of `n` random integers in [lo, hi] (inclusive)."""
    rng = make_rng(seed)
    return [rng.randint(lo, hi) for _ in range(n)]


def generate_distinct_array(n: int, seed: int | None = None) -> List[int]:
    """Generate a random permutation of [0, 1, ..., n-1] (all distinct)."""
    rng = make_rng(seed)
    arr = list(range(n))
    rng.shuffle(arr)
    return arr


def generate_stream(n: int, seed: int | None = None) -> List[int]:
    """Generate a 'stream' of `n` distinct labels 0..n-1 in a random order."""
    return generate_distinct_array(n, seed=seed)


def generate_graph(n: int, seed: int | None = None, p: float = 0.5) -> Graph:
    """Generate a random connected undirected graph on `n` vertices.

    Each possible edge is included independently with probability `p`; then a
    random spanning path is added to guarantee connectivity. Returned as
    ``(vertices, edges)`` with vertices ``[0, 1, ..., n-1]``.
    """
    rng = make_rng(seed)
    vertices = list(range(n))
    edge_set = set()

    # Random spanning path over a random permutation guarantees connectivity.
    perm = vertices[:]
    rng.shuffle(perm)
    for a, b in zip(perm, perm[1:]):
        edge_set.add((min(a, b), max(a, b)))

    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < p:
                edge_set.add((u, v))

    edges = [tuple(e) for e in sorted(edge_set)]
    return vertices, edges


def cut_size(graph: Graph, side_a: set) -> int:
    """Count edges crossing the cut (side_a, V \\ side_a)."""
    _, edges = graph
    return sum(1 for u, v in edges if (u in side_a) != (v in side_a))


def is_prime_trial_division(n: int) -> bool:
    """Deterministic primality test by trial division (reference oracle)."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
