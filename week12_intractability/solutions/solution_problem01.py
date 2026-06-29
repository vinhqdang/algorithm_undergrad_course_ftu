"""
Problem 01 - SAT Verifier (SOLUTION)
=====================================
"""

from typing import List, Sequence

Clause = List[int]
Formula = List[Clause]


def verify_sat(formula: Formula, assignment: Sequence[bool]) -> bool:
    """Return True iff `assignment` satisfies every clause of `formula`."""
    for clause in formula:
        clause_satisfied = False
        for lit in clause:
            v = abs(lit)
            value = assignment[v - 1]
            if (lit > 0 and value) or (lit < 0 and not value):
                clause_satisfied = True
                break
        if not clause_satisfied:
            return False
    return True


if __name__ == "__main__":
    assert verify_sat([[1, -2], [2, 3]], (True, False, True)) is True
    assert verify_sat([[1, -2], [2, 3]], (True, True, False)) is True
    # (True, False, False): clause (x2 OR x3) is unsatisfied
    assert verify_sat([[1, -2], [2, 3]], (True, False, False)) is False
    # (False, True, False): clause (x1 OR NOT x2) is unsatisfied
    assert verify_sat([[1, -2], [2, 3]], (False, True, False)) is False
    # (x1 OR NOT x2) fails when x1=False, x2=True
    assert verify_sat([[1, -2]], (False, True)) is False
    # empty formula is satisfied by anything
    assert verify_sat([], (True,)) is True
    # a formula containing the empty clause is satisfied by nothing
    assert verify_sat([[]], (True,)) is False
    # all-positive clause
    assert verify_sat([[1, 2, 3]], (False, False, True)) is True
    assert verify_sat([[1, 2, 3]], (False, False, False)) is False

    print("All tests passed!")
