"""
Problem 09 - Las Vegas vs. Monte Carlo (SOLUTION)
==================================================

Task: find an index of `target` in `arr` (which is guaranteed to contain it).

- Las Vegas: probe random indices until the target is found. ALWAYS correct;
  the running time (number of probes) is random.
- Monte Carlo: probe at most `max_probes` random indices; return an index if
  found, else None. Fixed time bound; may FAIL (return None) but is never wrong
  when it does return an index.
"""

import random
from typing import List, Optional


def las_vegas_find(arr: List, target, seed: int) -> int:
    """Always-correct random search; returns an index i with arr[i] == target."""
    rng = random.Random(seed)
    n = len(arr)
    while True:
        i = rng.randrange(n)
        if arr[i] == target:
            return i


def monte_carlo_find(arr: List, target, max_probes: int, seed: int) -> Optional[int]:
    """Bounded random search; returns an index or None (never a wrong index)."""
    rng = random.Random(seed)
    n = len(arr)
    for _ in range(max_probes):
        i = rng.randrange(n)
        if arr[i] == target:
            return i
    return None


if __name__ == "__main__":
    arr = list(range(100))
    target = 42

    # Las Vegas is ALWAYS correct over many seeds.
    for seed in range(500):
        i = las_vegas_find(arr, target, seed)
        assert arr[i] == target

    # Monte Carlo: never wrong when it returns an index; may return None.
    saw_success = False
    saw_failure = False
    for seed in range(500):
        i = monte_carlo_find(arr, target, max_probes=3, seed=seed)
        if i is None:
            saw_failure = True
        else:
            assert arr[i] == target  # never wrong
            saw_success = True
    # With only 3 probes into 100 slots we should see both outcomes.
    assert saw_success and saw_failure

    # A generous probe budget makes Monte Carlo essentially always succeed here.
    successes = sum(
        1 for seed in range(200)
        if monte_carlo_find(arr, target, max_probes=2000, seed=seed) is not None
    )
    assert successes == 200

    print("All tests passed!")
