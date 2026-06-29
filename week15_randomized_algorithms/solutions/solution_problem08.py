"""
Problem 08 - Monte Carlo Estimation of pi (SOLUTION)
=====================================================
"""

import math
import random


def estimate_pi(num_samples: int, seed: int) -> float:
    """Estimate pi by throwing `num_samples` random darts into the unit square."""
    rng = random.Random(seed)
    inside = 0
    for _ in range(num_samples):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / num_samples


if __name__ == "__main__":
    # Small sample: should at least be in a plausible range.
    rough = estimate_pi(1000, seed=0)
    assert 2.5 < rough < 3.8, rough

    # Large sample with a fixed seed lands within a loose tolerance of pi.
    est = estimate_pi(200_000, seed=12345)
    assert abs(est - math.pi) < 0.1, (est, math.pi)

    # A second fixed seed also stays within tolerance (no flakiness).
    est2 = estimate_pi(200_000, seed=67890)
    assert abs(est2 - math.pi) < 0.1, (est2, math.pi)

    print("All tests passed!")
