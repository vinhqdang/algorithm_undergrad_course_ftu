"""
Problem 02 - Mergesort with a Comparison Counter (SOLUTION)
============================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List, Optional

from starter_code import Counter, generate_array, is_sorted


def _merge_counting(left: List[int], right: List[int], counter: Optional[Counter]) -> List[int]:
    merged: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if counter is not None:
            counter.tick()
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def mergesort(arr: List[int], counter: Optional[Counter] = None) -> List[int]:
    """Return a new sorted copy of `arr`; count comparisons in `counter`."""
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = mergesort(arr[:mid], counter)
    right = mergesort(arr[mid:], counter)
    return _merge_counting(left, right, counter)


if __name__ == "__main__":
    import math

    assert mergesort([3, 1, 2]) == [1, 2, 3]
    assert mergesort([]) == []
    assert mergesort([5]) == [5]
    assert mergesort([2, 2, 1, 1]) == [1, 1, 2, 2]

    for seed in range(20):
        a = generate_array(50, seed=seed)
        out = mergesort(a)
        assert out == sorted(a)
        assert is_sorted(out)
        assert a == generate_array(50, seed=seed)

    c = Counter()
    a = generate_array(64, seed=99)
    mergesort(a, c)
    assert c.count <= 64 * math.ceil(math.log2(64))

    print("All tests passed!")
