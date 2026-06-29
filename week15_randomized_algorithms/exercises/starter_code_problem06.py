"""
Problem 06 - Karger's Contraction Min-Cut, Single Run
======================================================

Implement `karger_min_cut(graph, seed)` performing ONE run of Karger's
contraction: repeatedly contract a uniformly random edge (merging endpoints,
keeping parallel edges, dropping self-loops) until two super-vertices remain;
return the number of edges between them (the cut size of this run).

`graph` is (vertices, edges) with edges a list of (u, v) tuples.

See practical_exercises.pdf, Problem 6.
"""

import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions")
)


def karger_min_cut(graph, seed: int) -> int:
    """One run of Karger's contraction; return the resulting cut size."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        from starter_code import generate_graph
        from solution_problem07 import brute_force_min_cut

        for trial in range(40):
            g = generate_graph(7, seed=400 + trial, p=0.4)
            true_min = brute_force_min_cut(g)
            run = karger_min_cut(g, seed=trial)
            assert run >= true_min, (trial, run, true_min)
            assert run >= 1

        g = generate_graph(8, seed=99, p=0.3)
        results = {karger_min_cut(g, seed=s) for s in range(30)}
        assert len(results) >= 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
