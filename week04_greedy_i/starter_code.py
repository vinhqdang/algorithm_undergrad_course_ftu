"""
Week 04 - Greedy Algorithms I
==============================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem22.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_intervals, is_feasible, interval_depth

Conventions
-----------
- An "interval" (or "request") is a tuple ``(start, finish)`` with
  ``start < finish``, representing a request that occupies a resource during
  the half-open time range ``[start, finish)``.
- A "job" for the lateness-minimization problems is a tuple
  ``(deadline, length)`` (in that order, matching the textbook's $(t_i, d_i)$
  presentation once a schedule fixes an order).
- A "selection" is a list/subset of intervals (e.g. the intervals chosen by a
  scheduling algorithm).
- Random instances are generated with Python's ``random.Random(seed)`` so
  that results are reproducible across runs.
"""

from __future__ import annotations

import random
from typing import List, Tuple

Interval = Tuple[float, float]
Job = Tuple[float, float]  # (deadline, length)


def generate_intervals(n: int, seed: int | None = None, max_start: float = 20.0, max_len: float = 5.0) -> List[Interval]:
    """Generate `n` random intervals (start, finish) with start < finish.

    Starts are uniform in [0, max_start); lengths are uniform in (0, max_len].
    """
    rng = random.Random(seed)
    intervals = []
    for _ in range(n):
        s = rng.uniform(0, max_start)
        length = rng.uniform(0.5, max_len)
        intervals.append((s, s + length))
    return intervals


def generate_jobs(n: int, seed: int | None = None, max_deadline: float = 30.0, max_len: float = 5.0) -> List[Job]:
    """Generate `n` random jobs (deadline, length), with positive lengths."""
    rng = random.Random(seed)
    jobs = []
    for _ in range(n):
        d = rng.uniform(1, max_deadline)
        length = rng.uniform(0.5, max_len)
        jobs.append((d, length))
    return jobs


def is_feasible(selection: List[Interval]) -> bool:
    """Return True iff no two intervals in `selection` overlap.

    Two intervals (s1, f1) and (s2, f2) overlap iff s1 < f2 and s2 < f1
    (they share an open sub-interval of time). Intervals that merely touch at
    an endpoint (f1 == s2) do NOT overlap, since intervals are half-open
    [start, finish).
    """
    sorted_sel = sorted(selection)
    for (_, f_prev), (s_next, _) in zip(sorted_sel, sorted_sel[1:]):
        if s_next < f_prev:
            return False
    return True


def interval_depth(intervals: List[Interval]) -> int:
    """Return the maximum number of intervals that simultaneously overlap.

    This is the classic "depth" of a set of intervals: the minimum number of
    resources (e.g. classrooms) needed so that every interval can be assigned
    a resource with no two overlapping intervals sharing a resource.
    """
    events = []
    for s, f in intervals:
        events.append((s, 1))   # interval starts: +1 to active count
        events.append((f, -1))  # interval ends: -1 (processed before starts at the same time)

    # Sort by time; at equal times, process endings (-1) before starts (+1)
    # so that an interval ending at time t does not count as overlapping with
    # one starting at time t (consistent with half-open [start, finish)).
    events.sort(key=lambda e: (e[0], e[1]))

    active = 0
    max_active = 0
    for _, delta in events:
        active += delta
        max_active = max(max_active, active)
    return max_active


def total_length(selection: List[Interval]) -> float:
    """Return the sum of (finish - start) over all intervals in `selection`."""
    return sum(f - s for s, f in selection)


def schedule_lateness(jobs: List[Job], order: List[int]) -> Tuple[List[float], float]:
    """Given `jobs` (list of (deadline, length)) and a processing `order`
    (a permutation of indices into `jobs`), schedule them back-to-back
    starting at time 0 in that order.

    Returns (finish_times, max_lateness), where finish_times[i] is the
    completion time of jobs[i] (indexed by original job index, not order
    position), and max_lateness = max over i of max(0, finish_times[i] -
    deadline_i).
    """
    finish_times = [0.0] * len(jobs)
    t = 0.0
    max_lateness = 0.0
    for idx in order:
        deadline, length = jobs[idx]
        t += length
        finish_times[idx] = t
        lateness = max(0.0, t - deadline)
        max_lateness = max(max_lateness, lateness)
    return finish_times, max_lateness
