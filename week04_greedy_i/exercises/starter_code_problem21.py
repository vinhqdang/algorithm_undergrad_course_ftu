"""
Problem 21 - A Non-Canonical Coin System Where Greedy Fails
==============================================================

A coin system is "canonical" if greedy change-making (Problem 20) is always
optimal. Not all coin systems are canonical!

Implement `find_greedy_failure(denominations, max_amount)` that searches
amounts `1, 2, ..., max_amount` and returns the SMALLEST amount for which
`greedy_change` (Problem 20) uses STRICTLY MORE coins than
`brute_force_min_coins` (Problem 20), or `None` if no such amount exists in
the range.

Then implement `non_canonical_system()` returning a list of denominations
(including 1) for which `find_greedy_failure` finds a failure with
`max_amount=100`.

Hint: the classic example is `[1, 3, 4]`: for amount 6, greedy picks
4 + 1 + 1 (3 coins), but the optimal is 3 + 3 (2 coins).

See practical_exercises.pdf, Problem 21.
"""

import os
import sys
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem20 import brute_force_min_coins, greedy_change


def find_greedy_failure(denominations: List[int], max_amount: int = 100) -> Optional[int]:
    """Return the smallest amount in [1, max_amount] where greedy is suboptimal, or None."""
    # TODO: implement this function.
    raise NotImplementedError


def non_canonical_system() -> List[int]:
    """Return a list of denominations (including 1) that is NOT canonical."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        system = non_canonical_system()
        assert 1 in system

        failure_amount = find_greedy_failure(system, max_amount=100)
        assert failure_amount is not None

        greedy_count = sum(greedy_change(failure_amount, system).values())
        optimal_count = brute_force_min_coins(failure_amount, system)
        assert greedy_count > optimal_count

        # The canonical system from Problem 20 has no failures up to 100.
        CANONICAL = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        assert find_greedy_failure(CANONICAL, max_amount=100) is None

        # The classic [1,3,4] example fails at amount 6.
        assert find_greedy_failure([1, 3, 4], max_amount=100) == 6

        print(f"Non-canonical system {system} first fails at amount {failure_amount} "
              f"(greedy uses {greedy_count} coins, optimal uses {optimal_count}).")
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
