"""
Problem 05 - Subset Sum: Decide if a Target Sum Is Achievable
=============================================================

The Subset Sum problem: given non-negative integers `nums` and a `target`,
is there a subset of `nums` summing to exactly `target`?

Boolean DP. Let reachable[t] be True iff some subset sums to t. Initially only
t = 0 is reachable (the empty subset). For each number x, a sum t becomes newly
reachable if t - x was already reachable. To keep each item used AT MOST ONCE
(this is 0/1 subset sum, not unbounded), iterate t from high to low when
applying x, so x is not re-used within the same update.

Implement `subset_sum_achievable(nums, target)` returning a bool. Return False
for negative targets. This is pseudo-polynomial: O(n * target) time.

See practical_exercises.pdf, Problem 5.
"""

from typing import List


def subset_sum_achievable(nums: List[int], target: int) -> bool:
    """Return True iff some subset of `nums` sums to `target`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert subset_sum_achievable([3, 34, 4, 12, 5, 2], 9) is True
        assert subset_sum_achievable([3, 34, 4, 12, 5, 2], 30) is False
        assert subset_sum_achievable([1, 2, 3], 0) is True
        assert subset_sum_achievable([], 0) is True
        assert subset_sum_achievable([], 5) is False
        assert subset_sum_achievable([5], 5) is True
        assert subset_sum_achievable([5], 4) is False
        assert subset_sum_achievable([2, 2, 2], 6) is True
        assert subset_sum_achievable([2, 2, 2], 5) is False
        assert subset_sum_achievable([1, 2, 3], -1) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
