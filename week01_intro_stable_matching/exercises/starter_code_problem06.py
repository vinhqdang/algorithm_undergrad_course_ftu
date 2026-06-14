"""
Problem 06 - How Many Stable Matchings Are There?
===================================================

Using `all_stable_matchings` from Problem 5, implement
`average_num_stable_matchings(n, num_trials, seed)` that:

  1. Generates `num_trials` random instances of size n.
  2. Computes the number of stable matchings for each instance.
  3. Returns the average over all trials (a float).

Then, in `__main__`, compute and print this average for n = 1..5 with
num_trials=20, and observe how quickly it can grow.

See practical_exercises.pdf, Problem 6.
"""

import os
import sys
from statistics import mean

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem05 import all_stable_matchings
from starter_code import generate_instance


def average_num_stable_matchings(n: int, num_trials: int = 20, seed: int = 0) -> float:
    """Return the average number of stable matchings over `num_trials` random
    instances of size n."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for n in range(1, 6):
            avg = average_num_stable_matchings(n, num_trials=20, seed=100)
            assert avg >= 1.0
            print(f"n={n}: average number of stable matchings = {avg:.2f}")

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
