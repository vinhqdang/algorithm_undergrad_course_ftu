"""
Problem 06 - Assignment Feasibility (Perfect Matching of One Side)
==================================================================

Implement `can_assign_everyone(people, tasks, allowed)`: return True iff every
person can be assigned a distinct allowed task. This is exactly: does the
bipartite graph (people = left, tasks = right, `allowed` pairs = edges) have a
matching saturating ALL people?

Also implement `assignment(people, tasks, allowed)` returning a person -> task
dict if everyone can be assigned, else an empty dict.

Use kuhn_matching from Problem 2.

See practical_exercises.pdf, Problem 6, for the full statement and examples.
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem02 import kuhn_matching

Pair = Tuple[Hashable, Hashable]


def can_assign_everyone(
    people: List[Hashable], tasks: List[Hashable], allowed: List[Pair]
) -> bool:
    """Return True iff every person can be assigned a distinct allowed task."""
    # TODO: implement this function.
    raise NotImplementedError


def assignment(
    people: List[Hashable], tasks: List[Hashable], allowed: List[Pair]
) -> Dict[Hashable, Hashable]:
    """Return a person -> task assignment if everyone can be assigned, else {}."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        people = ["Ann", "Bob", "Cy"]
        tasks = ["t1", "t2", "t3"]
        allowed = [("Ann", "t1"), ("Bob", "t2"), ("Cy", "t3"), ("Ann", "t2")]
        assert can_assign_everyone(people, tasks, allowed) is True
        asn = assignment(people, tasks, allowed)
        assert set(asn.keys()) == set(people)
        assert len(set(asn.values())) == 3

        assert can_assign_everyone(["A", "B"], ["t"], [("A", "t"), ("B", "t")]) is False
        assert assignment(["A", "B"], ["t"], [("A", "t"), ("B", "t")]) == {}
        assert can_assign_everyone(["A", "B"], ["t1", "t2"], [("A", "t1")]) is False
        assert can_assign_everyone(["A"], ["t1", "t2"], [("A", "t1"), ("A", "t2")]) is True
        assert can_assign_everyone([], ["t1"], []) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
