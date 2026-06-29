"""
Problem 10 - Max-Cut Local Search (Vertex Flips)
=================================================

Implement `max_cut_local_search(graph, seed)`: start from a seeded random
partition `side` (a list of 0/1 per vertex); while some vertex has more edges to
its OWN side than to the other side, flip it (this strictly increases the cut).
Return (side, cut). Then `verify_local_optimum_half(num_trials, n, p, seed)`:
check that the returned cut is >= m/2 on every random graph.

Use `cut_value` and `neighbors` from starter_code.py.

See practical_exercises.pdf, Problem 10.
"""

import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cut_value, generate_graph, neighbors  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def max_cut_local_search(graph: Graph, seed: int = 0) -> Tuple[List[int], int]:
    """Local search for Max-Cut via single-vertex flips. Return (side, cut)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_local_optimum_half(num_trials: int, n: int, p: float, seed: int) -> bool:
    """Return True iff the local-optimum cut is >= m/2 on every random graph."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        tri = (3, [(0, 1), (0, 2), (1, 2)])
        _, cut = max_cut_local_search(tri, seed=0)
        assert cut >= len(tri[1]) / 2
        assert cut == 2

        k22 = (4, [(0, 2), (0, 3), (1, 2), (1, 3)])
        _, cut = max_cut_local_search(k22, seed=1)
        assert cut == 4

        _, cut = max_cut_local_search((5, []), seed=0)
        assert cut == 0

        assert verify_local_optimum_half(num_trials=100, n=12, p=0.3, seed=10) is True
        assert verify_local_optimum_half(num_trials=100, n=15, p=0.5, seed=99) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
