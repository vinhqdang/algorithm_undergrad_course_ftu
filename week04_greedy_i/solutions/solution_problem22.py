"""
Problem 22 - Job Sequencing with Deadlines and Profits (SOLUTION)
=====================================================================
"""

from typing import Dict, List, Tuple

Job = Tuple[int, int]  # (deadline, profit)


def job_sequencing(jobs: List[Job]) -> Tuple[Dict[int, int], int]:
    """Return (schedule, total_profit) for the greedy job-sequencing algorithm."""
    schedule: Dict[int, int] = {}
    total_profit = 0

    order = sorted(range(len(jobs)), key=lambda i: jobs[i][1], reverse=True)
    for idx in order:
        deadline, profit = jobs[idx]
        for slot in range(min(deadline, len(jobs)), 0, -1):
            if slot not in schedule:
                schedule[slot] = idx
                total_profit += profit
                break

    return schedule, total_profit


def is_feasible_schedule(jobs: List[Job], schedule: Dict[int, int]) -> bool:
    """Return True iff every scheduled job meets its deadline and slots are unique."""
    seen_slots = set()
    for slot, job_idx in schedule.items():
        if slot in seen_slots:
            return False
        seen_slots.add(slot)
        deadline, _ = jobs[job_idx]
        if slot > deadline:
            return False
    return True


if __name__ == "__main__":
    jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
    schedule, total_profit = job_sequencing(jobs)

    assert is_feasible_schedule(jobs, schedule)
    assert total_profit == 142
    assert len(schedule) == 3

    empty_schedule, empty_profit = job_sequencing([])
    assert empty_schedule == {}
    assert empty_profit == 0

    single_schedule, single_profit = job_sequencing([(1, 50)])
    assert single_schedule == {1: 0}
    assert single_profit == 50

    two_schedule, two_profit = job_sequencing([(1, 10), (1, 20)])
    assert two_profit == 20
    assert len(two_schedule) == 1

    print("All tests passed!")
