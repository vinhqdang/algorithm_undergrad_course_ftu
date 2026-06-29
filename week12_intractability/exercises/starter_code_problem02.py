"""
Problem 02 - Brute-Force SAT Solver
====================================

Implement `brute_force_sat(formula)`: try all 2**n assignments over the
n = num_variables(formula) variables and return the first satisfying assignment
found (as a tuple of booleans), or None if the formula is unsatisfiable.

You may reuse `num_variables` and `all_assignments` from starter_code.py
(here `num_variables` and a helper are provided locally so the file is
self-contained).

See practical_exercises.pdf, Problem 2.
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
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        a = brute_force_sat([[1, -2], [2, 3]])
        assert a is not None
        assert _satisfies([[1, -2], [2, 3]], a)

        assert brute_force_sat([[1], [-1]]) is None
        assert brute_force_sat([]) == ()
        assert brute_force_sat([[]]) is None

        f = [[1, 2, 3], [-1, -2], [-2, -3], [1, -3]]
        a = brute_force_sat(f)
        assert a is not None and _satisfies(f, a)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
