"""
Problem 10 - Miller-Rabin Primality Test
=========================================

Implement `miller_rabin(n, seed, rounds=20)`: the Miller-Rabin probabilistic
primality test with `rounds` random witnesses (seeded). Handle small/even cases
directly. Write n - 1 = 2^s * d with d odd, then for each witness a check the
Miller-Rabin condition.

See practical_exercises.pdf, Problem 10.
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def miller_rabin(n: int, seed: int, rounds: int = 20) -> bool:
    """Probabilistic primality test with `rounds` random witnesses (seeded)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        from starter_code import is_prime_trial_division

        for n in range(0, 501):
            mr = miller_rabin(n, seed=2024, rounds=20)
            td = is_prime_trial_division(n)
            assert mr == td, (n, mr, td)

        assert miller_rabin(7919, seed=1, rounds=20) is True
        assert miller_rabin(7917, seed=1, rounds=20) is False
        assert miller_rabin(104729, seed=3, rounds=20) is True
        assert miller_rabin(561, seed=7, rounds=20) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
