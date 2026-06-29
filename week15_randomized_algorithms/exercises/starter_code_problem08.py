"""
Problem 08 - Monte Carlo Estimation of pi
==========================================

Implement `estimate_pi(num_samples, seed)`: throw `num_samples` random points
uniformly into [0,1]^2 (seeded) and return 4 * the fraction landing inside the
unit quarter-circle (x^2 + y^2 <= 1).

See practical_exercises.pdf, Problem 8.
"""

import math
import random


def estimate_pi(num_samples: int, seed: int) -> float:
    """Estimate pi by throwing `num_samples` random darts into the unit square."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        rough = estimate_pi(1000, seed=0)
        assert 2.5 < rough < 3.8, rough

        est = estimate_pi(200_000, seed=12345)
        assert abs(est - math.pi) < 0.1, (est, math.pi)

        est2 = estimate_pi(200_000, seed=67890)
        assert abs(est2 - math.pi) < 0.1, (est2, math.pi)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
