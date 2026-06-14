"""
Problem 06 - Counter-Example: Shortest-Interval-First Is Not Optimal
=======================================================================

A tempting greedy heuristic for Interval Scheduling is: "repeatedly pick the
SHORTEST remaining compatible interval" (instead of the one with the
earliest finish time). Implement `shortest_interval_first(intervals)`, which
applies exactly this rule:

    Sort requests by duration (finish - start), ascending. Repeatedly select
    the shortest remaining request that is compatible with everything chosen
    so far, discarding incompatible ones.

Then implement `counter_example_instance()`, returning a list of intervals on
which `shortest_interval_first` selects STRICTLY FEWER intervals than the
optimal (as computed by `brute_force_max_independent_set` from Problem 4) --
demonstrating that "shortest first" is not a correct greedy rule for Interval
Scheduling.

Hint: think of one short interval that overlaps with (and thereby blocks) two
or more longer, mutually-compatible intervals.

See practical_exercises.pdf, Problem 6.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem04 import brute_force_max_independent_set
from starter_code import is_feasible

Interval = Tuple[float, float]


def shortest_interval_first(intervals: List[Interval]) -> List[Interval]:
    """Greedily select the shortest remaining compatible interval, repeatedly."""
    # TODO: implement this function.
    raise NotImplementedError


def counter_example_instance() -> List[Interval]:
    """Return an instance where shortest_interval_first is strictly suboptimal."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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
    except NotImplementedError:
        print("TODO: implement the functions above.")
