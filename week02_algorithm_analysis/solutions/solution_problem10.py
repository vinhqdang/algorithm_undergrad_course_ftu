"""
Problem 10 - Finding Max and Min with a Comparison Counter (SOLUTION)
========================================================================
"""

from typing import List, Tuple


def find_max_min(arr: List[int]) -> Tuple[int, int, int]:
    """Return (max_val, min_val, comparisons) using two separate linear scans."""
    comparisons = 0

    max_val = arr[0]
    for x in arr[1:]:
        comparisons += 1
        if x > max_val:
            max_val = x

    min_val = arr[0]
    for x in arr[1:]:
        comparisons += 1
        if x < min_val:
            min_val = x

    return max_val, min_val, comparisons


def find_max_min_paired(arr: List[int]) -> Tuple[int, int, int]:
    """Return (max_val, min_val, comparisons) using the pairwise trick (~3n/2 comparisons)."""
    comparisons = 0
    n = len(arr)

    if n == 1:
        return arr[0], arr[0], 0

    i = 0
    if n % 2 == 1:
        max_val = min_val = arr[0]
        i = 1
    else:
        comparisons += 1
        if arr[0] >= arr[1]:
            max_val, min_val = arr[0], arr[1]
        else:
            max_val, min_val = arr[1], arr[0]
        i = 2

    while i + 1 < n:
        a, b = arr[i], arr[i + 1]
        comparisons += 1
        if a >= b:
            cand_max, cand_min = a, b
        else:
            cand_max, cand_min = b, a

        comparisons += 1
        if cand_max > max_val:
            max_val = cand_max

        comparisons += 1
        if cand_min < min_val:
            min_val = cand_min

        i += 2

    return max_val, min_val, comparisons


if __name__ == "__main__":
    arr = [3, 7, 1, 9, 4, 2, 8, 5, 6]

    max_v, min_v, cmp1 = find_max_min(arr)
    assert (max_v, min_v) == (9, 1)
    assert cmp1 == 2 * (len(arr) - 1)

    max_v2, min_v2, cmp2 = find_max_min_paired(arr)
    assert (max_v2, min_v2) == (9, 1)
    assert cmp2 < cmp1

    max_v3, min_v3, cmp3 = find_max_min([42])
    assert (max_v3, min_v3) == (42, 42)
    assert cmp3 == 0

    max_v4, min_v4, cmp4 = find_max_min_paired([42])
    assert (max_v4, min_v4) == (42, 42)
    assert cmp4 == 0

    max_v5, min_v5, _ = find_max_min_paired([5, 2])
    assert (max_v5, min_v5) == (5, 2)

    print("All tests passed!")
