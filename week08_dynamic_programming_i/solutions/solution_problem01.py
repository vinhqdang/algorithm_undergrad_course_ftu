"""
Problem 01 - Compute p(j) for Weighted Interval Scheduling (SOLUTION)
======================================================================
"""

import bisect
from typing import List, Tuple

WeightedInterval = Tuple[float, float, float]


def compute_p(intervals: List[WeightedInterval]) -> List[int]:
    """Return p where, after sorting intervals by finish time, p[j] is the
    index of the latest interval i < j compatible with j, or -1 if none.

    Returns the p-array indexed by position in the finish-sorted order.
    """
    ordered = sorted(intervals, key=lambda iv: iv[1])
    finishes = [iv[1] for iv in ordered]
    p = []
    for j, (s_j, _, _) in enumerate(ordered):
        # We want the rightmost interval whose finish time <= s_j.
        # bisect_right on finishes gives the count of finishes <= s_j.
        idx = bisect.bisect_right(finishes, s_j) - 1
        # idx must refer to an interval strictly before j in the ordering.
        if idx >= j:
            idx = j - 1
        p.append(idx)
    return p


if __name__ == "__main__":
    # Classic example (Kleinberg-Tardos), already finish-sorted:
    # intervals (s, f, w): finishes 2,4,6,7,9,10 ... use a small custom set.
    ivs = [(0, 3, 1), (1, 4, 1), (3, 5, 1), (5, 7, 1)]
    # finish-sorted order is the same; p:
    #   j=0 (0,3): no earlier compatible -> -1
    #   j=1 (1,4): earliest finish <= 1? none -> -1
    #   j=2 (3,5): finish <=3 is interval 0 (f=3) -> 0
    #   j=3 (5,7): finish <=5 is interval 2 (f=5) -> 2
    assert compute_p(ivs) == [-1, -1, 0, 2]

    # All mutually compatible (back to back): p[j] = j-1.
    chain = [(0, 1, 5), (1, 2, 5), (2, 3, 5), (3, 4, 5)]
    assert compute_p(chain) == [-1, 0, 1, 2]

    # All mutually overlapping: p[j] = -1 for all j.
    overlap = [(0, 10, 1), (0, 11, 1), (0, 12, 1)]
    assert compute_p(overlap) == [-1, -1, -1]

    # Single interval.
    assert compute_p([(0, 5, 3)]) == [-1]
    assert compute_p([]) == []

    print("All tests passed!")
