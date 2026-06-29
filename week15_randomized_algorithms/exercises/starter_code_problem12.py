"""
Problem 12 - Universal-Hashing Collision Count
===============================================

Implement `universal_hash_family(p, m, seed)` returning a hash function
h(x) = ((a*x + b) mod p) mod m with random a in [1, p-1], b in [0, p-1] (seeded).
Implement `count_collisions(keys, h)` counting colliding PAIRS, and
`average_collisions(n, m, num_trials, seed)` averaging the collision count over
seeded random hash functions on n distinct keys (0..n-1).

See practical_exercises.pdf, Problem 12.
"""

import random
from typing import Callable, List


def universal_hash_family(p: int, m: int, seed: int) -> Callable[[int], int]:
    """Return h(x) = ((a*x + b) mod p) mod m with random a in [1,p-1], b in [0,p-1]."""
    # TODO: implement this function.
    raise NotImplementedError


def count_collisions(keys: List[int], h: Callable[[int], int]) -> int:
    """Count the number of colliding (unordered) pairs of keys under h."""
    # TODO: implement this function.
    raise NotImplementedError


def average_collisions(n: int, m: int, num_trials: int, seed: int) -> float:
    """Average colliding-pair count over seeded random hash functions on n keys."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        p, m = 2_000_003, 50
        h = universal_hash_family(p, m, seed=0)
        for x in range(100):
            assert 0 <= h(x) < m

        constant = lambda x: 0
        assert count_collisions(list(range(5)), constant) == 10

        n, m = 200, 100
        expected = n * (n - 1) / 2 / m
        avg = average_collisions(n, m, num_trials=300, seed=777)
        assert 0.6 * expected <= avg <= 1.4 * expected, (avg, expected)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
