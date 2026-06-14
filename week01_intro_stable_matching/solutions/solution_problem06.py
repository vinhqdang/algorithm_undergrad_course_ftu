"""
Problem 06 - How Many Stable Matchings Are There? (SOLUTION)
==============================================================
"""

import os
import sys
from statistics import mean

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem05 import all_stable_matchings
from starter_code import generate_instance


def average_num_stable_matchings(n: int, num_trials: int = 20, seed: int = 0) -> float:
    """Return the average number of stable matchings over `num_trials` random
    instances of size n."""
    counts = []
    for trial in range(num_trials):
        men, women, men_prefs, women_prefs = generate_instance(n, seed=seed + trial)
        counts.append(len(all_stable_matchings(men, women, men_prefs, women_prefs)))
    return mean(counts)


if __name__ == "__main__":
    for n in range(1, 6):
        avg = average_num_stable_matchings(n, num_trials=20, seed=100)
        assert avg >= 1.0
        print(f"n={n}: average number of stable matchings = {avg:.2f}")

    print("All tests passed!")
