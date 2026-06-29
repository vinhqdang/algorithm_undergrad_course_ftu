"""
Problem 10 - Count of Range Sums via Divide and Conquer (SOLUTION)
==================================================================
"""

import random
import sys
import os
from typing import List

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def count_range_sum_brute(nums: List[int], lower: int, upper: int) -> int:
    """Count contiguous subarrays whose sum lies in [lower, upper], in O(n^2)."""
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
    """Count subarrays with sum in [lower, upper] in O(n log n).

    Works on the prefix-sum array S (length n+1): a subarray (i, j) has sum
    S[j] - S[i] in [lower, upper]. We merge-sort S and, during the merge,
    count for each left index i how many right indices j satisfy
    lower <= S[j] - S[i] <= upper.
    """
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    def sort_count(lo: int, hi: int) -> int:
        # Sorts prefix[lo:hi] in place and returns the count of valid pairs
        # (i, j) with lo <= i < j < hi straddling the midpoint.
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        count = sort_count(lo, mid) + sort_count(mid, hi)

        # Count pairs with i in [lo, mid), j in [mid, hi).
        j_low = j_high = mid
        for i in range(lo, mid):
            while j_low < hi and prefix[j_low] - prefix[i] < lower:
                j_low += 1
            while j_high < hi and prefix[j_high] - prefix[i] <= upper:
                j_high += 1
            count += j_high - j_low

        # Merge the two sorted halves.
        prefix[lo:hi] = sorted(prefix[lo:hi])
        return count

    return sort_count(0, n + 1)


if __name__ == "__main__":
    # Classic LeetCode example: [-2,5,-1], lower=-2, upper=2 -> 3.
    assert count_range_sum_dc([-2, 5, -1], -2, 2) == 3
    assert count_range_sum_brute([-2, 5, -1], -2, 2) == 3
    assert count_range_sum_dc([], 0, 0) == 0

    rng = random.Random(424242)
    for _ in range(300):
        n = rng.randint(0, 40)
        nums = [rng.randint(-20, 20) for _ in range(n)]
        lower = rng.randint(-50, 0)
        upper = rng.randint(0, 50)
        assert count_range_sum_dc(nums, lower, upper) == count_range_sum_brute(nums, lower, upper), (nums, lower, upper)

    print("All tests passed!")
