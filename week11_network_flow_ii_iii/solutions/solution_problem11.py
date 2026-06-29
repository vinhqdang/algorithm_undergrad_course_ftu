"""
Problem 11 - Circulation with Demands: Feasibility Check (SOLUTION)
===================================================================
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import MaxFlow

Vertex = Hashable
# An edge with a lower bound: (u, v, lower, upper)
DemandEdge = Tuple[Vertex, Vertex, float, float]


def circulation_feasible(
    vertices: List[Vertex],
    demands: Dict[Vertex, float],
    edges: List[DemandEdge],
) -> bool:
    """Decide whether a feasible circulation with demands and lower bounds exists.

    Each vertex v has a demand d_v: d_v > 0 means v is a sink that must absorb
    d_v units; d_v < 0 means a source supplying -d_v units. Each edge carries
    flow in [lower, upper].

    Reduction (Kleinberg-Tardos Section 7.7):
      1. Eliminate lower bounds: for an edge (u, v, L, U), force L units through
         it by reducing capacity to U - L and adjusting demands:
         d_u += L  (u must send L extra), d_v -= L  (v receives L extra).
      2. Add a super-source S and super-sink T. For each vertex v with adjusted
         demand d_v < 0 (supply): edge S -> v with capacity -d_v.
         For each v with d_v > 0 (demand): edge v -> T with capacity d_v.
      3. A feasible circulation exists iff the max S-T flow saturates all
         super-source edges (equivalently equals the total positive demand).
    """
    adj_demand: Dict[Vertex, float] = {v: demands.get(v, 0.0) for v in vertices}

    mf = MaxFlow()
    S, T = "__super_source__", "__super_sink__"

    for u, v, low, up in edges:
        if up - low < -1e-9:
            return False  # impossible edge bounds
        mf.add_edge(u, v, up - low)
        adj_demand[u] = adj_demand.get(u, 0.0) + low
        adj_demand[v] = adj_demand.get(v, 0.0) - low

    total_demand = 0.0
    total_supply = 0.0
    for v in vertices:
        dv = adj_demand.get(v, 0.0)
        if dv < 0:  # net supply
            mf.add_edge(S, v, -dv)
            total_supply += -dv
        elif dv > 0:  # net demand
            mf.add_edge(v, T, dv)
            total_demand += dv

    # Necessary condition: total adjusted supply must equal total adjusted demand,
    # otherwise no circulation can conserve flow at every vertex.
    if abs(total_demand - total_supply) > 1e-6:
        return False

    flow_value = mf.max_flow(S, T)
    return abs(flow_value - total_demand) < 1e-6


if __name__ == "__main__":
    # Feasible: source a (-3) -> sink b (+3) with an edge of capacity >= 3.
    assert circulation_feasible(
        ["a", "b"], {"a": -3, "b": 3}, [("a", "b", 0, 5)]
    ) is True

    # Infeasible: edge capacity too small to meet the demand.
    assert circulation_feasible(
        ["a", "b"], {"a": -3, "b": 3}, [("a", "b", 0, 2)]
    ) is False

    # Lower bound forces flow that the sink cannot absorb -> infeasible.
    # a supplies 1, but edge lower bound forces 5 through, b can only absorb 1.
    assert circulation_feasible(
        ["a", "b"], {"a": -1, "b": 1}, [("a", "b", 5, 10)]
    ) is False

    # Demands don't balance -> automatically infeasible (supply != demand).
    assert circulation_feasible(
        ["a", "b"], {"a": -3, "b": 2}, [("a", "b", 0, 10)]
    ) is False

    # Triangle circulation, feasible routing.
    V = ["a", "b", "c"]
    D = {"a": -4, "b": 0, "c": 4}
    E = [("a", "b", 0, 4), ("b", "c", 0, 4), ("a", "c", 0, 4)]
    assert circulation_feasible(V, D, E) is True

    # No demands at all: trivially feasible (zero circulation works).
    assert circulation_feasible(["a", "b"], {}, [("a", "b", 0, 3)]) is True

    print("All tests passed!")
