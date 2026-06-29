"""
Problem 11 - Longest Increasing Subsequence via O(n^2) DP (SOLUTION)
====================================================================
"""

import itertools
from typing import List


def longest_increasing_subsequence_length(nums: List[int]) -> int:
    """Return the length of the longest STRICTLY increasing subsequence of `nums`.

    O(n^2) DP: L[i] = length of the longest increasing subsequence ENDING at i.
        L[i] = 1 + max(L[j] for j < i with nums[j] < nums[i]), or 1 if none.
    Answer is max(L).
    """
    n = len(nums)
    if n == 0:
        return 0
    L = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1
    return max(L)


def _brute_lis_length(nums: List[int]) -> int:
    """Brute force: try all subsequences (small n only)."""
    best = 0
    n = len(nums)
    for r in range(n + 1):
        for combo in itertools.combinations(nums, r):
            if all(combo[k] < combo[k + 1] for k in range(len(combo) - 1)):
                best = max(best, len(combo))
    return best


if __name__ == "__main__":
    assert longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence_length([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence_length([7, 7, 7, 7]) == 1  # strictly increasing
    assert longest_increasing_subsequence_length([]) == 0
    assert longest_increasing_subsequence_length([5]) == 1
    assert longest_increasing_subsequence_length([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence_length([5, 4, 3, 2, 1]) == 1

    # Verified against brute force on small random inputs.
    import random
    rng = random.Random(5)
    for _ in range(300):
        nums = [rng.randint(0, 9) for _ in range(rng.randint(0, 10))]
        assert longest_increasing_subsequence_length(nums) == _brute_lis_length(nums)

    print("All tests passed!")
