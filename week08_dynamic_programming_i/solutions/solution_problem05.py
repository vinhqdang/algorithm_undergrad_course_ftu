"""
Problem 05 - Subset Sum: Decide if a Target Sum Is Achievable (SOLUTION)
========================================================================
"""

from typing import List


def subset_sum_achievable(nums: List[int], target: int) -> bool:
    """Return True iff some subset of `nums` (non-negative ints) sums to `target`.

    Boolean DP: reachable[t] is True iff some subset sums to t. Start with only
    t = 0 reachable, then for each number x update reachable in DESCENDING order
    of t so each item is used at most once (0/1).
    """
    if target < 0:
        return False
    reachable = [False] * (target + 1)
    reachable[0] = True
    for x in nums:
        if x <= 0:
            if x == 0:
                continue  # a zero element never changes reachability
            raise ValueError("subset_sum_achievable expects non-negative integers")
        for t in range(target, x - 1, -1):
            if reachable[t - x]:
                reachable[t] = True
    return reachable[target]


if __name__ == "__main__":
    assert subset_sum_achievable([3, 34, 4, 12, 5, 2], 9) is True   # 4 + 5
    assert subset_sum_achievable([3, 34, 4, 12, 5, 2], 30) is False
    assert subset_sum_achievable([1, 2, 3], 0) is True              # empty subset
    assert subset_sum_achievable([], 0) is True
    assert subset_sum_achievable([], 5) is False
    assert subset_sum_achievable([5], 5) is True
    assert subset_sum_achievable([5], 4) is False
    assert subset_sum_achievable([2, 2, 2], 6) is True
    assert subset_sum_achievable([2, 2, 2], 5) is False
    assert subset_sum_achievable([1, 2, 3], -1) is False

    # Cross-check against brute force on small random instances.
    import itertools
    import random
    rng = random.Random(0)
    for _ in range(200):
        nums = [rng.randint(1, 9) for _ in range(rng.randint(0, 8))]
        target = rng.randint(0, 20)
        brute = any(
            sum(c) == target
            for r in range(len(nums) + 1)
            for c in itertools.combinations(nums, r)
        )
        assert subset_sum_achievable(nums, target) == brute

    print("All tests passed!")
