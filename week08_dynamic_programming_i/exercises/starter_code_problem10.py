"""
Problem 10 - Rod Cutting: Maximum Revenue and the Cut List
==========================================================

Given a rod of length n and a price table where prices[i] is the price of a
piece of length i+1, cut the rod into integer-length pieces to maximize total
revenue (pieces may repeat -- this is unbounded).

DP over rod length:
    rev[0] = 0
    rev[L] = max over k in 1..L of ( prices[k-1] + rev[L-k] )

To recover the actual cuts, record, for each L, the first cut length k that
achieved rev[L]; then peel off pieces from L = n downward.

Implement `rod_cutting(prices)` returning `(best_revenue, cuts)` where `cuts`
is a list of piece lengths summing to n = len(prices) whose prices sum to
`best_revenue`.

See practical_exercises.pdf, Problem 10.
"""

from typing import List, Tuple


def rod_cutting(prices: List[int]) -> Tuple[int, List[int]]:
    """Return (best_revenue, cuts) for cutting a rod of length len(prices)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        prices = [1, 5, 8, 9, 10, 17, 17, 20]
        rev, cuts = rod_cutting(prices)
        assert rev == 22
        assert sum(cuts) == 8
        assert sum(prices[k - 1] for k in cuts) == rev

        rev, cuts = rod_cutting([2, 4, 6])
        assert rev == 6
        assert sum(cuts) == 3

        rev, cuts = rod_cutting([])
        assert rev == 0 and cuts == []

        rev, cuts = rod_cutting([3])
        assert rev == 3 and cuts == [1]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
