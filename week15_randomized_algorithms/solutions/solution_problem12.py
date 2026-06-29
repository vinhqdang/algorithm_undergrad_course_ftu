"""
Problem 12 - Universal-Hashing Collision Count (SOLUTION)
=========================================================
"""

import random
from typing import Callable, List


def universal_hash_family(p: int, m: int, seed: int) -> Callable[[int], int]:
    """Return h(x) = ((a*x + b) mod p) mod m with random a in [1,p-1], b in [0,p-1]."""
    rng = random.Random(seed)
    a = rng.randrange(1, p)
    b = rng.randrange(0, p)

    def h(x: int) -> int:
        return ((a * x + b) % p) % m

    return h


def count_collisions(keys: List[int], h: Callable[[int], int]) -> int:
    """Count the number of colliding (unordered) pairs of keys under h."""
    from collections import Counter

    buckets = Counter(h(k) for k in keys)
    return sum(c * (c - 1) // 2 for c in buckets.values())


def average_collisions(n: int, m: int, num_trials: int, seed: int) -> float:
    """Average colliding-pair count over seeded random hash functions on n keys."""
    # A large prime exceeding the key universe.
    p = 2_000_003
    keys = list(range(n))
    total = 0
    for trial in range(num_trials):
        h = universal_hash_family(p, m, seed=seed + trial)
        total += count_collisions(keys, h)
    return total / num_trials


if __name__ == "__main__":
    # A single hash function is a valid mapping into [0, m).
    p, m = 2_000_003, 50
    h = universal_hash_family(p, m, seed=0)
    for x in range(100):
        assert 0 <= h(x) < m

    # count_collisions sanity: all keys to one bucket -> C(n,2) pairs.
    constant = lambda x: 0
    assert count_collisions(list(range(5)), constant) == 10  # C(5,2)

    # Average colliding pairs ~ C(n,2)/m ~ n^2/(2m) over trials (loose bound).
    n, m = 200, 100
    expected = n * (n - 1) / 2 / m  # = C(n,2)/m
    avg = average_collisions(n, m, num_trials=300, seed=777)
    # Generous +/-40% band; comfortable for a universal family at this size.
    assert 0.6 * expected <= avg <= 1.4 * expected, (avg, expected)

    print("All tests passed!")
