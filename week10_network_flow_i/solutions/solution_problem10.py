"""
Problem 10 - Multiple Sources/Sinks via Super-Source/Super-Sink (SOLUTION)
===========================================================================
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem05 import edmonds_karp
from starter_code import FlowNetwork

Node = Hashable
Edge = Tuple[Node, Node, float]  # (u, v, capacity)


def multi_source_sink_max_flow(
    nodes: List[Node],
    edges: List[Edge],
    sources: List[Node],
    sinks: List[Node],
) -> float:
    """Max flow with multiple sources and sinks, via the standard reduction.

    Introduce a *super-source* S* connected to every original source with an
    infinite-capacity edge, and a *super-sink* T* fed by every original sink
    with an infinite-capacity edge. The max flow from S* to T* in this enlarged
    network equals the maximum total flow that the multiple sources can deliver
    to the multiple sinks. Returns that value.
    """
    SUPER_SOURCE = "__S*__"
    SUPER_SINK = "__T*__"
    INF = float("inf")

    g = FlowNetwork(source=SUPER_SOURCE, sink=SUPER_SINK)
    for u in nodes:
        g.add_node(u)
    for (u, v, cap) in edges:
        g.add_edge(u, v, cap)
    for src in sources:
        g.add_edge(SUPER_SOURCE, src, INF)
    for snk in sinks:
        g.add_edge(snk, SUPER_SINK, INF)

    return edmonds_karp(g)


if __name__ == "__main__":
    # Two sources {0, 1}, one sink {3}. Capacities limit total to 3 + 2 = 5
    # into the sink: edges 0->2 (3), 1->2 (2), 2->3 (10).
    nodes = [0, 1, 2, 3]
    edges = [(0, 2, 3), (1, 2, 2), (2, 3, 10)]
    assert multi_source_sink_max_flow(nodes, edges, sources=[0, 1], sinks=[3]) == 5.0

    # The shared edge 2->3 now bottlenecks at 4.
    edges_bottleneck = [(0, 2, 3), (1, 2, 2), (2, 3, 4)]
    assert multi_source_sink_max_flow(nodes, edges_bottleneck, [0, 1], [3]) == 4.0

    # Two sources and two sinks.
    nodes2 = [0, 1, 2, 3, 4, 5]
    edges2 = [
        (0, 2, 3), (1, 2, 3),    # sources 0,1 feed node 2
        (2, 3, 5),               # node 2 -> node 3
        (3, 4, 2), (3, 5, 2),    # node 3 splits to sinks 4,5
    ]
    # Total deliverable to sinks {4,5} is 2 + 2 = 4.
    assert multi_source_sink_max_flow(nodes2, edges2, sources=[0, 1], sinks=[4, 5]) == 4.0

    # Single source/sink should match a plain max-flow computation.
    nodes3 = [0, 1, 2]
    edges3 = [(0, 1, 7), (1, 2, 7)]
    assert multi_source_sink_max_flow(nodes3, edges3, sources=[0], sinks=[2]) == 7.0

    print("All tests passed!")
