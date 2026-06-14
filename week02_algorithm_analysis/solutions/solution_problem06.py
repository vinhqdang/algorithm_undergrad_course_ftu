"""
Problem 06 - Recurrence T(n) = 2T(n/2) + O(n): Linearithmic Recursion (SOLUTION)
====================================================================================
"""

from typing import List


def divide_combine_ops(n: int) -> int:
    """Recursively compute T(n) = 2*T(n//2) + n for n > 1, T(n) = n for n <= 1."""
    if n <= 1:
        return n
    return 2 * divide_combine_ops(n // 2) + n


def verify_linearithmic_growth(powers_of_two: List[int]) -> bool:
    """Check divide_combine_ops(2**k) == 2**k * (k+1) for every k in powers_of_two."""
    return all(divide_combine_ops(2 ** k) == 2 ** k * (k + 1) for k in powers_of_two)


if __name__ == "__main__":
    assert divide_combine_ops(0) == 0
    assert divide_combine_ops(1) == 1
    assert divide_combine_ops(2) == 2 * 1 + 2
    assert divide_combine_ops(4) == 2 * 4 + 4

    assert verify_linearithmic_growth([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print("All tests passed!")
