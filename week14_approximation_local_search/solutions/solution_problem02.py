"""
Problem 02 - Verifying the 2-Approximation for Vertex Cover (SOLUTION)
======================================================================
"""

import itertools
import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import generate_graph, is_vertex_cover  # noqa: E402
from solution_problem01 import vertex_cover_matching  # noqa: E402

Graph = Tuple[int, List[Tuple[int, int]]]


def brute_force_min_vertex_cover(graph: Graph) -> int:
    """Return the size of a minimum vertex cover by trying all subsets, smallest first."""
    n, edges = graph
    if not edges:
        return 0
    vertices = list(range(n))
    for size in range(n + 1):
        for subset in itertools.combinations(vertices, size):
            if is_vertex_cover(graph, set(subset)):
                return size
    return n  # unreachable for a valid graph


def verify_vc_2approx(num_trials: int, n: int, p: float, seed: int) -> bool:
    """Check |matching cover| <= 2 * OPT on random graphs."""
    for trial in range(num_trials):
        g = generate_graph(n, p, seed=seed + trial)
        approx = len(vertex_cover_matching(g))
        opt = brute_force_min_vertex_cover(g)
        if approx > 2 * opt:
            return False
    return True


if __name__ == "__main__":
    # Path 0-1-2-3: OPT = 2 (cover {1,2}); matching cover has size 4 <= 2*2.
    g = (4, [(0, 1), (1, 2), (2, 3)])
    assert brute_force_min_vertex_cover(g) == 2
    assert len(vertex_cover_matching(g)) <= 2 * 2

    # Triangle: OPT = 2.
    tri = (3, [(0, 1), (0, 2), (1, 2)])
    assert brute_force_min_vertex_cover(tri) == 2

    # Empty graph: OPT = 0.
    assert brute_force_min_vertex_cover((5, [])) == 0

    # Random verification across many small graphs.
    assert verify_vc_2approx(num_trials=40, n=10, p=0.3, seed=1) is True
    assert verify_vc_2approx(num_trials=20, n=12, p=0.5, seed=100) is True

    print("All tests passed!")
