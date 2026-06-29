"""
Problem 02 - Verifying the 2-Approximation for Vertex Cover
===========================================================

Implement `brute_force_min_vertex_cover(graph)` returning the size of a MINIMUM
vertex cover (try all 2^n subsets, smallest first). Then implement
`verify_vc_2approx(num_trials, n, p, seed)`: for each random graph, check that
the matching cover (Problem 1) has size <= 2 * OPT. Intended for n <= 15.

You may import `vertex_cover_matching` from your Problem 1 solution; here we
re-implement it locally so this file is self-contained.

See practical_exercises.pdf, Problem 2.
"""

import itertools
import os
import sys
from typing import List, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_graph, is_vertex_cover  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def vertex_cover_matching(graph: Graph) -> Set[int]:
    """Maximal-matching vertex cover (copied from Problem 1)."""
    _, edges = graph
    cover: Set[int] = set()
    for u, v in edges:
        if u not in cover and v not in cover:
            cover.add(u)
            cover.add(v)
    return cover


def brute_force_min_vertex_cover(graph: Graph) -> int:
    """Return the size of a minimum vertex cover."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_vc_2approx(num_trials: int, n: int, p: float, seed: int) -> bool:
    """Return True iff |matching cover| <= 2 * OPT on every random trial."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        g = (4, [(0, 1), (1, 2), (2, 3)])
        assert brute_force_min_vertex_cover(g) == 2
        assert len(vertex_cover_matching(g)) <= 2 * 2

        tri = (3, [(0, 1), (0, 2), (1, 2)])
        assert brute_force_min_vertex_cover(tri) == 2

        assert brute_force_min_vertex_cover((5, [])) == 0

        assert verify_vc_2approx(num_trials=40, n=10, p=0.3, seed=1) is True
        assert verify_vc_2approx(num_trials=20, n=12, p=0.5, seed=100) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
