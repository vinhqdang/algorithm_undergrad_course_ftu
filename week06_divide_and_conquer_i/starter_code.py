"""
Week 06 - Divide and Conquer I
==============================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_array, Counter, is_sorted

Conventions
-----------
- An "array" is a plain Python ``list`` of comparable elements (usually
  integers). Algorithms in this week never mutate their input unless the
  docstring explicitly says so; they return a new list instead.
- A ``Counter`` (defined below) is a tiny mutable box used to count
  "operations" -- comparisons, multiplications, or recursive calls -- so that
  the exercises can confirm empirically that an algorithm matches its
  recurrence (e.g. mergesort performs ~n log n comparisons).
- Random instances are generated with Python's ``random.Random(seed)`` so
  that results are reproducible across runs.
"""

from __future__ import annotations

import random
from typing import List


class Counter:
    """A tiny mutable counter used to instrument algorithms.

    Pass a single shared ``Counter`` into a recursive routine and call
    ``tick()`` whenever the operation of interest happens (a comparison, a
    multiplication, a recursive call, ...). Read the running total via
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


def generate_array(n: int, seed: int | None = None, lo: int = 0, hi: int = 1000) -> List[int]:
    """Generate `n` random integers, each uniform in [lo, hi]."""
    rng = random.Random(seed)
    return [rng.randint(lo, hi) for _ in range(n)]


def generate_sorted_array(n: int, seed: int | None = None, lo: int = 0, hi: int = 1000) -> List[int]:
    """Generate a sorted (non-decreasing) array of `n` random integers."""
    return sorted(generate_array(n, seed=seed, lo=lo, hi=hi))


def generate_reverse_array(n: int, seed: int | None = None, lo: int = 0, hi: int = 1000) -> List[int]:
    """Generate a reverse-sorted (non-increasing) array of `n` random integers."""
    return sorted(generate_array(n, seed=seed, lo=lo, hi=hi), reverse=True)


def is_sorted(arr: List[int]) -> bool:
    """Return True iff `arr` is in non-decreasing order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def count_inversions_brute(arr: List[int]) -> int:
    """Count inversions (pairs i < j with arr[i] > arr[j]) in O(n^2).

    This is the slow reference implementation used to check the fast
    O(n log n) divide-and-conquer version in the exercises.
    """
    n = len(arr)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv
