"""
Problem 11 - Karatsuba vs. Grade-School Multiplication Counts (SOLUTION)
========================================================================
"""

from typing import List, Tuple


def karatsuba_mults(n: int) -> int:
    """Base-case multiplications for T(n) = 3 T(n/2) + O(n), T(1)=1."""
    if n <= 1:
        return 1
    return 3 * karatsuba_mults(n // 2)


def gradeschool_mults(n: int) -> int:
    """Base-case multiplications for T(n) = 4 T(n/2) + O(n), T(1)=1."""
    if n <= 1:
        return 1
    return 4 * gradeschool_mults(n // 2)


def compare_growth(max_power: int) -> List[Tuple[int, int, int, float]]:
    """Return [(n, gradeschool, karatsuba, ratio)] for n = 2^1 .. 2^max_power."""
    rows: List[Tuple[int, int, int, float]] = []
    for power in range(1, max_power + 1):
        n = 2 ** power
        gs = gradeschool_mults(n)
        ka = karatsuba_mults(n)
        rows.append((n, gs, ka, gs / ka))
    return rows


if __name__ == "__main__":
    assert karatsuba_mults(1) == 1
    assert karatsuba_mults(2) == 3
    assert karatsuba_mults(4) == 9
    assert karatsuba_mults(8) == 27

    assert gradeschool_mults(1) == 1
    assert gradeschool_mults(2) == 4
    assert gradeschool_mults(4) == 16
    assert gradeschool_mults(8) == 64

    rows = compare_growth(6)
    assert len(rows) == 6
    assert rows[0][0] == 2 and rows[-1][0] == 64
    for n, gs, ka, ratio in rows:
        assert gs == gradeschool_mults(n)
        assert ka == karatsuba_mults(n)
        assert abs(ratio - gs / ka) < 1e-9
    ratios = [r[3] for r in rows]
    assert all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))

    print("All tests passed!")
