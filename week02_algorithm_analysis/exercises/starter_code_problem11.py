"""
Problem 11 - Median via Sorting vs. Quickselect
=================================================

Implement `median_via_sort(arr)` that returns the median of `arr` (the
middle element of the sorted array for odd length; for even length, return
the lower of the two middle elements, i.e. index n//2 - 1 of 0-indexed sorted
array... to keep this simple, define median as `sorted(arr)[(len(arr)-1)//2]`
for both even and odd lengths) by calling Python's built-in `sorted()`.

Then implement `quickselect(arr, k)`, which returns the k-th smallest element
(0-indexed) of `arr` using the Quickselect algorithm:

  1. If `len(arr) == 1`, return `arr[0]`.
  2. Choose a pivot (use `arr[0]` for determinism).
  3. Partition `arr` into three lists: elements `< pivot`, `== pivot`, and
     `> pivot`.
  4. If `k < len(less)`, recurse into `less` with the same `k`.
     Elif `k < len(less) + len(equal)`, return `pivot`.
     Else recurse into `greater` with `k - len(less) - len(equal)`.

Then implement `median_via_quickselect(arr)` that calls
`quickselect(arr, (len(arr)-1)//2)`.

Finally, implement `count_comparisons_sort(arr)` returning the number of
comparisons `sorted()` would roughly need in the worst case for an array of
length n, i.e. `ceil(n * log2(n))` if n > 1 else 0 (a standard upper-bound
estimate for comparison sorts) -- this is for *discussion*, not measured
directly.

See practical_exercises.pdf, Problem 11.
"""

import math
from typing import List


def median_via_sort(arr: List[int]) -> int:
    """Return sorted(arr)[(len(arr)-1)//2]."""
    # TODO: implement this function.
    raise NotImplementedError


def quickselect(arr: List[int], k: int) -> int:
    """Return the k-th smallest element (0-indexed) of arr via Quickselect."""
    # TODO: implement this function (recursively).
    raise NotImplementedError


def median_via_quickselect(arr: List[int]) -> int:
    """Return the median of arr using quickselect."""
    # TODO: implement this function.
    raise NotImplementedError


def count_comparisons_sort(n: int) -> int:
    """Return ceil(n * log2(n)) for n > 1, else 0 -- a rough comparison-sort estimate."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        arr = [9, 3, 7, 1, 8, 2, 5]  # sorted: [1,2,3,5,7,8,9], median index 3 -> 5
        assert median_via_sort(arr) == 5
        assert median_via_quickselect(arr) == 5

        arr2 = [4, 2, 1, 3]  # sorted: [1,2,3,4], (len-1)//2 = 1 -> 2
        assert median_via_sort(arr2) == 2
        assert median_via_quickselect(arr2) == 2

        for k in range(len(arr)):
            assert quickselect(arr, k) == sorted(arr)[k]

        assert quickselect([42], 0) == 42

        assert count_comparisons_sort(1) == 0
        assert count_comparisons_sort(8) == math.ceil(8 * math.log2(8))

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
