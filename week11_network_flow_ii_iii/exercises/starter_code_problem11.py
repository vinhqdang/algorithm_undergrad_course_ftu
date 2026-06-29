"""
Problem 11 - Circulation with Demands: Feasibility Check
========================================================

Implement `circulation_feasible(vertices, demands, edges)`: decide whether a
feasible circulation with demands and lower bounds exists.

Each vertex v has a demand d_v: d_v > 0 means v must absorb d_v units (a sink),
d_v < 0 means v supplies -d_v units (a source). Each edge (u, v, lower, upper)
must carry flow in [lower, upper].

Reduction (Kleinberg-Tardos Section 7.7):
  1. Eliminate lower bounds: for edge (u, v, L, U), reduce capacity to U - L and
     set d_u += L, d_v -= L.
  2. Add super-source S and super-sink T. For each v with adjusted demand < 0:
     S -> v with capacity -d_v. For each v with adjusted demand > 0:
     v -> T with capacity d_v.
  3. A feasible circulation exists iff (adjusted total supply == adjusted total
     demand) AND the max S-T flow saturates all super-source edges.

Use the `MaxFlow` helper from starter_code.py.

See practical_exercises.pdf, Problem 11, for the full statement and examples.
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import MaxFlow

Vertex = Hashable
DemandEdge = Tuple[Vertex, Vertex, float, float]  # (u, v, lower, upper)


def circulation_feasible(
    vertices: List[Vertex],
    demands: Dict[Vertex, float],
    edges: List[DemandEdge],
) -> bool:
    """Decide whether a feasible circulation with demands and lower bounds exists."""
    # TODO: implement this function using MaxFlow.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert circulation_feasible(["a", "b"], {"a": -3, "b": 3}, [("a", "b", 0, 5)]) is True
        assert circulation_feasible(["a", "b"], {"a": -3, "b": 3}, [("a", "b", 0, 2)]) is False
        assert circulation_feasible(["a", "b"], {"a": -1, "b": 1}, [("a", "b", 5, 10)]) is False
        assert circulation_feasible(["a", "b"], {"a": -3, "b": 2}, [("a", "b", 0, 10)]) is False

        V = ["a", "b", "c"]
        D = {"a": -4, "b": 0, "c": 4}
        E = [("a", "b", 0, 4), ("b", "c", 0, 4), ("a", "c", 0, 4)]
        assert circulation_feasible(V, D, E) is True

        assert circulation_feasible(["a", "b"], {}, [("a", "b", 0, 3)]) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
