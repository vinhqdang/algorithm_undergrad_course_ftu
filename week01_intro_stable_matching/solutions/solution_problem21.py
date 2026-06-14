"""
Problem 21 - Recursion: Naive vs Memoized Fibonacci (SOLUTION)
=================================================================
"""

from typing import Dict, Tuple


def fib_naive(n: int) -> Tuple[int, int]:
    """Return (fib(n), total number of recursive calls)."""
    counter = [0]

    def helper(k: int) -> int:
        counter[0] += 1
        if k < 2:
            return k
        return helper(k - 1) + helper(k - 2)

    value = helper(n)
    return value, counter[0]


def fib_memo(n: int) -> Tuple[int, int]:
    """Return (fib(n), total number of recursive calls), using memoization."""
    cache: Dict[int, int] = {}
    counter = [0]

    def helper(k: int) -> int:
        counter[0] += 1
        if k in cache:
            return cache[k]
        if k < 2:
            cache[k] = k
            return k
        cache[k] = helper(k - 1) + helper(k - 2)
        return cache[k]

    value = helper(n)
    return value, counter[0]


if __name__ == "__main__":
    for n, expected in [(0, 0), (1, 1), (2, 1), (10, 55)]:
        val, _ = fib_naive(n)
        assert val == expected, (n, val)
        val, _ = fib_memo(n)
        assert val == expected, (n, val)

    _, naive_calls = fib_naive(20)
    _, memo_calls = fib_memo(20)

    assert memo_calls <= 2 * 20 + 2, memo_calls
    assert naive_calls > memo_calls
    assert naive_calls > 1000

    print(f"fib(20): naive_calls={naive_calls}, memo_calls={memo_calls}")
    print("All tests passed!")
