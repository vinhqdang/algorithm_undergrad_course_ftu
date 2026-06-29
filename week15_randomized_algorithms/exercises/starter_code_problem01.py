"""
Problem 01 - Fisher-Yates Shuffle
==================================

Implement `fisher_yates_shuffle(arr, seed)` returning a uniformly random
permutation of `arr` using the in-place Fisher-Yates (Knuth) shuffle: for i from
n-1 down to 1, pick j uniformly in [0, i] and swap positions i and j. Route ALL
randomness through random.Random(seed) (never the global random module).

See practical_exercises.pdf, Problem 1, for the full statement.
"""

import random
from typing import List


def fisher_yates_shuffle(arr: List, seed: int) -> List:
    """Return a uniformly random permutation of `arr` (seeded, not in place)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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
            assert 0.8 * expected <= c <= 1.2 * expected, (perm, c, expected)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
