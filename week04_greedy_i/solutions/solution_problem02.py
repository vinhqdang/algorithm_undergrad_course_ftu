"""
Problem 02 - Interval Depth (Maximum Overlap) (SOLUTION)
===========================================================
"""

from typing import List, Tuple

Interval = Tuple[float, float]


def interval_depth_scratch(intervals: List[Interval]) -> int:
    """Return the maximum number of intervals overlapping at any point in time."""
    events = []
    for s, f in intervals:
        events.append((s, 1))
        events.append((f, -1))

    # Process -1 (endings) before +1 (starts) at equal times.
    events.sort(key=lambda e: (e[0], e[1]))

    active = 0
    max_active = 0
    for _, delta in events:
        active += delta
        max_active = max(max_active, active)
    return max_active


if __name__ == "__main__":
    assert interval_depth_scratch([(0, 5), (1, 4), (2, 6)]) == 3
    assert interval_depth_scratch([(0, 1), (1, 2), (2, 3)]) == 1
    assert interval_depth_scratch([]) == 0
    assert interval_depth_scratch([(0, 2), (2, 4)]) == 1

    intervals = [(0, 3), (1, 4), (2, 5), (6, 8), (7, 9)]
    assert interval_depth_scratch(intervals) == 3

    print("All tests passed!")
