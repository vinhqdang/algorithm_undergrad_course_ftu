"""
Problem 05 - Empirically Confirm Mergesort's Recurrence (SOLUTION)
==================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List, Tuple

from starter_code import generate_array


def count_merge_calls(arr: List[int]) -> Tuple[int, int, int]:
    """Return (num_mergesort_calls, num_merge_ops, total_comparisons)."""
    stats = {"calls": 0, "merges": 0, "comps": 0}

    def _sort(a: List[int]) -> List[int]:
        stats["calls"] += 1
        if len(a) <= 1:
            return list(a)
        mid = len(a) // 2
        left = _sort(a[:mid])
        right = _sort(a[mid:])
        stats["merges"] += 1
        merged: List[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            stats["comps"] += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    _sort(arr)
    return stats["calls"], stats["merges"], stats["comps"]


if __name__ == "__main__":
    calls, merges, comps = count_merge_calls([42])
    assert (calls, merges, comps) == (1, 0, 0)

    for n in (2, 4, 7, 16, 50, 100):
        a = generate_array(n, seed=n)
        calls, merges, comps = count_merge_calls(a)
        assert merges == n - 1, (n, merges)
        assert comps >= 0

    print("All tests passed!")
