"""
Problem 02 - Interval Depth (Maximum Overlap)
================================================

Implement `interval_depth_scratch(intervals)` WITHOUT using `interval_depth`
from starter_code.py.

The *depth* of a set of intervals is the maximum number of intervals that are
"active" (their [start, finish) range contains some common point) at the same
time. Equivalently, it is the minimum number of resources (e.g. classrooms)
needed so every interval can be assigned a resource with no overlap on a
single resource (this fact is used in Problem 8).

Hint: a standard approach is the "sweep line": create a +1 event at each
start time and a -1 event at each finish time, sort all events by time
(processing -1 events before +1 events at the same time, since [start,
finish) is half-open), and track the running sum -- its maximum value is the
depth.

See practical_exercises.pdf, Problem 2.
"""

from typing import List, Tuple

Interval = Tuple[float, float]


def interval_depth_scratch(intervals: List[Interval]) -> int:
    """Return the maximum number of intervals overlapping at any point in time."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Three intervals all overlapping at time 2
        assert interval_depth_scratch([(0, 5), (1, 4), (2, 6)]) == 3

        # Disjoint intervals -> depth 1
        assert interval_depth_scratch([(0, 1), (1, 2), (2, 3)]) == 1

        # Empty input -> depth 0
        assert interval_depth_scratch([]) == 0

        # Two intervals touching at an endpoint do not overlap
        assert interval_depth_scratch([(0, 2), (2, 4)]) == 1

        # Classic textbook example (Kleinberg & Tardos, Ch 4):
        # several lectures with varying overlap, max simultaneous = 3
        intervals = [(0, 3), (1, 4), (2, 5), (6, 8), (7, 9)]
        assert interval_depth_scratch(intervals) == 3

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
