"""
Problem 11 - Karatsuba vs. Grade-School Multiplication Counts
=============================================================

We do not implement full big-integer multiplication here (that is next week);
instead we COUNT multiplications to compare two recurrences. Assume n is a
power of 2.

Implement:
  - `karatsuba_mults(n)`: number of base-case multiplications for
    T(n) = 3 T(n/2) + O(n), with T(1) = 1. Closed form: 3^k = n^(log2 3).
  - `gradeschool_mults(n)`: number of base-case multiplications for
    T(n) = 4 T(n/2) + O(n), with T(1) = 1. Closed form: 4^k = n^2.
  - `compare_growth(max_power)`: return a list of tuples
    (n, gradeschool, karatsuba, ratio) for n = 2^1 .. 2^max_power, where
    ratio = gradeschool / karatsuba. The ratio should grow with n.

See practical_exercises.pdf, Problem 11.
"""

from typing import List, Tuple


def karatsuba_mults(n: int) -> int:
    """Base-case multiplications for T(n) = 3 T(n/2) + O(n), T(1)=1."""
    # TODO: implement this function.
    raise NotImplementedError


def gradeschool_mults(n: int) -> int:
    """Base-case multiplications for T(n) = 4 T(n/2) + O(n), T(1)=1."""
    # TODO: implement this function.
    raise NotImplementedError


def compare_growth(max_power: int) -> List[Tuple[int, int, int, float]]:
    """Return [(n, gradeschool, karatsuba, ratio)] for n = 2^1 .. 2^max_power."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert karatsuba_mults(1) == 1
        assert karatsuba_mults(2) == 3
        assert karatsuba_mults(4) == 9
        assert karatsuba_mults(8) == 27   # 3^3

        assert gradeschool_mults(1) == 1
        assert gradeschool_mults(2) == 4
        assert gradeschool_mults(4) == 16
        assert gradeschool_mults(8) == 64  # 4^3

        rows = compare_growth(6)
        assert len(rows) == 6
        assert rows[0][0] == 2 and rows[-1][0] == 64
        for n, gs, ka, ratio in rows:
            assert gs == gradeschool_mults(n)
            assert ka == karatsuba_mults(n)
            assert abs(ratio - gs / ka) < 1e-9
        # The ratio strictly grows as n grows.
        ratios = [r[3] for r in rows]
        assert all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
