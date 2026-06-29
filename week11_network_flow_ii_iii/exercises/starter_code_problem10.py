"""
Problem 10 - Project Selection / Max-Weight Closure via Min-Cut
===============================================================

Implement `select_projects(profits, prerequisites)`: choose a subset S of
projects maximizing total profit, where S must be CLOSED under prerequisites
(if p in S and (p, q) is a prerequisite, then q in S too). Profits may be
negative.

Reduction to min-cut (Kleinberg-Tardos Section 7.11):
  - source -> p with capacity profit[p]   for each p with profit > 0
  - p -> sink with capacity -profit[p]     for each p with profit < 0
  - prerequisite edge p -> q with capacity infinity
Then max profit = (sum of positive profits) - (min cut), and the selected set is
the source side of the min cut. Use `MaxFlow.min_cut_reachable`.

Return `(max_profit, selected_set)`.

Also implement `brute_force_select(profits, prerequisites)` (try all closed
subsets) so you can verify the min-cut answer on small inputs.

See practical_exercises.pdf, Problem 10, for the full statement and examples.
"""

import os
import sys
from itertools import combinations
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import MaxFlow

Project = Hashable


def select_projects(
    profits: Dict[Project, float],
    prerequisites: List[Tuple[Project, Project]],
) -> Tuple[float, set]:
    """Maximum-profit feasible (closed) subset of projects, via min-cut."""
    # TODO: implement this function using MaxFlow.
    raise NotImplementedError


def brute_force_select(
    profits: Dict[Project, float],
    prerequisites: List[Tuple[Project, Project]],
) -> float:
    """Brute-force max profit over all closed subsets (for small instances)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        profits = {"A": 10, "B": -4}
        prereqs = [("A", "B")]
        val, sel = select_projects(profits, prereqs)
        assert abs(val - 6) < 1e-9, val
        assert sel == {"A", "B"}

        profits2 = {"A": 3, "B": -10}
        prereqs2 = [("A", "B")]
        val2, sel2 = select_projects(profits2, prereqs2)
        assert abs(val2 - 0) < 1e-9, val2
        assert sel2 == set()

        import random
        rng = random.Random(2024)
        for trial in range(80):
            n = rng.randint(1, 6)
            profs = {i: rng.randint(-10, 10) for i in range(n)}
            prq = []
            for i in range(n):
                for j in range(n):
                    if i != j and rng.random() < 0.25:
                        prq.append((i, j))
            flow_val, _ = select_projects(profs, prq)
            bf = brute_force_select(profs, prq)
            assert abs(flow_val - bf) < 1e-9, (trial, flow_val, bf)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
