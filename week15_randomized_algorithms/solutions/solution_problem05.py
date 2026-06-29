"""
Problem 05 - Contention Resolution Simulation (SOLUTION)
=========================================================
"""

import math
import random


def simulate_contention(n: int, seed: int) -> int:
    """Simulate n processes (p = 1/n per round); return rounds until ALL succeed."""
    rng = random.Random(seed)
    p = 1.0 / n
    succeeded = [False] * n
    remaining = n
    rounds = 0
    while remaining > 0:
        rounds += 1
        attempts = [(not succeeded[i]) and (rng.random() < p) for i in range(n)]
        num_attempts = sum(attempts)
        if num_attempts == 1:
            i = attempts.index(True)
            if not succeeded[i]:
                succeeded[i] = True
                remaining -= 1
    return rounds


def average_rounds(n: int, num_trials: int, seed: int) -> float:
    """Average number of rounds until all succeed, over seeded trials."""
    total = 0
    for trial in range(num_trials):
        total += simulate_contention(n, seed=seed + trial)
    return total / num_trials


if __name__ == "__main__":
    # Single run terminates and returns a positive number of rounds.
    for seed in range(20):
        r = simulate_contention(8, seed)
        assert r >= 1

    # The average grows like Theta(n log n): it should sit in a loose
    # constant-factor window around n * ln(n). The window is wide enough that a
    # correct simulation never flakes.
    for n in (10, 20):
        avg = average_rounds(n, num_trials=200, seed=12345)
        nln = n * math.log(n)
        # O(n log n) upper end with the e factor; lower end well below n ln n.
        assert 0.3 * nln <= avg <= 6.0 * nln, (n, avg, nln)

    print("All tests passed!")
