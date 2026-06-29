"""
Problem 03 - Dijkstra with Predecessors and Path Reconstruction (SOLUTION)
==========================================================================
"""

import heapq
import os
import sys
from typing import Dict, Hashable, List, Optional, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import Graph, add_edge  # noqa: E402


def dijkstra_with_pred(
    graph: Graph, source: Hashable
) -> Tuple[Dict[Hashable, float], Dict[Hashable, Optional[Hashable]]]:
    """Run Dijkstra from ``source``; return ``(dist, pred)``.

    ``pred[v]`` is the vertex preceding ``v`` on a shortest path from
    ``source`` (``None`` for the source and for unreachable vertices).
    """
    dist: Dict[Hashable, float] = {v: float("inf") for v in graph}
    pred: Dict[Hashable, Optional[Hashable]] = {v: None for v in graph}
    dist[source] = 0.0
    heap = [(0.0, source)]
    visited = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                pred[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, pred


def reconstruct_path(
    pred: Dict[Hashable, Optional[Hashable]], source: Hashable, target: Hashable
) -> Optional[List[Hashable]]:
    """Reconstruct the shortest path source -> target from ``pred``.

    Returns the list of vertices ``[source, ..., target]``, or ``None`` if
    ``target`` is unreachable from ``source``.
    """
    if target != source and pred.get(target) is None:
        return None
    path: List[Hashable] = []
    cur: Optional[Hashable] = target
    while cur is not None:
        path.append(cur)
        if cur == source:
            break
        cur = pred[cur]
    path.reverse()
    if path[0] != source:
        return None
    return path


if __name__ == "__main__":
    g: Graph = {}
    add_edge(g, 0, 1, 4)
    add_edge(g, 0, 2, 1)
    add_edge(g, 2, 1, 2)
    add_edge(g, 1, 3, 1)
    add_edge(g, 2, 3, 5)

    dist, pred = dijkstra_with_pred(g, 0)
    assert dist[3] == 4.0
    assert reconstruct_path(pred, 0, 3) == [0, 2, 1, 3]
    assert reconstruct_path(pred, 0, 0) == [0]

    # Unreachable target.
    g2: Graph = {}
    add_edge(g2, 0, 1, 1)
    g2.setdefault(9, {})
    _, pred2 = dijkstra_with_pred(g2, 0)
    assert reconstruct_path(pred2, 0, 9) is None

    print("All tests passed!")
