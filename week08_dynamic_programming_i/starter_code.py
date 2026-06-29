"""
Week 08 - Dynamic Programming I
===============================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_weighted_intervals, generate_knapsack_instance

Conventions
-----------
- A "weighted interval" (or "weighted request") is a tuple
  ``(start, finish, weight)`` with ``start < finish`` and ``weight >= 0``,
  representing a job that occupies a single resource during the half-open time
  range ``[start, finish)`` and is worth ``weight`` if selected.
- A "knapsack instance" is a triple ``(weights, values, capacity)`` where
  ``weights[i]`` and ``values[i]`` are the weight and value of item ``i`` (both
  non-negative integers) and ``capacity`` is a non-negative integer knapsack
  capacity.
- Random instances are generated with Python's ``random.Random(seed)`` so that
  results are reproducible across runs.
"""

from __future__ import annotations

import random
from typing import List, Tuple

WeightedInterval = Tuple[float, float, float]  # (start, finish, weight)
KnapsackInstance = Tuple[List[int], List[int], int]  # (weights, values, capacity)


def generate_weighted_intervals(
    n: int,
    seed: int | None = None,
    max_start: float = 20.0,
    max_len: float = 6.0,
    max_weight: float = 10.0,
) -> List[WeightedInterval]:
    """Generate `n` random weighted intervals (start, finish, weight).

    Starts are uniform in [0, max_start); lengths are uniform in [0.5, max_len];
    weights are integers uniform in [1, max_weight].
    """
    rng = random.Random(seed)
    intervals = []
    for _ in range(n):
        s = rng.uniform(0, max_start)
        length = rng.uniform(0.5, max_len)
        weight = float(rng.randint(1, int(max_weight)))
        intervals.append((s, s + length, weight))
    return intervals


def generate_knapsack_instance(
    n: int,
    seed: int | None = None,
    max_weight: int = 10,
    max_value: int = 20,
    capacity: int | None = None,
) -> KnapsackInstance:
    """Generate a random 0/1-knapsack instance with `n` items.

    Item weights are integers uniform in [1, max_weight]; item values are
    integers uniform in [1, max_value]. If `capacity` is None, it defaults to
    roughly half the total item weight (so the instance is non-trivial).
    """
    rng = random.Random(seed)
    weights = [rng.randint(1, max_weight) for _ in range(n)]
    values = [rng.randint(1, max_value) for _ in range(n)]
    if capacity is None:
        capacity = max(1, sum(weights) // 2)
    return weights, values, capacity


def total_weight(intervals: List[WeightedInterval]) -> float:
    """Return the sum of weights over all weighted intervals."""
    return sum(w for _, _, w in intervals)


def intervals_compatible(a: WeightedInterval, b: WeightedInterval) -> bool:
    """Return True iff two weighted intervals do not overlap.

    Intervals (s1, f1, _) and (s2, f2, _) overlap iff s1 < f2 and s2 < f1.
    Intervals that merely touch at an endpoint (f1 == s2) do NOT overlap, since
    intervals are half-open [start, finish).
    """
    s1, f1, _ = a
    s2, f2, _ = b
    return not (s1 < f2 and s2 < f1)


def selection_is_feasible(selection: List[WeightedInterval]) -> bool:
    """Return True iff no two weighted intervals in `selection` overlap."""
    ordered = sorted(selection, key=lambda iv: (iv[0], iv[1]))
    for (_, f_prev, _), (s_next, _, _) in zip(ordered, ordered[1:]):
        if s_next < f_prev:
            return False
    return True
