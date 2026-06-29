"""
Problem 01 - Edit Distance (Levenshtein)
==========================================

Implement `edit_distance(x, y)` returning the Levenshtein edit distance between
two strings: the minimum number of single-character insertions, deletions, and
substitutions that turn `x` into `y`. Use the standard 2-D DP:

    OPT(i, 0) = i,  OPT(0, j) = j,
    OPT(i, j) = min( [x[i] != y[j]] + OPT(i-1, j-1),
                     1 + OPT(i-1, j),
                     1 + OPT(i, j-1) ).

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""


def edit_distance(x: str, y: str) -> int:
    """Return the Levenshtein edit distance between x and y."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert edit_distance("kitten", "sitting") == 3
        assert edit_distance("", "") == 0
        assert edit_distance("abc", "") == 3
        assert edit_distance("", "abc") == 3
        assert edit_distance("abc", "abc") == 0
        assert edit_distance("flaw", "lawn") == 2
        assert edit_distance("intention", "execution") == 5

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
