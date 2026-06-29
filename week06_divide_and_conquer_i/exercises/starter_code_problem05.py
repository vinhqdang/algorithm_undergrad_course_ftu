"""
Problem 05 - Empirically Confirm Mergesort's Recurrence
========================================================

Implement `count_merge_calls(arr)`: run mergesort instrumented to count
  - the number of recursive MERGESORT calls (including base cases),
  - the number of MERGE operations (non-base-case calls that actually merge),
  - the total number of element comparisons.
Return the tuple (num_mergesort_calls, num_merge_ops, total_comparisons).

For an array of length n >= 1, the number of MERGE operations should equal
n - 1 (a binary recursion tree with n leaves has exactly n - 1 internal
nodes), confirming the recurrence structure T(n) = 2 T(n/2) + Theta(n).

See practical_exercises.pdf, Problem 5.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List, Tuple

from starter_code import generate_array


def count_merge_calls(arr: List[int]) -> Tuple[int, int, int]:
    """Return (num_mergesort_calls, num_merge_ops, total_comparisons)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # n = 1: one mergesort call, no merges, no comparisons.
        calls, merges, comps = count_merge_calls([42])
        assert (calls, merges, comps) == (1, 0, 0)

        # For arrays of length n, merge ops == n - 1.
        for n in (2, 4, 7, 16, 50, 100):
            a = generate_array(n, seed=n)
            calls, merges, comps = count_merge_calls(a)
            assert merges == n - 1, (n, merges)
            assert comps >= 0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
