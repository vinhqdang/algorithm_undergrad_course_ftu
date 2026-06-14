"""
Problem 21 - A Non-Canonical Coin System Where Greedy Fails (SOLUTION)
==========================================================================
"""

import os
import sys
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem20 import brute_force_min_coins, greedy_change


def find_greedy_failure(denominations: List[int], max_amount: int = 100) -> Optional[int]:
    """Return the smallest amount in [1, max_amount] where greedy is suboptimal, or None."""
    for amount in range(1, max_amount + 1):
        greedy_count = sum(greedy_change(amount, denominations).values())
        optimal_count = brute_force_min_coins(amount, denominations)
        if greedy_count > optimal_count:
            return amount
    return None


def non_canonical_system() -> List[int]:
    """Return a list of denominations (including 1) that is NOT canonical."""
    # Classic example: with coins {1, 3, 4}, greedy makes 6 as 4+1+1 (3
    # coins), but 3+3 (2 coins) is optimal.
    return [1, 3, 4]


if __name__ == "__main__":
    system = non_canonical_system()
    assert 1 in system

    failure_amount = find_greedy_failure(system, max_amount=100)
    assert failure_amount is not None

    greedy_count = sum(greedy_change(failure_amount, system).values())
    optimal_count = brute_force_min_coins(failure_amount, system)
    assert greedy_count > optimal_count

    CANONICAL = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    assert find_greedy_failure(CANONICAL, max_amount=100) is None

    assert find_greedy_failure([1, 3, 4], max_amount=100) == 6

    print(f"Non-canonical system {system} first fails at amount {failure_amount} "
          f"(greedy uses {greedy_count} coins, optimal uses {optimal_count}).")
    print("All tests passed!")
