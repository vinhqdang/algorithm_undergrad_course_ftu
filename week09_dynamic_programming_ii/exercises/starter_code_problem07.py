"""
Problem 07 - Bellman-Ford Negative-Cycle Detection
===================================================

Implement `find_negative_cycle(n, edges)` returning None if the graph has no
negative cycle, or otherwise a list of vertices [c0, c1, ..., c0] describing one
negative cycle (start and end vertex repeated). Initialise all distances to 0 so
every vertex is a potential source, relax all edges n times, and if some edge
still relaxes on the n-th pass, follow parent pointers n times to land inside the
cycle, then walk it out.

See practical_exercises.pdf, Problem 7, for the full statement and examples.
"""

from typing import List, Optional, Tuple

Edge = Tuple[int, int, float]


def find_negative_cycle(n: int, edges: List[Edge]) -> Optional[List[int]]:
    """Return a negative cycle [c0, ..., c0] if one exists, else None."""
    # TODO: implement this function.
    raise NotImplementedError


def _cycle_weight(edges: List[Edge], cycle: List[int]) -> float:
    weight = {}
    for u, v, w in edges:
        if (u, v) not in weight or w < weight[(u, v)]:
            weight[(u, v)] = w
    total = 0.0
    for a, b in zip(cycle, cycle[1:]):
        total += weight[(a, b)]
    return total


if __name__ == "__main__":
    try:
        cyc = find_negative_cycle(2, [(0, 1, 1), (1, 0, -3)])
        assert cyc is not None
        assert cyc[0] == cyc[-1]
        assert _cycle_weight([(0, 1, 1), (1, 0, -3)], cyc) < 0

        assert find_negative_cycle(3, [(0, 1, 4), (0, 2, 5), (1, 2, -3)]) is None

        edges = [(0, 1, 1), (1, 2, -3), (2, 0, 1)]
        cyc = find_negative_cycle(3, edges)
        assert cyc is not None and cyc[0] == cyc[-1]
        assert _cycle_weight(edges, cyc) < 0
        edge_set = {(u, v) for u, v, _ in edges}
        assert all((a, b) in edge_set for a, b in zip(cyc, cyc[1:]))

        assert find_negative_cycle(3, [(0, 1, 1), (1, 2, 1), (2, 0, 1)]) is None

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
