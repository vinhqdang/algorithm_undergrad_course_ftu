"""
Problem 04 - Longest Common Subsequence (Length + One LCS)
===========================================================

Implement `lcs(x, y)` returning (length, subseq) where `length` is the length of
a longest common subsequence of `x` and `y`, and `subseq` is one such subsequence
(a string). Use the standard DP and trace back to build the subsequence.

See practical_exercises.pdf, Problem 4, for the full statement and examples.
"""

from typing import Tuple


def lcs(x: str, y: str) -> Tuple[int, str]:
    """Return (length, subsequence) for a longest common subsequence of x and y."""
    # TODO: implement this function.
    raise NotImplementedError


def _is_subsequence(s: str, t: str) -> bool:
    it = iter(t)
    return all(ch in it for ch in s)


if __name__ == "__main__":
    try:
        length, sub = lcs("AGGTAB", "GXTXAYB")
        assert length == 4
        assert len(sub) == 4
        assert _is_subsequence(sub, "AGGTAB") and _is_subsequence(sub, "GXTXAYB")

        length, sub = lcs("abc", "abc")
        assert length == 3 and sub == "abc"

        length, sub = lcs("abc", "def")
        assert length == 0 and sub == ""

        length, sub = lcs("", "abc")
        assert length == 0 and sub == ""

        length, sub = lcs("AGCAT", "GAC")
        assert length == 2
        assert _is_subsequence(sub, "AGCAT") and _is_subsequence(sub, "GAC")

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
