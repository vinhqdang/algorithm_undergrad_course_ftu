"""
Problem 10 - Finding Max and Min with a Comparison Counter
=============================================================

Implement `find_max_min(arr)` that returns `(max_val, min_val, comparisons)`
where `comparisons` is the total number of element-vs-element comparisons
performed.

  - Naive approach: scan once to find the max (n-1 comparisons), then scan
    again to find the min (n-1 comparisons), for a total of 2(n-1)
    comparisons.

  - Implement the naive approach exactly as described (two separate linear
    scans), and return the comparison count.

Then implement `find_max_min_paired(arr)` that uses the classic
"divide into pairs" trick: process elements two at a time. For each pair
(a, b), first compare a vs b (1 comparison) to determine which is the
candidate-max and which is the candidate-min of the pair, then compare the
candidate-max against the running maximum (1 comparison) and the
candidate-min against the running minimum (1 comparison) -- 3 comparisons per
pair of elements, instead of 4. Handle an odd-length array by initializing
the running max/min from the first element (0 extra comparisons) before
processing the rest in pairs.

For n elements, the naive approach uses 2(n-1) comparisons; the paired
approach uses roughly 3n/2 comparisons -- fewer for n > 2.

See practical_exercises.pdf, Problem 10.
"""

from typing import List, Tuple


def find_max_min(arr: List[int]) -> Tuple[int, int, int]:
    """Return (max_val, min_val, comparisons) using two separate linear scans."""
    # TODO: implement this function.
    raise NotImplementedError


def find_max_min_paired(arr: List[int]) -> Tuple[int, int, int]:
    """Return (max_val, min_val, comparisons) using the pairwise trick (~3n/2 comparisons)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        arr = [3, 7, 1, 9, 4, 2, 8, 5, 6]

        max_v, min_v, cmp1 = find_max_min(arr)
        assert (max_v, min_v) == (9, 1)
        assert cmp1 == 2 * (len(arr) - 1)  # 2*(9-1) = 16

        max_v2, min_v2, cmp2 = find_max_min_paired(arr)
        assert (max_v2, min_v2) == (9, 1)
        assert cmp2 < cmp1  # the paired approach should use fewer comparisons

        # Single element: no comparisons needed.
        max_v3, min_v3, cmp3 = find_max_min([42])
        assert (max_v3, min_v3) == (42, 42)
        assert cmp3 == 0

        max_v4, min_v4, cmp4 = find_max_min_paired([42])
        assert (max_v4, min_v4) == (42, 42)
        assert cmp4 == 0

        # Two elements.
        max_v5, min_v5, _ = find_max_min_paired([5, 2])
        assert (max_v5, min_v5) == (5, 2)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
