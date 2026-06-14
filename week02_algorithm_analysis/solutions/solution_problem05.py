"""
Problem 05 - Recurrence T(n) = T(n/2) + O(1): Logarithmic Recursion (SOLUTION)
=================================================================================
"""

import math
from typing import List


def halving_ops(n: int) -> int:
    """Recursively compute T(n) where T(n) = T(n // 2) + 1, T(0) = 1."""
    if n <= 0:
        return 1
    return 1 + halving_ops(n // 2)


def verify_log_recurrence(n_values: List[int]) -> bool:
    """Check halving_ops(n) == floor(log2(n)) + 2 for every n >= 1 in n_values."""
    return all(halving_ops(n) == math.floor(math.log2(n)) + 2 for n in n_values if n >= 1)


if __name__ == "__main__":
    assert halving_ops(0) == 1
    assert halving_ops(1) == 2
    assert halving_ops(2) == 3
    assert halving_ops(8) == 5
    assert halving_ops(1024) == 12

    assert verify_log_recurrence([1, 2, 3, 4, 7, 8, 16, 100, 1000, 1024])

    for n in [1, 2, 4, 8, 16, 32, 64]:
        assert halving_ops(2 * n) - halving_ops(n) in (0, 1)

    print("All tests passed!")
