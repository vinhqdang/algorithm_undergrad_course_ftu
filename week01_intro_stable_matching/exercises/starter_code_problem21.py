"""
Problem 21 - Recursion: Naive vs Memoized Fibonacci
======================================================

Implement `fib_naive(n)` returning `(value, call_count)` where `value` is the
n-th Fibonacci number (fib(0)=0, fib(1)=1) and `call_count` is the total
number of recursive calls made (including the initial call).

Then implement `fib_memo(n)` returning `(value, call_count)` using memoization
(a dict cache), where `call_count` should be much smaller -- O(n) instead of
exponential.

See practical_exercises.pdf, Problem 21.
"""

from typing import Dict, Tuple


def fib_naive(n: int) -> Tuple[int, int]:
    """Return (fib(n), total number of recursive calls)."""
    # TODO: implement.
    raise NotImplementedError


def fib_memo(n: int) -> Tuple[int, int]:
    """Return (fib(n), total number of recursive calls), using memoization."""
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for n, expected in [(0, 0), (1, 1), (2, 1), (10, 55)]:
            val, _ = fib_naive(n)
            assert val == expected, (n, val)
            val, _ = fib_memo(n)
            assert val == expected, (n, val)

        _, naive_calls = fib_naive(20)
        _, memo_calls = fib_memo(20)

        # Naive recursion is exponential; memoized is linear.
        assert memo_calls <= 2 * 20 + 2, memo_calls
        assert naive_calls > memo_calls
        assert naive_calls > 1000  # fib(20) naive makes thousands of calls

        print(f"fib(20): naive_calls={naive_calls}, memo_calls={memo_calls}")
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
