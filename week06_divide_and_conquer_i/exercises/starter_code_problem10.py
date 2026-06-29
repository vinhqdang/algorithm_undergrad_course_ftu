"""
Problem 10 - Majority Element (Divide and Conquer)
===================================================

Implement `majority_element(arr)`: return the value occurring STRICTLY MORE THAN
floor(n/2) times, or None if no such value exists, using divide and conquer.
Recursively find each half's majority candidate; the only candidates for the
whole are these two, so count each candidate's occurrences across the full range
and return whichever (if any) exceeds n/2. Verify against direct counting with
collections.Counter.

See practical_exercises.pdf, Problem 10.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import Counter as CollCounter
from typing import List, Optional

from starter_code import generate_array


def majority_element(arr: List[int]) -> Optional[int]:
    """Return the strict majority element of `arr`, or None if none exists."""
    # TODO: implement this function.
    raise NotImplementedError


def _brute_force_majority(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    value, count = CollCounter(arr).most_common(1)[0]
    return value if count > len(arr) // 2 else None


if __name__ == "__main__":
    try:
        assert majority_element([3, 3, 4, 2, 3, 3, 3]) == 3
        assert majority_element([1, 2, 3, 4]) is None
        assert majority_element([7]) == 7
        assert majority_element([]) is None
        assert majority_element([2, 2, 2, 2]) == 2
        assert majority_element([1, 1, 2, 2]) is None  # tie, no strict majority

        for seed in range(50):
            # Bias toward producing a majority sometimes.
            arr = generate_array(31, seed=seed, lo=0, hi=3)
            assert majority_element(arr) == _brute_force_majority(arr)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
