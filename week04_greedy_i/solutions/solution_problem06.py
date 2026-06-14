"""
Problem 06 - Counter-Example: Shortest-Interval-First Is Not Optimal (SOLUTION)
==================================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem04 import brute_force_max_independent_set
from starter_code import is_feasible

Interval = Tuple[float, float]


def shortest_interval_first(intervals: List[Interval]) -> List[Interval]:
    """Greedily select the shortest remaining compatible interval, repeatedly."""
    selected: List[Interval] = []
    for s, f in sorted(intervals, key=lambda iv: iv[1] - iv[0]):
        if is_feasible(selected + [(s, f)]):
            selected.append((s, f))
    return selected


def counter_example_instance() -> List[Interval]:
    """Return an instance where shortest_interval_first is strictly suboptimal."""
    # A short interval (4,6) overlaps two longer, mutually-compatible intervals
    # (0,5) and (5,10). Shortest-first picks (4,6) alone (size 1), while the
    # optimum picks {(0,5), (5,10)} (size 2).
    return [(0, 5), (4, 6), (5, 10)]


if __name__ == "__main__":
    instance = counter_example_instance()
    greedy_result = shortest_interval_first(instance)
    optimal = brute_force_max_independent_set(instance)

    assert is_feasible(greedy_result)
    assert is_feasible(optimal)
    assert len(greedy_result) < len(optimal), (
        f"shortest-interval-first selected {len(greedy_result)} intervals, "
        f"but the optimum is {len(optimal)}"
    )

    print(f"shortest-interval-first selects {len(greedy_result)} interval(s); "
          f"optimal selects {len(optimal)}.")
    print("All tests passed!")
