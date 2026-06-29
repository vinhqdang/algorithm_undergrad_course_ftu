"""
Problem 04 - Reservoir Sampling (SOLUTION)
===========================================
"""

import random
from typing import Iterable, List


def reservoir_sample(stream: Iterable, k: int, seed: int) -> List:
    """Return a uniform random k-subset of `stream` in one pass, O(k) space."""
    rng = random.Random(seed)
    reservoir: List = []
    for t, item in enumerate(stream, start=1):
        if t <= k:
            reservoir.append(item)
        else:
            # Accept the t-th item with probability k/t.
            j = rng.randrange(t)
            if j < k:
                reservoir[j] = item
    return reservoir


if __name__ == "__main__":
    n, k = 10, 3

    # Result is always a size-k subset of distinct stream elements.
    for seed in range(50):
        sample = reservoir_sample(range(n), k, seed)
        assert len(sample) == k
        assert len(set(sample)) == k
        assert all(0 <= x < n for x in sample)

    # If the stream is shorter than k, return all of it.
    assert sorted(reservoir_sample(range(2), 5, seed=0)) == [0, 1]

    # Empirical inclusion frequency ~ k/n over many seeded trials (loose bound).
    counts = [0] * n
    trials = 60000
    for seed in range(trials):
        for x in reservoir_sample(range(n), k, seed):
            counts[x] += 1

    expected = trials * k / n
    for x in range(n):
        # +/-10% band around k/n expectation; comfortable for this sample size.
        assert 0.9 * expected <= counts[x] <= 1.1 * expected, (x, counts[x], expected)

    print("All tests passed!")
