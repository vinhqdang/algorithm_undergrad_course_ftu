"""
Problem 14 - Counter-Example: Shortest-Job-First Is Not Optimal for Lateness
===============================================================================

Another tempting greedy heuristic is "process jobs in order of increasing
LENGTH" (shortest job first), ignoring deadlines entirely. Implement
`shortest_job_first(jobs)`:

    Sort jobs by length, ascending (ties broken arbitrarily), and schedule
    them back-to-back in that order starting at time 0.

Return `(order, max_lateness)` exactly like `earliest_deadline_first`
(Problem 11): `order` is the list of original indices in the order they are
scheduled, and `max_lateness` is computed via `schedule_lateness`.

Then implement `counter_example_instance()` returning a list of jobs
`(deadline, length)` on which `shortest_job_first` produces a STRICTLY LARGER
max lateness than `earliest_deadline_first` (Problem 11) -- demonstrating
that "shortest job first" is not a correct greedy rule for minimizing
lateness.

Hint: give a very short job a very tight deadline, and a longer job a much
later deadline.

See practical_exercises.pdf, Problem 14.
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem11 import earliest_deadline_first
from starter_code import schedule_lateness

Job = Tuple[float, float]


def shortest_job_first(jobs: List[Job]) -> Tuple[List[int], float]:
    """Return (order, max_lateness) for the shortest-job-first schedule."""
    # TODO: implement this function.
    raise NotImplementedError


def counter_example_instance() -> List[Job]:
    """Return an instance where shortest_job_first is strictly worse than EDF."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        instance = counter_example_instance()
        _, sjf_lateness = shortest_job_first(instance)
        _, edf_lateness = earliest_deadline_first(instance)

        assert sjf_lateness > edf_lateness, (
            f"shortest-job-first lateness = {sjf_lateness}, "
            f"earliest-deadline-first lateness = {edf_lateness}"
        )

        print(f"shortest-job-first max lateness = {sjf_lateness}; "
              f"EDF max lateness = {edf_lateness}.")
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
