"""
Problem 10 - DAG Shortest Path via Topological Order (SOLUTION)
================================================================
"""

import os
import sys
from collections import deque
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import INF, generate_dag

from solution_problem06 import bellman_ford

Edge = Tuple[int, int, float]


def topological_order(n: int, edges: List[Edge]) -> List[int]:
    """Return a topological order of the DAG via Kahn's algorithm."""
    indeg = [0] * n
    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v, _ in edges:
        adj[u].append(v)
        indeg[v] += 1
    queue = deque(v for v in range(n) if indeg[v] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    if len(order) != n:
        raise ValueError("graph is not a DAG (cycle detected)")
    return order


def dag_shortest_path(n: int, edges: List[Edge], source: int) -> List[float]:
    """Shortest-path distances in a DAG by relaxing edges in topological order."""
    out: List[List[Tuple[int, float]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        out[u].append((v, w))
    dist = [INF] * n
    dist[source] = 0.0
    for u in topological_order(n, edges):
        if dist[u] == INF:
            continue
        for v, w in out[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


def verify_dag_matches_bellman_ford(num_trials: int, n: int, m: int, seed: int) -> bool:
    """On random DAGs, the linear-time sweep must match general Bellman-Ford."""
    for trial in range(num_trials):
        _, edges = generate_dag(n, m, seed=seed + trial)
        if dag_shortest_path(n, edges, 0) != bellman_ford(n, edges, 0):
            return False
    return True


if __name__ == "__main__":
    # Simple chain with a negative edge (Dijkstra would need care; DAG sweep is trivial)
    edges = [(0, 1, 1), (1, 2, -2), (0, 2, 4)]
    assert dag_shortest_path(3, edges, 0) == [0, 1, -1]

    # Diamond
    edges = [(0, 1, 2), (0, 2, 5), (1, 3, 3), (2, 3, -1)]
    assert dag_shortest_path(4, edges, 0) == [0, 2, 5, 4]

    assert verify_dag_matches_bellman_ford(num_trials=50, n=8, m=15, seed=1) is True
    assert verify_dag_matches_bellman_ford(num_trials=30, n=12, m=30, seed=777) is True

    print("All tests passed!")
