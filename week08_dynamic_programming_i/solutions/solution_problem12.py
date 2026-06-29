"""
Problem 12 - Memoization vs Bottom-Up: Counting Subproblem Work (SOLUTION)
==========================================================================

We instrument three ways of computing the n-th Fibonacci number -- the cleanest
example of OVERLAPPING SUBPROBLEMS -- and count how many recursive calls /
table writes each performs:

  * naive_fib:    plain recursion, no memoization. Number of calls grows
                  EXPONENTIALLY (about Fib(n) leaves), re-solving the same
                  subproblems again and again.
  * memoized_fib: top-down recursion with a cache. Each distinct subproblem
                  fib(k) for k = 0..n is computed exactly ONCE, so the number of
                  *distinct* subproblems is LINEAR in n.
  * bottom_up_fib: an explicit table filled k = 0..n, doing n+1 units of work.

The point of the exercise: DP turns exponential repeated work into linear work
by SOLVING EACH SUBPROBLEM ONCE.
"""

from typing import Dict, Tuple


def naive_fib(n: int) -> Tuple[int, int]:
    """Return (fib(n), call_count) for plain (un-memoized) recursion."""
    calls = 0

    def rec(k: int) -> int:
        nonlocal calls
        calls += 1
        if k < 2:
            return k
        return rec(k - 1) + rec(k - 2)

    value = rec(n)
    return value, calls


def memoized_fib(n: int) -> Tuple[int, int]:
    """Return (fib(n), distinct_subproblems) for top-down memoized recursion.

    distinct_subproblems counts how many distinct fib(k) values were actually
    COMPUTED (i.e. cache misses), which for k = 0..n is n+1.
    """
    memo: Dict[int, int] = {}
    computed = 0

    def rec(k: int) -> int:
        nonlocal computed
        if k in memo:
            return memo[k]
        computed += 1
        if k < 2:
            memo[k] = k
        else:
            memo[k] = rec(k - 1) + rec(k - 2)
        return memo[k]

    value = rec(n)
    return value, computed


def bottom_up_fib(n: int) -> Tuple[int, int]:
    """Return (fib(n), table_writes) for explicit bottom-up DP."""
    if n < 2:
        return n, n + 1
    dp = [0] * (n + 1)
    dp[1] = 1
    writes = 2  # dp[0], dp[1]
    for k in range(2, n + 1):
        dp[k] = dp[k - 1] + dp[k - 2]
        writes += 1
    return dp[n], writes


if __name__ == "__main__":
    # All three agree on the actual Fibonacci value.
    for n in range(0, 25):
        v_naive, _ = naive_fib(n)
        v_memo, _ = memoized_fib(n)
        v_bottom, _ = bottom_up_fib(n)
        assert v_naive == v_memo == v_bottom

    # Memoized work is LINEAR. For n >= 2 every fib(k), k = 0..n, is reached
    # exactly once, so n+1 distinct subproblems are computed. (For n = 0 or 1
    # the recursion bottoms out immediately and reaches only 1 subproblem.)
    assert memoized_fib(0)[1] == 1
    assert memoized_fib(1)[1] == 1
    for n in range(2, 30):
        _, computed = memoized_fib(n)
        assert computed == n + 1

    # Bottom-up does linear work too: n+1 table writes.
    for n in range(0, 30):
        _, writes = bottom_up_fib(n)
        assert writes == n + 1

    # Naive recursion is EXPONENTIAL and dwarfs the DP work for moderate n.
    _, naive_calls = naive_fib(25)
    _, memo_calls = memoized_fib(25)
    assert naive_calls > 100 * memo_calls   # exponential vs linear blow-up

    # Concretely: number of naive calls for fib(n) is 2*Fib(n+1) - 1.
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    for n in range(0, 20):
        _, calls = naive_fib(n)
        assert calls == 2 * fib(n + 1) - 1

    print("All tests passed!")
