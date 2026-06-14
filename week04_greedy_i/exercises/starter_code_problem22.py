"""
Problem 22 - Job Sequencing with Deadlines and Profits
=========================================================

In this variant, each job `i` has a DEADLINE `d_i` (a positive integer) and a
PROFIT `p_i`. Every job takes exactly 1 unit of time, and there is a single
machine. A job earns its profit ONLY IF it is scheduled to finish AT OR
BEFORE its deadline (it may be left unscheduled entirely, earning nothing).
The goal is to select a subset of jobs and an assignment of each to a
distinct time slot `1, 2, 3, ...` (each slot used at most once, each job
finishing by its deadline) that MAXIMIZES total profit.

Implement `job_sequencing(jobs)`, where `jobs` is a list of `(deadline,
profit)` tuples:

    Sort jobs by profit, DESCENDING. For each job in this order, try to place
    it in the LATEST free time slot `t` with `1 <= t <= deadline` (this is
    the standard greedy for this problem -- placing as late as possible
    leaves earlier slots open for jobs with tighter deadlines). If such a
    slot exists, schedule the job there (earning its profit); otherwise skip
    it.

Return `(schedule, total_profit)` where `schedule` is a dict mapping time
slot (int, 1-indexed) -> index into `jobs` for every slot that is used, and
`total_profit` is the sum of profits of scheduled jobs.

Then implement `is_feasible_schedule(jobs, schedule)` that returns True iff,
for every `(slot, job_index)` in `schedule`, `slot <= jobs[job_index][0]`
(the job's deadline) AND no two entries share the same slot (the latter is
automatically true since `schedule` is a dict keyed by slot, but check it
defensively by construction in your implementation).

See practical_exercises.pdf, Problem 22.
"""

from typing import Dict, List, Tuple

Job = Tuple[int, int]  # (deadline, profit)


def job_sequencing(jobs: List[Job]) -> Tuple[Dict[int, int], int]:
    """Return (schedule, total_profit) for the greedy job-sequencing algorithm."""
    # TODO: implement this function.
    raise NotImplementedError


def is_feasible_schedule(jobs: List[Job], schedule: Dict[int, int]) -> bool:
    """Return True iff every scheduled job meets its deadline and slots are unique."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Classic example: jobs (deadline, profit)
        #   J1: d=2, p=100
        #   J2: d=1, p=19
        #   J3: d=2, p=27
        #   J4: d=1, p=25
        #   J5: d=3, p=15
        jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
        schedule, total_profit = job_sequencing(jobs)

        assert is_feasible_schedule(jobs, schedule)
        # Optimal total profit is 100 + 27 + 15 = 142
        # (J1 in slot 2, J3 in slot 1... or some feasible arrangement
        # achieving the same total).
        assert total_profit == 142
        assert len(schedule) == 3

        # No jobs -> empty schedule, zero profit.
        empty_schedule, empty_profit = job_sequencing([])
        assert empty_schedule == {}
        assert empty_profit == 0

        # A single job with deadline 1 -> scheduled in slot 1.
        single_schedule, single_profit = job_sequencing([(1, 50)])
        assert single_schedule == {1: 0}
        assert single_profit == 50

        # Two jobs both with deadline 1 -> only the higher-profit one fits.
        two_schedule, two_profit = job_sequencing([(1, 10), (1, 20)])
        assert two_profit == 20
        assert len(two_schedule) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
