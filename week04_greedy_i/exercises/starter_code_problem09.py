"""
Problem 09 - Can K Resources Suffice?
========================================

Implement `min_resources_needed(intervals)` that returns the MINIMUM number
of resources needed to schedule all `intervals` with no overlap on a single
resource. By the theorem verified in Problem 8, this equals
`interval_depth(intervals)` -- but here, implement it WITHOUT calling
`interval_depth` directly: instead, run `interval_partitioning` (Problem 7)
and return the number of distinct resources it uses.

Then implement `can_schedule_with_k_resources(intervals, k)` that returns
True iff `min_resources_needed(intervals) <= k`, i.e. iff `k` resources
suffice.

See practical_exercises.pdf, Problem 9.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem07 import interval_partitioning

Interval = Tuple[float, float]


def min_resources_needed(intervals: List[Interval]) -> int:
    """Return the minimum number of resources needed to schedule all intervals."""
    # TODO: implement this function.
    raise NotImplementedError


def can_schedule_with_k_resources(intervals: List[Interval], k: int) -> bool:
    """Return True iff `k` resources suffice to schedule all intervals."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        intervals = [(0, 3), (1, 4), (2, 5), (6, 8), (7, 9)]
        assert min_resources_needed(intervals) == 3

        assert can_schedule_with_k_resources(intervals, 3) is True
        assert can_schedule_with_k_resources(intervals, 2) is False
        assert can_schedule_with_k_resources(intervals, 5) is True

        # Empty input needs 0 resources.
        assert min_resources_needed([]) == 0
        assert can_schedule_with_k_resources([], 0) is True

        # Disjoint intervals need only 1 resource.
        disjoint = [(0, 1), (1, 2), (2, 3)]
        assert min_resources_needed(disjoint) == 1
        assert can_schedule_with_k_resources(disjoint, 1) is True
        assert can_schedule_with_k_resources(disjoint, 0) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
