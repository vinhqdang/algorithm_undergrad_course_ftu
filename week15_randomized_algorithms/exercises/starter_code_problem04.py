"""
Problem 04 - Reservoir Sampling
================================

Implement `reservoir_sample(stream, k, seed)` returning a uniform random k-subset
of `stream` (an iterable of unknown length) in a SINGLE pass using O(k) space:
keep the first k items, and for the t-th item (t > k) accept it with probability
k/t, replacing a uniformly random reservoir slot.

See practical_exercises.pdf, Problem 4.
"""

import random
from typing import Iterable, List


def reservoir_sample(stream: Iterable, k: int, seed: int) -> List:
    """Return a uniform random k-subset of `stream` in one pass, O(k) space."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        n, k = 10, 3

        for seed in range(50):
            sample = reservoir_sample(range(n), k, seed)
            assert len(sample) == k
            assert len(set(sample)) == k
            assert all(0 <= x < n for x in sample)

        assert sorted(reservoir_sample(range(2), 5, seed=0)) == [0, 1]

        counts = [0] * n
        trials = 60000
        for seed in range(trials):
            for x in reservoir_sample(range(n), k, seed):
                counts[x] += 1

        expected = trials * k / n
        for x in range(n):
            assert 0.9 * expected <= counts[x] <= 1.1 * expected, (x, counts[x], expected)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
