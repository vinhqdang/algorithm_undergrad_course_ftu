"""
Problem 02 - Mergesort with a Comparison Counter
=================================================

Implement `mergesort(arr, counter=None)`: return a NEW sorted list (do not
mutate `arr`), using recursive divide-and-conquer mergesort. If a `Counter`
(from starter_code.py) is passed, call `counter.tick()` once per element
comparison performed while merging, so the total reflects the comparison count
(which is O(n log n)).

See practical_exercises.pdf, Problem 2.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List, Optional

from starter_code import Counter, generate_array, is_sorted


def mergesort(arr: List[int], counter: Optional[Counter] = None) -> List[int]:
    """Return a new sorted copy of `arr`; count comparisons in `counter`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    import math

    try:
        assert mergesort([3, 1, 2]) == [1, 2, 3]
        assert mergesort([]) == []
        assert mergesort([5]) == [5]
        assert mergesort([2, 2, 1, 1]) == [1, 1, 2, 2]

        for seed in range(20):
            a = generate_array(50, seed=seed)
            out = mergesort(a)
            assert out == sorted(a)
            assert is_sorted(out)
            assert a == generate_array(50, seed=seed)  # input not mutated

        # Comparison count is O(n log n): never exceeds n * ceil(log2 n).
        c = Counter()
        a = generate_array(64, seed=99)
        mergesort(a, c)
        assert c.count <= 64 * math.ceil(math.log2(64))

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
