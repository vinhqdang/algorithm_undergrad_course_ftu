"""
Problem 03 - Randomized Quickselect (SOLUTION)
===============================================
"""

import os
import random
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def randomized_quickselect(arr: List, k: int, seed: int):
    """Return the k-th smallest element (1-indexed) using random pivots."""
    if not 1 <= k <= len(arr):
        raise ValueError("k out of range")
    rng = random.Random(seed)
    return _select(list(arr), k, rng)


def _select(a: List, k: int, rng: random.Random):
    if len(a) == 1:
        return a[0]
    pivot = a[rng.randrange(len(a))]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    if k <= len(less):
        return _select(less, k, rng)
    if k <= len(less) + len(equal):
        return pivot
    return _select(greater, k - len(less) - len(equal), rng)


if __name__ == "__main__":
    from starter_code import generate_array

    # Against sorted()[k-1] for every k over many seeded instances.
    for trial in range(60):
        arr = generate_array(35, seed=2000 + trial)
        srt = sorted(arr)
        for k in range(1, len(arr) + 1):
            assert randomized_quickselect(arr, k, seed=trial) == srt[k - 1], (trial, k)

    # Distinct-element arrays too.
    for trial in range(40):
        from starter_code import generate_distinct_array

        arr = generate_distinct_array(30, seed=3000 + trial)
        srt = sorted(arr)
        for k in (1, 5, 15, 30):
            assert randomized_quickselect(arr, k, seed=trial) == srt[k - 1]

    # Edge cases.
    assert randomized_quickselect([42], 1, seed=0) == 42

    print("All tests passed!")
