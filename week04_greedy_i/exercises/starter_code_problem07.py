"""
Problem 07 - Interval Partitioning (Earliest-Start-Time-First)
=================================================================

Implement `interval_partitioning(intervals)`, the greedy algorithm for the
Interval Partitioning Problem: assign every interval to one of the smallest
possible number of "resources" (e.g. classrooms) so that no two intervals
assigned to the same resource overlap.

Algorithm (Kleinberg & Tardos, Ch 4.1):
    Sort intervals by start time. Maintain a min-heap of (end_time,
    resource_id) for resources currently "in use", keyed by the end time of
    the last interval assigned to that resource. For each interval (s, f) in
    order of start time:
        - If the heap is non-empty and its minimum end_time <= s, that
          resource is free: pop it, assign the interval to that resource_id,
          and push (f, resource_id) back onto the heap.
        - Otherwise, no resource is free: allocate a NEW resource (the next
          unused integer id, starting at 0), assign the interval to it, and
          push (f, new_id) onto the heap.

Return a dict mapping each interval (the tuple (start, finish)) to the
resource id (int) it was assigned to. If the same interval tuple appears more
than once in the input, treat each occurrence independently (use the index in
the sorted order, but the dict only needs to record SOME valid assignment per
distinct interval -- for the tests below, all intervals are distinct).

See practical_exercises.pdf, Problem 7.
"""

import heapq
import os
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import interval_depth

Interval = Tuple[float, float]


def interval_partitioning(intervals: List[Interval]) -> Dict[Interval, int]:
    """Return a dict mapping each interval to an assigned resource id (0-indexed)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Classic textbook lecture-scheduling example (depth 3 -> 3 classrooms).
        intervals = [(0, 3), (1, 4), (2, 5), (6, 8), (7, 9)]
        assignment = interval_partitioning(intervals)

        assert set(assignment.keys()) == set(intervals)
        num_resources_used = len(set(assignment.values()))
        assert num_resources_used == interval_depth(intervals) == 3

        # Resource ids are non-negative and contiguous starting from 0.
        assert set(assignment.values()) == set(range(num_resources_used))

        # No two intervals assigned the same resource may overlap.
        for r in range(num_resources_used):
            group = [iv for iv, res in assignment.items() if res == r]
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    s1, f1 = group[i]
                    s2, f2 = group[j]
                    assert not (s1 < f2 and s2 < f1)

        # Disjoint intervals -> 1 resource suffices.
        disjoint = [(0, 1), (1, 2), (2, 3)]
        assignment2 = interval_partitioning(disjoint)
        assert len(set(assignment2.values())) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
