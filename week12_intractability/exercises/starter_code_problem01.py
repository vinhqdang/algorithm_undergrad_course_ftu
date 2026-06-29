"""
Problem 01 - SAT Verifier
==========================

Implement `verify_sat(formula, assignment)`.

A CNF *formula* is a list of clauses; each clause is a list of signed integers
(literals). A positive literal `v` means "variable v is True"; `-v` means
"variable v is False". An *assignment* is a sequence of booleans where
assignment[v-1] is the truth value of variable v.

The formula is satisfied iff EVERY clause has at least one true literal.
A literal v > 0 is true iff assignment[v-1] is True; a literal v < 0 is true
iff assignment[-v-1] is False.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

from typing import List, Sequence

Clause = List[int]
Formula = List[Clause]


def verify_sat(formula: Formula, assignment: Sequence[bool]) -> bool:
    """Return True iff `assignment` satisfies every clause of `formula`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_sat([[1, -2], [2, 3]], (True, False, True)) is True
        assert verify_sat([[1, -2], [2, 3]], (True, True, False)) is True
        assert verify_sat([[1, -2], [2, 3]], (True, False, False)) is False
        assert verify_sat([[1, -2], [2, 3]], (False, True, False)) is False
        assert verify_sat([[1, -2]], (False, True)) is False
        assert verify_sat([], (True,)) is True
        assert verify_sat([[]], (True,)) is False
        assert verify_sat([[1, 2, 3]], (False, False, True)) is True
        assert verify_sat([[1, 2, 3]], (False, False, False)) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
