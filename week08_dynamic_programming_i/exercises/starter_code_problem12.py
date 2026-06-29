"""
Problem 12 - Memoization vs Bottom-Up: Counting Subproblem Work
==============================================================

This exercise makes the central DP idea measurable. We compute the n-th
Fibonacci number -- the textbook example of OVERLAPPING SUBPROBLEMS -- three
ways, INSTRUMENTING each to count its work:

  * `naive_fib(n)`    -> (fib(n), call_count):  plain recursion, no caching.
                         Count every recursive call. This grows EXPONENTIALLY.
  * `memoized_fib(n)` -> (fib(n), distinct_subproblems):  top-down recursion
                         with a cache. Count how many distinct fib(k) you
                         actually COMPUTE (cache misses). This is LINEAR: n+1.
  * `bottom_up_fib(n)`-> (fib(n), table_writes):  fill a table k = 0..n.
                         Count table writes. Also LINEAR: n+1.

Implement all three. The tests confirm the three values agree, that the DP
variants do n+1 units of work, and that naive recursion blows up exponentially
(naive_fib(25) does >100x the work of memoized_fib(25)).

Note: for naive recursion, the call count for fib(n) equals 2*Fib(n+1) - 1.

See practical_exercises.pdf, Problem 12.
"""

from typing import Tuple


def naive_fib(n: int) -> Tuple[int, int]:
    """Return (fib(n), call_count) for plain (un-memoized) recursion."""
    # TODO: implement this function.
    raise NotImplementedError


def memoized_fib(n: int) -> Tuple[int, int]:
    """Return (fib(n), distinct_subproblems) for top-down memoized recursion."""
    # TODO: implement this function.
    raise NotImplementedError


def bottom_up_fib(n: int) -> Tuple[int, int]:
    """Return (fib(n), table_writes) for explicit bottom-up DP."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for n in range(0, 25):
            v_naive, _ = naive_fib(n)
            v_memo, _ = memoized_fib(n)
            v_bottom, _ = bottom_up_fib(n)
            assert v_naive == v_memo == v_bottom

        assert memoized_fib(0)[1] == 1
        assert memoized_fib(1)[1] == 1
        for n in range(2, 30):
            _, computed = memoized_fib(n)
            assert computed == n + 1
        for n in range(0, 30):
            _, writes = bottom_up_fib(n)
            assert writes == n + 1

        _, naive_calls = naive_fib(25)
        _, memo_calls = memoized_fib(25)
        assert naive_calls > 100 * memo_calls

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
