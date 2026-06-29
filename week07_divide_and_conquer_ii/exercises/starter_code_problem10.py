"""
Problem 10 - Count of Range Sums via Divide and Conquer
=======================================================

Given an integer array ``nums`` and bounds ``lower <= upper``, count the
number of contiguous subarrays whose sum lies in [lower, upper].

Implement `count_range_sum_dc(nums, lower, upper)` in O(n log n). Work on the
prefix-sum array S (length n+1): a subarray (i, j) has sum S[j] - S[i]. During
a merge sort of S, count for each left index i how many right indices j have
lower <= S[j] - S[i] <= upper (a sliding two-pointer window over the sorted
right half).

A brute-force baseline `count_range_sum_brute` is provided; your D&C result
must match it.

See practical_exercises.pdf, Problem 10.
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def count_range_sum_brute(nums: List[int], lower: int, upper: int) -> int:
    """Count subarrays whose sum lies in [lower, upper], in O(n^2)."""
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    count = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if lower <= prefix[j] - prefix[i] <= upper:
                count += 1
    return count


def count_range_sum_dc(nums: List[int], lower: int, upper: int) -> int:
    """Count subarrays with sum in [lower, upper] in O(n log n)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert count_range_sum_dc([-2, 5, -1], -2, 2) == 3
        assert count_range_sum_brute([-2, 5, -1], -2, 2) == 3
        assert count_range_sum_dc([], 0, 0) == 0

        rng = random.Random(424242)
        for _ in range(300):
            n = rng.randint(0, 40)
            nums = [rng.randint(-20, 20) for _ in range(n)]
            lower = rng.randint(-50, 0)
            upper = rng.randint(0, 50)
            assert count_range_sum_dc(nums, lower, upper) == count_range_sum_brute(nums, lower, upper)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
