"""
Problem 10 - Miller-Rabin Primality Test (SOLUTION)
====================================================
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def miller_rabin(n: int, seed: int, rounds: int = 20) -> bool:
    """Probabilistic primality test with `rounds` random witnesses (seeded)."""
    if n < 2:
        return False
    # Small primes / trivial divisibility.
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for sp in small_primes:
        if n == sp:
            return True
        if n % sp == 0:
            return False

    # Write n - 1 = 2^s * d with d odd.
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    rng = random.Random(seed)
    for _ in range(rounds):
        a = rng.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True


if __name__ == "__main__":
    from starter_code import is_prime_trial_division

    # Agree with deterministic trial division over a range, with a fixed seed.
    for n in range(0, 501):
        mr = miller_rabin(n, seed=2024, rounds=20)
        td = is_prime_trial_division(n)
        assert mr == td, (n, mr, td)

    # A few larger known primes / composites.
    assert miller_rabin(7919, seed=1, rounds=20) is True   # prime
    assert miller_rabin(7917, seed=1, rounds=20) is False  # composite
    assert miller_rabin(104729, seed=3, rounds=20) is True  # 10000th prime
    # Carmichael number 561 = 3*11*17 must be caught as composite.
    assert miller_rabin(561, seed=7, rounds=20) is False

    print("All tests passed!")
