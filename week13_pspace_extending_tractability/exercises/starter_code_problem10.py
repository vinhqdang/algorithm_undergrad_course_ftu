"""
Problem 10 - 2-SAT in Polynomial Time (Implication Graph + SCC)
===============================================================

Implement `two_sat(num_vars, clauses)` returning a satisfying assignment
``{var: bool}`` or None if the 2-CNF formula is unsatisfiable.

Build the implication graph: each clause (a OR b) yields (NOT a -> b) and
(NOT b -> a). Represent each literal as a node (a helper `_node` is suggested:
node 2*(v-1) = "v true", node 2*(v-1)+1 = "v false"). Compute strongly
connected components (Kosaraju or Tarjan). The formula is satisfiable iff for
no variable v do "v true" and "v false" share an SCC. Read off the assignment
from SCC ordering (set v True iff its "true" literal's component comes later in
the reverse-topological order).

The helper `cnf_is_satisfied` in starter_code.py checks an assignment.

See practical_exercises.pdf, Problem 10.
"""

import os
import sys
from typing import Dict, List, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cnf_is_satisfied, generate_2sat  # noqa: E402


def two_sat(num_vars: int, clauses: List[List[int]]) -> Optional[Dict[int, bool]]:
    """Return a satisfying assignment {var: bool}, or None if unsatisfiable."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        import itertools

        clauses = [[1, 2], [-1, 2], [-2, 3]]
        asg = two_sat(3, clauses)
        assert asg is not None and cnf_is_satisfied(clauses, asg)

        assert two_sat(1, [[1, 1], [-1, -1]]) is None
        assert two_sat(2, [[1, 2], [1, -2], [-1, 2], [-1, -2]]) is None

        def brute_force_sat(num_vars, cls):
            for bits in itertools.product([False, True], repeat=num_vars):
                a = {i + 1: bits[i] for i in range(num_vars)}
                if cnf_is_satisfied(cls, a):
                    return True
            return False

        for seed in range(300):
            nv = 6
            cl = generate_2sat(num_vars=nv, num_clauses=8, seed=seed)
            res = two_sat(nv, cl)
            assert (res is not None) == brute_force_sat(nv, cl)
            if res is not None:
                assert cnf_is_satisfied(cl, res)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
