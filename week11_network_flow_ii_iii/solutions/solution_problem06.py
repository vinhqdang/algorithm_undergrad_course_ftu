"""
Problem 06 - Assignment Feasibility (Perfect Matching of One Side) (SOLUTION)
=============================================================================
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem02 import kuhn_matching

Vertex = Hashable
Pair = Tuple[Hashable, Hashable]


def can_assign_everyone(
    people: List[Hashable], tasks: List[Hashable], allowed: List[Pair]
) -> bool:
    """Return True iff every person can be assigned a distinct allowed task.

    This is exactly: does the bipartite graph (people on the left, tasks on the
    right, ``allowed`` pairs as edges) have a matching saturating ALL people?
    """
    matching = kuhn_matching(people, tasks, allowed)  # task -> person
    return len(matching) == len(people)


def assignment(
    people: List[Hashable], tasks: List[Hashable], allowed: List[Pair]
) -> Dict[Hashable, Hashable]:
    """Return a person -> task assignment if everyone can be assigned, else {}.

    The assignment, when non-empty, gives every person a distinct task.
    """
    match_right = kuhn_matching(people, tasks, allowed)  # task -> person
    if len(match_right) != len(people):
        return {}
    return {person: task for task, person in match_right.items()}


if __name__ == "__main__":
    # Everyone assignable: each person has their own task.
    people = ["Ann", "Bob", "Cy"]
    tasks = ["t1", "t2", "t3"]
    allowed = [("Ann", "t1"), ("Bob", "t2"), ("Cy", "t3"), ("Ann", "t2")]
    assert can_assign_everyone(people, tasks, allowed) is True
    asn = assignment(people, tasks, allowed)
    assert set(asn.keys()) == set(people)
    assert len(set(asn.values())) == 3  # distinct tasks

    # Two people, one task -> impossible.
    assert can_assign_everyone(["A", "B"], ["t"], [("A", "t"), ("B", "t")]) is False
    assert assignment(["A", "B"], ["t"], [("A", "t"), ("B", "t")]) == {}

    # A person with no allowed task -> impossible.
    assert can_assign_everyone(["A", "B"], ["t1", "t2"], [("A", "t1")]) is False

    # More tasks than people, all coverable.
    assert can_assign_everyone(["A"], ["t1", "t2"], [("A", "t1"), ("A", "t2")]) is True

    # Empty set of people: vacuously assignable.
    assert can_assign_everyone([], ["t1"], []) is True

    print("All tests passed!")
