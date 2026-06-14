"""
Problem 06 - Recurrence T(n) = 2T(n/2) + O(n): Linearithmic Recursion
=======================================================================

Consider the recursive function `divide_combine_ops(n)` that simulates the
recurrence T(n) = 2*T(n/2) + n for n > 1, with T(1) = 1 (and T(0) = 0):

    def divide_combine_ops(n):
        if n <= 1:
            return n
        return 2 * divide_combine_ops(n // 2) + n

This is the same recurrence that governs mergesort's running time, and its
solution is T(n) = Theta(n log n).

Implement `divide_combine_ops(n)` recursively as above. (For n that is not a
power of 2, `n // 2` truncates -- that's fine, just follow the recurrence
literally.)

Then implement `verify_linearithmic_growth(powers_of_two)` where
`powers_of_two` is a list of exponents k (so n = 2**k). For each k, compute
T(n) = divide_combine_ops(2**k). When n is an exact power of two, the closed
form is T(n) = n * (k + 1) = n * log2(n) + n. Check that
`divide_combine_ops(2**k) == 2**k * (k + 1)` for every k in `powers_of_two`.
Return True iff this holds for all of them.

See practical_exercises.pdf, Problem 6.
"""

from typing import List


def divide_combine_ops(n: int) -> int:
    """Recursively compute T(n) = 2*T(n//2) + n for n > 1, T(n) = n for n <= 1."""
    # TODO: implement this function (recursively).
    raise NotImplementedError


def verify_linearithmic_growth(powers_of_two: List[int]) -> bool:
    """Check divide_combine_ops(2**k) == 2**k * (k+1) for every k in powers_of_two."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert divide_combine_ops(0) == 0
        assert divide_combine_ops(1) == 1
        assert divide_combine_ops(2) == 2 * 1 + 2  # 2*T(1) + 2 = 2*1 + 2 = 4
        assert divide_combine_ops(4) == 2 * 4 + 4  # 2*T(2) + 4 = 2*4 + 4 = 12

        assert verify_linearithmic_growth([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
