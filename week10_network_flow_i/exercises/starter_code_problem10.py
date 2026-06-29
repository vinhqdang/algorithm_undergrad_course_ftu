"""
Problem 10 - Multiple Sources/Sinks via Super-Source/Super-Sink
================================================================

Implement ``multi_source_sink_max_flow(nodes, edges, sources, sinks)``:
compute the maximum total flow from several sources to several sinks.

Reduction: introduce a super-source S* with an infinite-capacity edge to every
original source, and a super-sink T* fed by an infinite-capacity edge from
every original sink. The max flow from S* to T* equals the maximum total flow
the sources can deliver to the sinks. Each edge is a tuple ``(u, v, capacity)``.
Return the value.

See practical_exercises.pdf, Problem 10, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

# from starter_code_problem05 import edmonds_karp

Node = Hashable
Edge = Tuple[Node, Node, float]


def multi_source_sink_max_flow(
    nodes: List[Node],
    edges: List[Edge],
    sources: List[Node],
    sinks: List[Node],
) -> float:
    """Max flow with multiple sources and sinks via the super-source/super-sink
    reduction."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        nodes = [0, 1, 2, 3]
        edges = [(0, 2, 3), (1, 2, 2), (2, 3, 10)]
        assert multi_source_sink_max_flow(nodes, edges, [0, 1], [3]) == 5.0

        edges_bottleneck = [(0, 2, 3), (1, 2, 2), (2, 3, 4)]
        assert multi_source_sink_max_flow(nodes, edges_bottleneck, [0, 1], [3]) == 4.0

        nodes2 = [0, 1, 2, 3, 4, 5]
        edges2 = [(0, 2, 3), (1, 2, 3), (2, 3, 5), (3, 4, 2), (3, 5, 2)]
        assert multi_source_sink_max_flow(nodes2, edges2, [0, 1], [4, 5]) == 4.0

        nodes3 = [0, 1, 2]
        edges3 = [(0, 1, 7), (1, 2, 7)]
        assert multi_source_sink_max_flow(nodes3, edges3, [0], [2]) == 7.0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
