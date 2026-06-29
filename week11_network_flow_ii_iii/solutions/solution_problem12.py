"""
Problem 12 - Matching <= Vertex Cover, with Equality in Bipartite Graphs (SOLUTION)
===================================================================================
"""

import os
import sys
from itertools import combinations
from typing import Hashable, List, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem02 import kuhn_matching
from solution_problem05 import min_vertex_cover, is_vertex_cover
from starter_code import generate_bipartite_graph, generate_random_graph

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def brute_force_max_matching(vertices: List[Vertex], edges: List[Edge]) -> int:
    """Largest set of edges with no shared endpoint (any graph), by brute force."""
    best = 0
    m = len(edges)
    # Try matchings from largest size downward.
    for size in range(m, 0, -1):
        for combo in combinations(edges, size):
            used: Set[Vertex] = set()
            ok = True
            for u, v in combo:
                if u in used or v in used:
                    ok = False
                    break
                used.add(u)
                used.add(v)
            if ok:
                return size
    return best


def brute_force_min_vertex_cover(vertices: List[Vertex], edges: List[Edge]) -> int:
    """Smallest vertex set covering every edge (any graph), by brute force."""
    n = len(vertices)
    for size in range(0, n + 1):
        for combo in combinations(vertices, size):
            cover = set(combo)
            if all((u in cover) or (v in cover) for u, v in edges):
                return size
    return n


def verify_matching_cover_relationship(num_trials: int = 40, seed: int = 0) -> bool:
    """Check the two theorems on random graphs.

    1. (Any graph) max matching <= min vertex cover -- every matched edge needs
       a distinct cover vertex.
    2. (Bipartite, Konig) max matching == min vertex cover, and our constructive
       cover from Problem 5 attains it.
    """
    import random

    rng = random.Random(seed)
    for trial in range(num_trials):
        # --- General graph: weak duality matching <= cover ---
        n = rng.randint(2, 6)
        verts, gedges = generate_random_graph(n, p=0.4, seed=seed + trial)
        mm = brute_force_max_matching(verts, gedges)
        mc = brute_force_min_vertex_cover(verts, gedges)
        if not (mm <= mc):
            return False

        # --- Bipartite graph: Konig equality ---
        left, right, bedges = generate_bipartite_graph(4, 4, p=0.45, seed=seed + 1000 + trial)
        all_verts = left + right
        bmm = brute_force_max_matching(all_verts, bedges)
        bmc = brute_force_min_vertex_cover(all_verts, bedges)
        if bmm != bmc:
            return False
        # Constructive Konig cover from Problem 5 must equal max matching size.
        kuhn = kuhn_matching(left, right, bedges)
        cover = min_vertex_cover(left, right, bedges)
        if len(cover) != len(kuhn):
            return False
        if not is_vertex_cover(bedges, cover):
            return False
        if len(kuhn) != bmm:
            return False
    return True


if __name__ == "__main__":
    assert verify_matching_cover_relationship(num_trials=40, seed=0) is True
    assert verify_matching_cover_relationship(num_trials=25, seed=500) is True

    # A triangle (NON-bipartite) shows strict inequality: matching 1, cover 2.
    tri_v = [0, 1, 2]
    tri_e = [(0, 1), (1, 2), (2, 0)]
    assert brute_force_max_matching(tri_v, tri_e) == 1
    assert brute_force_min_vertex_cover(tri_v, tri_e) == 2

    print("All tests passed!")
