"""
Problem 09 - Bipartite Matching via Max Flow
==============================================

Implement ``max_bipartite_matching(left, right, edges)``: compute the size of a
maximum-cardinality matching in a bipartite graph, by REDUCING to max flow.

Reduction: add a super-source s with a unit-capacity edge to each left vertex,
a unit-capacity edge for each allowed pair (left u -> right v), and a
unit-capacity edge from each right vertex to a super-sink t. The max-flow value
equals the maximum matching size (and by integrality the flow selects matching
edges). Return that integer.

To keep the two sides distinct, label left vertices ``("L", u)`` and right
vertices ``("R", v)`` in your flow network.

See practical_exercises.pdf, Problem 9, for the full statement and examples.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork, generate_bipartite_graph

# from starter_code_problem05 import edmonds_karp


def max_bipartite_matching(left: int, right: int, edges: List[Tuple[int, int]]) -> int:
    """Maximum bipartite matching size, computed via max flow."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert max_bipartite_matching(3, 3, [(0, 0), (1, 1), (2, 2)]) == 3
        assert max_bipartite_matching(3, 3, [(0, 0), (1, 0), (2, 0)]) == 1
        assert max_bipartite_matching(2, 2, [(0, 0), (0, 1), (1, 0)]) == 2
        assert max_bipartite_matching(3, 3, []) == 0
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
