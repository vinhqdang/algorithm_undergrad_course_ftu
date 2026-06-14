"""
Problem 02 - Counting Operations in Nested Loops (SOLUTION)
==============================================================
"""

from typing import List


def count_single_loop(n: int) -> int:
    """Count operations in a single for-loop over range(n)."""
    ops = 0
    for _ in range(n):
        ops += 1
    return ops


def count_nested_loop(n: int) -> int:
    """Count operations in a doubly-nested for-loop, both over range(n)."""
    ops = 0
    for _ in range(n):
        for _ in range(n):
            ops += 1
    return ops


def count_triangular_loop(n: int) -> int:
    """Count operations where the inner loop runs over range(i) for outer index i."""
    ops = 0
    for i in range(n):
        for _ in range(i):
            ops += 1
    return ops


def tightest_bound(counts: List[int], n_values: List[int]) -> str:
    """Return the tightest growth class ("constant", "linear", "quadratic")
    consistent with `counts` measured at `n_values`."""
    tol = 0.15
    for k, name in [(0, "constant"), (1, "linear"), (2, "quadratic")]:
        ratios = [c / (n ** k) for c, n in zip(counts, n_values)]
        base = ratios[0]
        if base == 0:
            continue
        if all(abs(r - base) / abs(base) <= tol for r in ratios):
            return name
    return "unknown"


if __name__ == "__main__":
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

    tri_counts = [count_triangular_loop(n) for n in n_values]
    assert tightest_bound(tri_counts, n_values) == "quadratic"

    print("All tests passed!")
