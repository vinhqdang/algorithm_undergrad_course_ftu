"""
Problem 17 - Correctness via Induction: Sum and Power
========================================================

Implement `iterative_sum(n)`, which computes 0 + 1 + ... + n using a loop
that maintains the invariant: "after processing i, `total == 0+1+...+i`".
Return the final total (for n >= 0; return 0 if n < 0).

Implement `fast_power(base, exp)`, which computes `base ** exp` for
`exp >= 0` using repeated squaring (also known as binary exponentiation):

    fast_power(base, exp):
        if exp == 0: return 1
        half = fast_power(base, exp // 2)
        if exp is even: return half * half
        else: return half * half * base

This runs in O(log exp) multiplications rather than O(exp).

Then implement `verify_sum_invariant(n)` that re-implements `iterative_sum`
but additionally checks, *at every step* of the loop, that the invariant
`total == i*(i+1)//2` holds (using `assert`), and returns the final total. If
the invariant is ever violated, the assertion will raise -- the function
should simply propagate that (do not catch it).

Then implement `verify_fast_power(values)` where `values` is a list of
`(base, exp)` pairs, returning True iff `fast_power(base, exp) ==
base ** exp` for every pair.

See practical_exercises.pdf, Problem 17.
"""

from typing import List, Tuple


def iterative_sum(n: int) -> int:
    """Return 0 + 1 + ... + n (0 if n < 0)."""
    # TODO: implement this function.
    raise NotImplementedError


def fast_power(base: int, exp: int) -> int:
    """Return base ** exp using binary exponentiation, for exp >= 0."""
    # TODO: implement this function (recursively).
    raise NotImplementedError


def verify_sum_invariant(n: int) -> int:
    """Like iterative_sum(n), but asserts the loop invariant total == i*(i+1)//2 at every step."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_fast_power(values: List[Tuple[int, int]]) -> bool:
    """Check fast_power(base, exp) == base ** exp for every (base, exp) in values."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert iterative_sum(0) == 0
        assert iterative_sum(1) == 1
        assert iterative_sum(5) == 15
        assert iterative_sum(100) == 5050
        assert iterative_sum(-3) == 0

        assert fast_power(2, 0) == 1
        assert fast_power(2, 10) == 1024
        assert fast_power(3, 5) == 243
        assert fast_power(5, 1) == 5

        for n in [0, 1, 5, 10, 50]:
            assert verify_sum_invariant(n) == n * (n + 1) // 2

        assert verify_fast_power([(2, 0), (2, 10), (3, 5), (10, 6), (1, 100), (7, 7)])

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
