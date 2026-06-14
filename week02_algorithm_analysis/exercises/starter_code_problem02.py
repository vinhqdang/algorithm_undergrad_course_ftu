"""
Problem 02 - Counting Operations in Nested Loops
==================================================

Implement three "instrumented" functions that count the number of times their
innermost operation runs, as a function of n:

  - `count_single_loop(n)`: a single loop `for i in range(n)`, one operation
    per iteration. Should return exactly n.

  - `count_nested_loop(n)`: a loop `for i in range(n)` containing an inner
    loop `for j in range(n)`, one operation per inner iteration. Should
    return exactly n*n.

  - `count_triangular_loop(n)`: a loop `for i in range(n)` containing an inner
    loop `for j in range(i)` (note: range(i), not range(n)), one operation per
    inner iteration. Should return exactly 0+1+...+(n-1) = n*(n-1)//2.

Then implement `tightest_bound(counts, n_values)` that, given a list of
operation counts measured at the corresponding `n_values`, returns the name
of the tightest matching growth class from
{"constant", "linear", "quadratic"} by checking which of n_values[i]**0,
n_values[i]**1, n_values[i]**2 the counts are closest to being proportional
to (use the ratio counts[i] / n_values[i]**k and check it is roughly
constant across all i, for the smallest k that works, within a relative
tolerance of 0.15).

See practical_exercises.pdf, Problem 2.
"""

from typing import List


def count_single_loop(n: int) -> int:
    """Count operations in a single for-loop over range(n)."""
    # TODO: implement this function.
    raise NotImplementedError


def count_nested_loop(n: int) -> int:
    """Count operations in a doubly-nested for-loop, both over range(n)."""
    # TODO: implement this function.
    raise NotImplementedError


def count_triangular_loop(n: int) -> int:
    """Count operations where the inner loop runs over range(i) for outer index i."""
    # TODO: implement this function.
    raise NotImplementedError


def tightest_bound(counts: List[int], n_values: List[int]) -> str:
    """Return the tightest growth class ("constant", "linear", "quadratic")
    consistent with `counts` measured at `n_values`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for n in [1, 5, 10, 50]:
            assert count_single_loop(n) == n
            assert count_nested_loop(n) == n * n
            assert count_triangular_loop(n) == n * (n - 1) // 2

        n_values = [10, 20, 40, 80]

        const_counts = [5 for _ in n_values]
        linear_counts = [count_single_loop(n) for n in n_values]
        quad_counts = [count_nested_loop(n) for n in n_values]

        assert tightest_bound(const_counts, n_values) == "constant"
        assert tightest_bound(linear_counts, n_values) == "linear"
        assert tightest_bound(quad_counts, n_values) == "quadratic"

        # The triangular loop is also quadratic (n*(n-1)/2 ~ n^2 / 2).
        tri_counts = [count_triangular_loop(n) for n in n_values]
        assert tightest_bound(tri_counts, n_values) == "quadratic"

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
