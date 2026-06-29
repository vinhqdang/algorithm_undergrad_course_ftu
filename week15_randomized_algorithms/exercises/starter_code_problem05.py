"""
Problem 05 - Contention Resolution Simulation
==============================================

Implement `simulate_contention(n, seed)`: simulate n processes that each attempt a
shared resource with probability p = 1/n per round; a process succeeds in a round
iff it is the ONLY one attempting. Return the number of rounds until ALL n have
succeeded at least once. Then implement `average_rounds(n, num_trials, seed)`
averaging this over seeded trials.

See practical_exercises.pdf, Problem 5.
"""

import math
import random


def simulate_contention(n: int, seed: int) -> int:
    """Simulate n processes (p = 1/n per round); return rounds until ALL succeed."""
    # TODO: implement this function.
    raise NotImplementedError


def average_rounds(n: int, num_trials: int, seed: int) -> float:
    """Average number of rounds until all succeed, over seeded trials."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for seed in range(20):
            r = simulate_contention(8, seed)
            assert r >= 1

        for n in (10, 20):
            avg = average_rounds(n, num_trials=200, seed=12345)
            nln = n * math.log(n)
            assert 0.3 * nln <= avg <= 6.0 * nln, (n, avg, nln)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
