"""
Problem 07 - Interval Partitioning (Earliest-Start-Time-First) (SOLUTION)
============================================================================
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
    assignment: Dict[Interval, int] = {}
    heap: List[Tuple[float, int]] = []  # (end_time, resource_id)
    next_resource_id = 0

    for s, f in sorted(intervals, key=lambda iv: iv[0]):
        if heap and heap[0][0] <= s:
            _, resource_id = heapq.heappop(heap)
        else:
            resource_id = next_resource_id
            next_resource_id += 1

        assignment[(s, f)] = resource_id
        heapq.heappush(heap, (f, resource_id))

    return assignment


if __name__ == "__main__":
    intervals = [(0, 3), (1, 4), (2, 5), (6, 8), (7, 9)]
    assignment = interval_partitioning(intervals)

    assert set(assignment.keys()) == set(intervals)
    num_resources_used = len(set(assignment.values()))
    assert num_resources_used == interval_depth(intervals) == 3

    assert set(assignment.values()) == set(range(num_resources_used))

    for r in range(num_resources_used):
        group = [iv for iv, res in assignment.items() if res == r]
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                s1, f1 = group[i]
                s2, f2 = group[j]
                assert not (s1 < f2 and s2 < f1)

    disjoint = [(0, 1), (1, 2), (2, 3)]
    assignment2 = interval_partitioning(disjoint)
    assert len(set(assignment2.values())) == 1

    print("All tests passed!")
