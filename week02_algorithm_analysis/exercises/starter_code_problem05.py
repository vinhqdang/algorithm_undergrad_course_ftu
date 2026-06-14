"""
Problem 05 - Recurrence T(n) = T(n/2) + O(1): Logarithmic Recursion
=====================================================================

Consider the recursive function `halving_ops(n)` that simulates the
recurrence T(n) = T(floor(n/2)) + 1 for n >= 1, with T(0) = 1:

    def halving_ops(n):
        if n <= 0:
            return 1
        return 1 + halving_ops(n // 2)

The closed form is T(n) = Theta(log n); precisely, T(n) = floor(log2(n)) + 2
for n >= 1 (T(0) = 1).

Implement `halving_ops(n)` recursively as above.

Then implement `verify_log_recurrence(n_values)` that, for each n in
n_values (n >= 1), computes `halving_ops(n)` and checks it equals
`floor(log2(n)) + 2`. Return True iff this holds for every n in n_values.

See practical_exercises.pdf, Problem 5.
"""

import math
from typing import List


def halving_ops(n: int) -> int:
    """Recursively compute T(n) where T(n) = T(n // 2) + 1, T(0) = 1."""
    # TODO: implement this function (recursively).
    raise NotImplementedError


def verify_log_recurrence(n_values: List[int]) -> bool:
    """Check halving_ops(n) == floor(log2(n)) + 2 for every n >= 1 in n_values."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert halving_ops(0) == 1
        assert halving_ops(1) == 2
        assert halving_ops(2) == 3
        assert halving_ops(8) == 5  # floor(log2(8)) + 2 = 3 + 2 = 5
        assert halving_ops(1024) == 12  # floor(log2(1024)) + 2 = 10 + 2 = 12

        assert verify_log_recurrence([1, 2, 3, 4, 7, 8, 16, 100, 1000, 1024])

        # Doubling n increases halving_ops(n) by (at most) 1 -- the hallmark
        # of logarithmic growth.
        for n in [1, 2, 4, 8, 16, 32, 64]:
            assert halving_ops(2 * n) - halving_ops(n) in (0, 1)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
