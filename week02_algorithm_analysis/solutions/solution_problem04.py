"""
Problem 04 - Recurrence T(n) = T(n-1) + O(1): Linear Recursion (SOLUTION)
============================================================================
"""

from typing import List


def countdown_ops(n: int) -> int:
    """Recursively compute T(n) where T(n) = T(n-1) + 1, T(0) = 1."""
    if n <= 0:
        return 1
    return 1 + countdown_ops(n - 1)


def verify_linear_recurrence(n_values: List[int]) -> bool:
    """Check that countdown_ops(n) == n + 1 for every n in n_values."""
    return all(countdown_ops(n) == n + 1 for n in n_values)


if __name__ == "__main__":
    assert countdown_ops(0) == 1
    assert countdown_ops(1) == 2
    assert countdown_ops(5) == 6
    assert countdown_ops(10) == 11

    assert verify_linear_recurrence([0, 1, 2, 5, 10, 50, 100])

    print("All tests passed!")
