"""
Problem 02 - Randomized QuickSort (SOLUTION)
=============================================
"""

import math
import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def randomized_quicksort(arr: List, seed: int) -> List:
    """Return a sorted copy of `arr` using randomized (seeded) pivots."""
    rng = random.Random(seed)
    return _qsort(list(arr), rng)


def _qsort(a: List, rng: random.Random) -> List:
    if len(a) <= 1:
        return a
    pivot = a[rng.randrange(len(a))]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return _qsort(less, rng) + equal + _qsort(greater, rng)


def quicksort_with_comparisons(arr: List, seed: int) -> Tuple[List, int]:
    """Return (sorted_copy, number_of_element_comparisons)."""
    rng = random.Random(seed)
    counter = [0]
    result = _qsort_count(list(arr), rng, counter)
    return result, counter[0]


def _qsort_count(a: List, rng: random.Random, counter: List[int]) -> List:
    if len(a) <= 1:
        return a
    pivot = a[rng.randrange(len(a))]
    less, equal, greater = [], [], []
    for x in a:
        counter[0] += 1  # each element compared once against the pivot
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return _qsort_count(less, rng, counter) + equal + _qsort_count(greater, rng, counter)


if __name__ == "__main__":
    from starter_code import generate_array

    # Correctness over many seeded instances.
    for trial in range(100):
        arr = generate_array(40, seed=1000 + trial)
        assert randomized_quicksort(arr, seed=trial) == sorted(arr)

    # Edge cases.
    assert randomized_quicksort([], seed=0) == []
    assert randomized_quicksort([5], seed=0) == [5]
    assert randomized_quicksort([3, 1, 2, 1], seed=0) == [1, 1, 2, 3]

    # Comparison count is O(n log n): average over trials stays well under a
    # generous constant factor of n log2 n (loose bound, never flakes).
    n = 200
    total = 0
    num_trials = 40
    for trial in range(num_trials):
        arr = generate_array(n, seed=5000 + trial)
        _, comps = quicksort_with_comparisons(arr, seed=trial)
        assert _ == sorted(arr)
        total += comps
    avg = total / num_trials
    bound = 10 * n * math.log2(n)
    assert avg <= bound, (avg, bound)

    print("All tests passed!")
