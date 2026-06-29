"""
Problem 10 - Project Selection / Max-Weight Closure via Min-Cut (SOLUTION)
==========================================================================
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
    """Maximum-profit feasible subset of projects (max-weight closure).

    Each project has a profit (possibly negative). ``prerequisites`` is a list
    of ``(p, q)`` meaning "selecting p REQUIRES also selecting q". We want the
    subset S that is closed under prerequisites (if p in S then q in S) and
    maximizes the total profit.

    Reduction to min-cut (Kleinberg-Tardos Section 7.11):
      - source s -> project p with capacity profit[p], for each p with profit > 0.
      - project p -> sink t with capacity -profit[p], for each p with profit < 0.
      - prerequisite edge p -> q with capacity infinity.
    Then max profit = (sum of positive profits) - (min cut value), and the
    selected set is the source side of the min cut (excluding s).

    Returns ``(max_profit, selected_set)``.
    """
    mf = MaxFlow()
    s, t = "__source__", "__sink__"
    positive_sum = 0.0
    for p, w in profits.items():
        if w > 0:
            mf.add_edge(s, p, w)
            positive_sum += w
        elif w < 0:
            mf.add_edge(p, t, -w)
    for p, q in prerequisites:
        mf.add_edge(p, q, float("inf"))

    min_cut = mf.max_flow(s, t)
    max_profit = positive_sum - min_cut

    reachable = mf.min_cut_reachable(s)
    selected = {p for p in profits if p in reachable}
    return max_profit, selected


def brute_force_select(
    profits: Dict[Project, float],
    prerequisites: List[Tuple[Project, Project]],
) -> float:
    """Brute-force max profit over all closed subsets (for small instances)."""
    items = list(profits.keys())
    best = 0.0  # empty set is always feasible with profit 0
    for r in range(len(items) + 1):
        for sub in combinations(items, r):
            chosen = set(sub)
            # Check closure under prerequisites.
            if all((p not in chosen) or (q in chosen) for p, q in prerequisites):
                total = sum(profits[p] for p in chosen)
                best = max(best, total)
    return best


if __name__ == "__main__":
    # Simple example: project A (+10) needs tool B (-4). Net +6 > 0, take both.
    profits = {"A": 10, "B": -4}
    prereqs = [("A", "B")]
    val, sel = select_projects(profits, prereqs)
    assert abs(val - 6) < 1e-9, val
    assert sel == {"A", "B"}

    # Prerequisite too expensive: A (+3) needs B (-10). Better to take nothing.
    profits2 = {"A": 3, "B": -10}
    prereqs2 = [("A", "B")]
    val2, sel2 = select_projects(profits2, prereqs2)
    assert abs(val2 - 0) < 1e-9, val2
    assert sel2 == set()

    # Cross-check against brute force on random small instances.
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
        assert abs(flow_val - bf) < 1e-9, (trial, flow_val, bf, profs, prq)

    print("All tests passed!")
