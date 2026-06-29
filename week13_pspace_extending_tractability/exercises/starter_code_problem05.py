"""
Problem 05 - Verify FPT Vertex Cover vs Brute-Force Minimum
===========================================================

Implement `verify_fpt_vertex_cover(num_trials, n, seed)`: for each of
``num_trials`` random graphs (``generate_graph(n, p=0.4, seed=seed + trial)``),
find the minimum vertex cover size both ways and confirm they agree:
  - brute force via ``brute_force_vertex_cover`` (starter_code.py), and
  - the FPT decider from Problem 4, called with increasing k.
Also confirm the FPT decision threshold is exact: a cover of size ``opt``
exists but one of size ``opt - 1`` does not.

Return True iff all checks pass for every trial.

The helper `min_vertex_cover_via_fpt(n, edges)` (find the smallest k for which
the decider succeeds) is also expected.

See practical_exercises.pdf, Problem 5.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import brute_force_vertex_cover, generate_graph  # noqa: E402
from starter_code_problem04 import vertex_cover_fpt  # noqa: E402


def min_vertex_cover_via_fpt(n, edges):
    """Find the minimum cover size by trying k = 0, 1, 2, ... with the FPT decider."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_fpt_vertex_cover(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff FPT and brute force agree, with an exact threshold,
    for every random trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_fpt_vertex_cover(num_trials=30, n=8, seed=1) is True
        assert verify_fpt_vertex_cover(num_trials=20, n=10, seed=100) is True
        assert verify_fpt_vertex_cover(num_trials=15, n=6, seed=999) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
