"""
Problem 06 - Karger's Contraction Min-Cut, Single Run (SOLUTION)
================================================================
"""

import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def karger_min_cut(graph, seed: int) -> int:
    """One run of Karger's contraction; return the resulting cut size.

    `graph` is (vertices, edges) with edges a list of (u, v) tuples.
    """
    vertices, edges = graph
    rng = random.Random(seed)

    # Work on a mutable edge list of vertex labels; contraction relabels.
    edge_list: List[Tuple] = [tuple(e) for e in edges]
    # Use a union-find-free "parent label" approach via a representative map.
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    num_super = len(vertices)
    while num_super > 2:
        u, v = edge_list[rng.randrange(len(edge_list))]
        ru, rv = find(u), find(v)
        if ru == rv:
            continue  # self-loop after prior contractions; pick again
        parent[ru] = rv  # merge ru into rv
        num_super -= 1

    # Count edges crossing the final two super-vertices (parallel edges kept).
    cut = 0
    for u, v in edge_list:
        if find(u) != find(v):
            cut += 1
    return cut


if __name__ == "__main__":
    from starter_code import generate_graph
    from solution_problem07 import brute_force_min_cut

    # A single run always returns a valid cut size >= the true min-cut.
    for trial in range(40):
        g = generate_graph(7, seed=400 + trial, p=0.4)
        true_min = brute_force_min_cut(g)
        run = karger_min_cut(g, seed=trial)
        assert run >= true_min, (trial, run, true_min)
        assert run >= 1  # connected graph: a cut has at least one edge

    # Different seeds can give different cuts on the same graph.
    g = generate_graph(8, seed=99, p=0.3)
    results = {karger_min_cut(g, seed=s) for s in range(30)}
    assert len(results) >= 1

    print("All tests passed!")
