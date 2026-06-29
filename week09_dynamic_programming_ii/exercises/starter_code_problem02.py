"""
Problem 02 - Sequence Alignment with Custom Gap and Mismatch Costs
===================================================================

Implement `alignment_cost(x, y, gap, mismatch)` returning the minimum total cost
of aligning `x` and `y`, where each gap (insertion or deletion) costs `gap`, each
mismatch (aligning two different characters) costs `mismatch`, and matching equal
characters costs 0. This generalises Problem 1 (the case gap == mismatch == 1).

See practical_exercises.pdf, Problem 2, for the full statement and examples.
"""


def alignment_cost(x: str, y: str, gap: float, mismatch: float) -> float:
    """Return the minimum-cost alignment of x and y under given gap/mismatch costs."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert alignment_cost("kitten", "sitting", gap=1, mismatch=1) == 3
        assert alignment_cost("AT", "AAT", gap=2, mismatch=3) == 2
        assert alignment_cost("abc", "abc", gap=5, mismatch=5) == 0
        assert alignment_cost("", "abc", gap=2, mismatch=1) == 6
        assert alignment_cost("a", "b", gap=1, mismatch=5) == 2
        assert alignment_cost("a", "b", gap=5, mismatch=1) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
