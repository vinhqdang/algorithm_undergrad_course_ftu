"""
Problem 04 - Hall's Condition Checker (SOLUTION)
==================================================
"""

import os
import sys
from itertools import combinations
from typing import Dict, Hashable, List, Optional, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem02 import kuhn_matching

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def neighbors_of(subset: Set[Vertex], adj: Dict[Vertex, Set[Vertex]]) -> Set[Vertex]:
    """Union of neighbourhoods N(subset) of a set of left vertices."""
    result: Set[Vertex] = set()
    for u in subset:
        result |= adj.get(u, set())
    return result


def hall_violator(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> Optional[Set[Vertex]]:
    """Decide whether the LEFT side has a perfect matching (all left matched).

    Returns None if a left-saturating matching exists; otherwise returns a
    "deficient" subset S of left vertices with |N(S)| < |S|, witnessing the
    failure of Hall's condition.

    The deficient set is recovered from a maximum matching: by Konig/Hall
    theory, if not all of LEFT is matched, the set of left vertices reachable
    by alternating paths from an unmatched left vertex is deficient. We use a
    direct, robust construction here.
    """
    adj: Dict[Vertex, Set[Vertex]] = {u: set() for u in left}
    for u, v in edges:
        adj[u].add(v)

    match_right = kuhn_matching(left, right, edges)  # right -> left
    matched_left = set(match_right.values())

    if len(matched_left) == len(left):
        return None  # Hall's condition holds: perfect matching of LEFT exists.

    # Find an unmatched left vertex and grow the set of left vertices reachable
    # by alternating paths (free left -> edge -> matched right -> match -> left).
    match_left: Dict[Vertex, Vertex] = {u: v for v, u in match_right.items()}
    free_left = [u for u in left if u not in matched_left]

    reachable_left: Set[Vertex] = set()
    reachable_right: Set[Vertex] = set()
    stack = list(free_left)
    reachable_left.update(free_left)
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w in reachable_right:
                continue
            reachable_right.add(w)
            # Follow the matching edge back to a left vertex (if any).
            if w in match_right:
                nxt = match_right[w]
                if nxt not in reachable_left:
                    reachable_left.add(nxt)
                    stack.append(nxt)

    # S = reachable left vertices; N(S) = reachable right vertices.
    S = reachable_left
    assert len(neighbors_of(S, adj)) < len(S), (len(neighbors_of(S, adj)), len(S))
    return S


if __name__ == "__main__":
    # Perfect matching exists: identity 3x3.
    left = [("L", i) for i in range(3)]
    right = [("R", j) for j in range(3)]
    edges = [(("L", i), ("R", i)) for i in range(3)]
    assert hall_violator(left, right, edges) is None

    # Two left vertices share a single right neighbour -> deficient set of size 2.
    left2 = [("L", 0), ("L", 1)]
    right2 = [("R", 0)]
    edges2 = [(("L", 0), ("R", 0)), (("L", 1), ("R", 0))]
    S = hall_violator(left2, right2, edges2)
    assert S is not None
    adj2 = {("L", 0): {("R", 0)}, ("L", 1): {("R", 0)}}
    assert len(neighbors_of(S, adj2)) < len(S)

    # A left vertex with no neighbours is deficient by itself.
    left3 = [("L", 0), ("L", 1)]
    right3 = [("R", 0)]
    edges3 = [(("L", 0), ("R", 0))]
    S3 = hall_violator(left3, right3, edges3)
    assert S3 is not None and ("L", 1) in S3

    # Brute-force cross-check on random small graphs: hall_violator returns None
    # iff NO subset S of left violates |N(S)| < |S|.
    from starter_code import generate_bipartite_graph

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
