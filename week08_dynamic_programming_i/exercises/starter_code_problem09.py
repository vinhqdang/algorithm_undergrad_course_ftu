"""
Problem 09 - Coin Change: Number of Distinct Ways
=================================================

Given coin denominations `coins` (unlimited supply) and a target `amount`,
count the number of DISTINCT COMBINATIONS of coins summing to `amount` (order
does not matter: 1+2 and 2+1 are the SAME way).

Counting DP. The subtle point: to count combinations (not permutations), loop
over coins on the OUTSIDE and amounts on the inside:

    ways[0] = 1
    for c in coins:
        for a in c..amount:
            ways[a] += ways[a - c]

If you swapped the loop order, you would count ordered sequences instead.

Implement `coin_change_ways(coins, amount)`. (There is exactly one way to make
amount 0: choose nothing.)

See practical_exercises.pdf, Problem 9.
"""

from typing import List


def coin_change_ways(coins: List[int], amount: int) -> int:
    """Return the number of distinct coin combinations summing to `amount`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert coin_change_ways([1, 2, 5], 5) == 4
        assert coin_change_ways([2], 3) == 0
        assert coin_change_ways([], 0) == 1
        assert coin_change_ways([1, 2, 3], 4) == 4
        assert coin_change_ways([7], 14) == 1
        assert coin_change_ways([1], 0) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
