"""
Problem 02 - Brute-Force SAT Solver (SOLUTION)
================================================
"""

import itertools
from typing import List, Optional, Tuple

Clause = List[int]
Formula = List[Clause]
Assignment = Tuple[bool, ...]


def num_variables(formula: Formula) -> int:
    """Largest variable index appearing in `formula` (0 if none)."""
    m = 0
    for clause in formula:
        for lit in clause:
            m = max(m, abs(lit))
    return m


def _satisfies(formula: Formula, assignment: Assignment) -> bool:
    for clause in formula:
        if not any(
            (lit > 0 and assignment[abs(lit) - 1])
            or (lit < 0 and not assignment[abs(lit) - 1])
            for lit in clause
        ):
            return False
    return True


def brute_force_sat(formula: Formula) -> Optional[Assignment]:
    """Try all 2**n assignments; return a satisfying one, or None."""
    n = num_variables(formula)
    for bits in itertools.product((False, True), repeat=n):
        if _satisfies(formula, bits):
            return bits
    return None


if __name__ == "__main__":
    # Satisfiable formula
    a = brute_force_sat([[1, -2], [2, 3]])
    assert a is not None
    assert _satisfies([[1, -2], [2, 3]], a)

    # Classic unsatisfiable: (x1) AND (NOT x1)
    assert brute_force_sat([[1], [-1]]) is None

    # All four clauses over 1 var that exclude both values -> unsat
    assert brute_force_sat([[1], [-1]]) is None

    # Trivially satisfiable empty formula -> empty assignment
    assert brute_force_sat([]) == ()

    # Unsatisfiable: every clause is the empty clause
    assert brute_force_sat([[]]) is None

    # 3-variable satisfiable
    f = [[1, 2, 3], [-1, -2], [-2, -3], [1, -3]]
    a = brute_force_sat(f)
    assert a is not None and _satisfies(f, a)

    print("All tests passed!")
