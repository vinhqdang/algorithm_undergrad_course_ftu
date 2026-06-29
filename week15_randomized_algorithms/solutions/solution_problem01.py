"""
Problem 01 - Fisher-Yates Shuffle (SOLUTION)
=============================================
"""

import random
from typing import List


def fisher_yates_shuffle(arr: List, seed: int) -> List:
    """Return a uniformly random permutation of `arr` (seeded, not in place)."""
    rng = random.Random(seed)
    a = list(arr)
    for i in range(len(a) - 1, 0, -1):
        j = rng.randint(0, i)
        a[i], a[j] = a[j], a[i]
    return a


if __name__ == "__main__":
    base = list(range(8))

    # The result is always a permutation of the input.
    for seed in range(50):
        out = fisher_yates_shuffle(base, seed)
        assert sorted(out) == base
        assert out is not base

    # Empirical uniformity: shuffle [0,1,2] many times and check each of the
    # 6 permutations appears with frequency near 1/6 (loose bound).
    from collections import Counter

    counts = Counter()
    trials = 60000
    for seed in range(trials):
        counts[tuple(fisher_yates_shuffle([0, 1, 2], seed))] += 1

    assert len(counts) == 6, "all 6 permutations should appear"
    expected = trials / 6
    for perm, c in counts.items():
        # Loose +/-20% band around the expected count; never flakes for a
        # correct shuffle at this sample size.
        assert 0.8 * expected <= c <= 1.2 * expected, (perm, c, expected)

    print("All tests passed!")
