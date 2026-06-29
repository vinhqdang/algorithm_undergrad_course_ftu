"""
Problem 08 - Metric TSP 2-Approximation via MST Preorder (SOLUTION)
===================================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import distance_matrix, euclidean, generate_points  # noqa: E402

Point = Tuple[float, float]


def _prim_mst(dist: List[List[float]]) -> Tuple[List[List[int]], float]:
    """Build an MST with Prim's algorithm; return (adjacency_children, total_weight).

    adjacency is rooted at vertex 0: adjacency[u] lists the children of u in the
    MST tree (so a DFS preorder from 0 visits every vertex).
    """
    n = len(dist)
    if n == 0:
        return [], 0.0
    in_tree = [False] * n
    parent = [-1] * n
    best = [float("inf")] * n
    best[0] = 0.0
    total = 0.0
    for _ in range(n):
        u = min((v for v in range(n) if not in_tree[v]), key=lambda v: best[v])
        in_tree[u] = True
        total += best[u]
        for v in range(n):
            if not in_tree[v] and dist[u][v] < best[v]:
                best[v] = dist[u][v]
                parent[v] = u
    children: List[List[int]] = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)
    return children, total


def _preorder(children: List[List[int]], root: int = 0) -> List[int]:
    order: List[int] = []
    stack = [root]
    while stack:
        u = stack.pop()
        order.append(u)
        # Push children in reverse so they are visited in ascending order.
        for c in reversed(children[u]):
            stack.append(c)
    return order


def mst_weight(points: List[Point]) -> float:
    """Weight of the Euclidean MST of `points`."""
    dist = distance_matrix(points)
    _, total = _prim_mst(dist)
    return total


def mst_tsp_tour(points: List[Point]) -> Tuple[List[int], float]:
    """Return (tour, tour_length): MST preorder visiting order and closed-tour length."""
    n = len(points)
    if n == 0:
        return [], 0.0
    if n == 1:
        return [0], 0.0
    dist = distance_matrix(points)
    children, _ = _prim_mst(dist)
    tour = _preorder(children, 0)
    length = 0.0
    for i in range(len(tour)):
        a = tour[i]
        b = tour[(i + 1) % len(tour)]
        length += dist[a][b]
    return tour, length


def verify_tsp_2approx(num_trials: int, n: int, seed: int) -> bool:
    """Check tour_length <= 2 * w(MST) on random point sets."""
    for trial in range(num_trials):
        points = generate_points(n, seed=seed + trial)
        _, length = mst_tsp_tour(points)
        w = mst_weight(points)
        if length > 2 * w + 1e-9:
            return False
    return True


if __name__ == "__main__":
    # Unit square corners: optimal tour length 4; MST-based tour is a valid tour.
    square = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)]
    tour, length = mst_tsp_tour(square)
    assert sorted(tour) == [0, 1, 2, 3]  # visits every city exactly once
    w = mst_weight(square)
    assert length <= 2 * w + 1e-9

    # Collinear points.
    line = [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0), (3.0, 0.0)]
    tour, length = mst_tsp_tour(line)
    assert sorted(tour) == [0, 1, 2, 3]
    assert length <= 2 * mst_weight(line) + 1e-9

    # Random verification of the 2-approximation bound.
    assert verify_tsp_2approx(num_trials=50, n=12, seed=1) is True
    assert verify_tsp_2approx(num_trials=30, n=20, seed=99) is True

    print("All tests passed!")
