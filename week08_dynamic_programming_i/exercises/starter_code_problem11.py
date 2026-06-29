"""
Problem 11 - Longest Increasing Subsequence via O(n^2) DP
=========================================================

A subsequence keeps the original order but may drop elements. The Longest
Increasing Subsequence (LIS) is the longest STRICTLY increasing one.

O(n^2) DP: let L[i] be the length of the longest increasing subsequence that
ENDS at index i:

    L[i] = 1 + max( L[j] : j < i and nums[j] < nums[i] )    (or 1 if no such j)

The answer is max(L) (or 0 for an empty list).

Implement `longest_increasing_subsequence_length(nums)`. The final test checks
your DP against a brute-force search over all subsequences on small inputs.

See practical_exercises.pdf, Problem 11.
"""

import itertools
from typing import List


def longest_increasing_subsequence_length(nums: List[int]) -> int:
    """Return the length of the longest strictly increasing subsequence."""
    # TODO: implement this function.
    raise NotImplementedError


def _brute_lis_length(nums: List[int]) -> int:
    """Brute force reference (provided): try all subsequences (small n only)."""
    best = 0
    n = len(nums)
    for r in range(n + 1):
        for combo in itertools.combinations(nums, r):
            if all(combo[k] < combo[k + 1] for k in range(len(combo) - 1)):
                best = max(best, len(combo))
    return best


if __name__ == "__main__":
    try:
        assert longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert longest_increasing_subsequence_length([0, 1, 0, 3, 2, 3]) == 4
        assert longest_increasing_subsequence_length([7, 7, 7, 7]) == 1
        assert longest_increasing_subsequence_length([]) == 0
        assert longest_increasing_subsequence_length([5]) == 1
        assert longest_increasing_subsequence_length([1, 2, 3, 4, 5]) == 5
        assert longest_increasing_subsequence_length([5, 4, 3, 2, 1]) == 1

        import random
        rng = random.Random(5)
        for _ in range(300):
            nums = [rng.randint(0, 9) for _ in range(rng.randint(0, 10))]
            assert longest_increasing_subsequence_length(nums) == _brute_lis_length(nums)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
