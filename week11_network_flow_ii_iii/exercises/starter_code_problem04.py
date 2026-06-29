"""
Problem 04 - Hall's Condition Checker
======================================

Implement `hall_violator(left, right, edges)`: decide whether the LEFT side has
a matching saturating ALL of its vertices (a "perfect matching of one side").

Return None if such a matching exists. Otherwise return a "deficient" subset S
of left vertices with |N(S)| < |S| -- a witness that Hall's condition fails.

Recommended approach: compute a maximum matching (e.g. via kuhn_matching from
Problem 2), and if not all left vertices are matched, recover the deficient set
from the set of left vertices reachable by alternating paths from an unmatched
left vertex.

Also implement `neighbors_of(subset, adj)` returning the union of neighbourhoods.

See practical_exercises.pdf, Problem 4, for the full statement and examples.
"""

import os
import sys
from itertools import combinations
from typing import Dict, Hashable, List, Optional, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem02 import kuhn_matching
from starter_code import generate_bipartite_graph

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def neighbors_of(subset: Set[Vertex], adj: Dict[Vertex, Set[Vertex]]) -> Set[Vertex]:
    """Union of neighbourhoods N(subset) of a set of left vertices."""
    # TODO: implement this function.
    raise NotImplementedError


def hall_violator(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> Optional[Set[Vertex]]:
    """Return None if LEFT has a perfect matching, else a deficient subset S."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        left = [("L", i) for i in range(3)]
        right = [("R", j) for j in range(3)]
        edges = [(("L", i), ("R", i)) for i in range(3)]
        assert hall_violator(left, right, edges) is None

        left2 = [("L", 0), ("L", 1)]
        right2 = [("R", 0)]
        edges2 = [(("L", 0), ("R", 0)), (("L", 1), ("R", 0))]
        S = hall_violator(left2, right2, edges2)
        assert S is not None
        adj2 = {("L", 0): {("R", 0)}, ("L", 1): {("R", 0)}}
        assert len(neighbors_of(S, adj2)) < len(S)

        left3 = [("L", 0), ("L", 1)]
        right3 = [("R", 0)]
        edges3 = [(("L", 0), ("R", 0))]
        S3 = hall_violator(left3, right3, edges3)
        assert S3 is not None and ("L", 1) in S3

        for seed in range(60):
            L, R, E = generate_bipartite_graph(4, 4, p=0.45, seed=seed)
            adj = {u: set() for u in L}
            for u, v in E:
                adj[u].add(v)
            brute_violation = False
            for r in range(1, len(L) + 1):
                for sub in combinations(L, r):
                    if len(neighbors_of(set(sub), adj)) < len(sub):
                        brute_violation = True
                        break
                if brute_violation:
                    break
            result = hall_violator(L, R, E)
            assert (result is None) == (not brute_violation), seed
            if result is not None:
                assert len(neighbors_of(result, adj)) < len(result)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
