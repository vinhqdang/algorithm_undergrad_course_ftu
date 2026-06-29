"""
Problem 03 - Dijkstra with Predecessors and Path Reconstruction
================================================================

Extend Dijkstra to record a predecessor array, then reconstruct the actual
shortest path from a source to a target. See practical_exercises.pdf, Problem 3.
"""

import heapq  # noqa: F401  (you will need this)
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
    # TODO: implement this function.
    raise NotImplementedError


def reconstruct_path(
    pred: Dict[Hashable, Optional[Hashable]], source: Hashable, target: Hashable
) -> Optional[List[Hashable]]:
    """Reconstruct the shortest path source -> target from ``pred``.

    Returns ``[source, ..., target]``, or ``None`` if ``target`` is unreachable.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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

        g2: Graph = {}
        add_edge(g2, 0, 1, 1)
        g2.setdefault(9, {})
        _, pred2 = dijkstra_with_pred(g2, 0)
        assert reconstruct_path(pred2, 0, 9) is None

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
