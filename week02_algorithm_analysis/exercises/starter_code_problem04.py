"""
Problem 04 - Recurrence T(n) = T(n-1) + O(1): Linear Recursion
================================================================

Consider the recursive function `countdown_ops(n)` that simulates the
recurrence T(n) = T(n-1) + 1 (with T(0) = 1):

    def countdown_ops(n):
        if n <= 0:
            return 1
        return 1 + countdown_ops(n - 1)

The closed form is T(n) = n + 1 = Theta(n).

Implement `countdown_ops(n)` exactly as above (recursively -- do not just
return n+1 directly; the point is to call this on small n and see that the
*number of recursive calls* matches the closed form).

Then implement `verify_linear_recurrence(n_values)` that, for each n in
n_values, computes `countdown_ops(n)` and checks it equals `n + 1`. Return
True iff this holds for every n in n_values.

See practical_exercises.pdf, Problem 4.
"""

from typing import List


def countdown_ops(n: int) -> int:
    """Recursively compute T(n) where T(n) = T(n-1) + 1, T(0) = 1."""
    # TODO: implement this function (recursively).
    raise NotImplementedError


def verify_linear_recurrence(n_values: List[int]) -> bool:
    """Check that countdown_ops(n) == n + 1 for every n in n_values."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert countdown_ops(0) == 1
        assert countdown_ops(1) == 2
        assert countdown_ops(5) == 6
        assert countdown_ops(10) == 11

        assert verify_linear_recurrence([0, 1, 2, 5, 10, 50, 100])

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
