"""
Problem 10 - DAG Shortest Path via Topological Order
=====================================================

Implement `dag_shortest_path(n, edges, source)` for a directed ACYCLIC graph:
compute a topological order (e.g. Kahn's algorithm), then relax edges once in
that order, returning the `dist` list. Then implement
`verify_dag_matches_bellman_ford(num_trials, n, m, seed)` that, on random DAGs
(via generate_dag), checks the linear-time DAG sweep produces the same distances
as the general Bellman-Ford (imported from the Problem 6 starter).

See practical_exercises.pdf, Problem 10, for the full statement and examples.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from starter_code import generate_dag

from starter_code_problem06 import bellman_ford

Edge = Tuple[int, int, float]


def dag_shortest_path(n: int, edges: List[Edge], source: int) -> List[float]:
    """Shortest-path distances in a DAG by relaxing edges in topological order."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_dag_matches_bellman_ford(num_trials: int, n: int, m: int, seed: int) -> bool:
    """On random DAGs, the linear-time sweep must match general Bellman-Ford."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        edges = [(0, 1, 1), (1, 2, -2), (0, 2, 4)]
        assert dag_shortest_path(3, edges, 0) == [0, 1, -1]

        edges = [(0, 1, 2), (0, 2, 5), (1, 3, 3), (2, 3, -1)]
        assert dag_shortest_path(4, edges, 0) == [0, 2, 5, 4]

        assert verify_dag_matches_bellman_ford(num_trials=50, n=8, m=15, seed=1) is True
        assert verify_dag_matches_bellman_ford(num_trials=30, n=12, m=30, seed=777) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
