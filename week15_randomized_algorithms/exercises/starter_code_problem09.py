"""
Problem 09 - Las Vegas vs. Monte Carlo
=======================================

Task: find an index of `target` in `arr` (guaranteed to contain it).

- Implement `las_vegas_find(arr, target, seed)`: probe random indices until the
  target is found. ALWAYS correct; running time is random.
- Implement `monte_carlo_find(arr, target, max_probes, seed)`: probe at most
  `max_probes` random indices; return an index if found, else None. Fixed time;
  may fail (return None) but is NEVER wrong when it returns an index.

See practical_exercises.pdf, Problem 9.
"""

import random
from typing import List, Optional


def las_vegas_find(arr: List, target, seed: int) -> int:
    """Always-correct random search; returns an index i with arr[i] == target."""
    # TODO: implement this function.
    raise NotImplementedError


def monte_carlo_find(arr: List, target, max_probes: int, seed: int) -> Optional[int]:
    """Bounded random search; returns an index or None (never a wrong index)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        arr = list(range(100))
        target = 42

        for seed in range(500):
            i = las_vegas_find(arr, target, seed)
            assert arr[i] == target

        saw_success = False
        saw_failure = False
        for seed in range(500):
            i = monte_carlo_find(arr, target, max_probes=3, seed=seed)
            if i is None:
                saw_failure = True
            else:
                assert arr[i] == target
                saw_success = True
        assert saw_success and saw_failure

        successes = sum(
            1 for seed in range(200)
            if monte_carlo_find(arr, target, max_probes=2000, seed=seed) is not None
        )
        assert successes == 200

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
