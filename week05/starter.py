"""
Week 5 Starter Code — Greedy Algorithms I
=========================================
Instructions:
  1. Implement each function marked with # TODO.
  2. Do NOT modify the auto-grader section at the bottom.
  3. Run this file: python starter.py
  4. You will see a score out of 100.
"""
import heapq

# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 1 (20 pts): Coin Changing
# ═══════════════════════════════════════════════════════════════════════════════

def coin_changing_greedy(amount: int, coins: list) -> list:
    """
    Implement the greedy coin changing algorithm.
    At each step, select the largest coin denomination less than or equal to the remaining amount.
    
    Input:
      amount: non-negative integer amount to change
      coins: list of positive integers representing available coin denominations
    Returns:
      list of coins selected (sorted descending).
    Raises:
      ValueError if the amount cannot be represented exactly.
    """
    # TODO: implement greedy coin changing
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 2 (20 pts): Interval Scheduling
# ═══════════════════════════════════════════════════════════════════════════════

def interval_scheduling(intervals: list) -> list:
    """
    Finds the maximum number of mutually compatible intervals.
    
    Input:
      intervals: list of tuples (start, end)
    Returns:
      list of indices of the selected intervals in their original input order.
      (i.e., if you select the 0th, 3rd, and 7th elements, return [0, 3, 7]).
    """
    # TODO: implement earliest finish-time first greedy selection
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 3 (20 pts): Interval Partitioning
# ═══════════════════════════════════════════════════════════════════════════════

def interval_partitioning(intervals: list) -> tuple:
    """
    Schedules all intervals using a minimum number of classrooms/rooms.
    No two overlapping intervals can be scheduled in the same room.
    
    Input:
      intervals: list of tuples (start, end)
    Returns:
      tuple (num_rooms, assignment)
      where:
        num_rooms: integer, the minimum number of rooms needed
        assignment: list of room IDs (0, 1, ..., num_rooms-1) assigned to each 
                    interval matching the input sequence order.
    """
    # TODO: implement start-time first greedy allocation using a min-heap
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 4 (20 pts): Scheduling to Minimize Lateness
# ═══════════════════════════════════════════════════════════════════════════════

def minimize_lateness(jobs: list) -> tuple:
    """
    Schedules a list of jobs on a single machine starting at time 0 to minimize
    the maximum lateness of any job.
    
    Input:
      jobs: list of tuples (duration, deadline)
    Returns:
      tuple (max_lateness, schedule)
      where:
        max_lateness: integer, the maximum lateness of any job.
                      Lateness L_i of job i is max(0, finish_time_i - deadline_i)
        schedule: list of tuples (orig_idx, start_time, finish_time) in execution order.
    """
    # TODO: implement Earliest Deadline First (EDF) scheduling
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# PROBLEM 5 (20 pts): Optimal Offline Caching
# ═══════════════════════════════════════════════════════════════════════════════

def optimal_caching(requests: list, cache_size: int) -> int:
    """
    Simulates cache replacement using the optimal Furthest-in-Future (FIF) policy.
    When evicting an item from a full cache, evict the item whose next occurrence
    is furthest in the future. If an item will never be requested again, treat its
    next occurrence as infinity. Break ties by any consistent method.
    
    Input:
      requests: list of items requested (can be strings or numbers)
      cache_size: integer, capacity of the cache
    Returns:
      integer, total number of cache misses.
    """
    # TODO: implement optimal furthest-in-future caching
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# ─────────────────────── AUTO-GRADER ─────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════════════════

def _run_tests():
    score = 0
    total = 100
    results = []

    # ── Problem 1: Coin Changing ─────────────────────────────────────────────
    p1 = 0
    try:
        assert coin_changing_greedy(41, [25, 10, 5, 1]) == [25, 10, 5, 1], "US coins test"
        assert coin_changing_greedy(11, [5, 1]) == [5, 5, 1], "repeated large coins"
        assert coin_changing_greedy(0, [1, 2, 5]) == [], "zero amount"
        try:
            coin_changing_greedy(5, [4, 3])
            assert False, "should raise ValueError for impossible target"
        except ValueError:
            pass # Correct behavior
        p1 = 20
        results.append(("Problem 1 - Coin Changing", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 1 - Coin Changing", f"FAIL: {e}", 0, 20))
    score += p1

    # ── Problem 2: Interval Scheduling ───────────────────────────────────────
    p2 = 0
    try:
        ints = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
        res2 = interval_scheduling(ints)
        assert res2 == [0, 3, 7], f"Expected indices [0, 3, 7], got {res2}"
        assert interval_scheduling([]) == [], "empty intervals"
        assert interval_scheduling([(1, 2)]) == [0], "single interval"
        p2 = 20
        results.append(("Problem 2 - Interval Scheduling", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 2 - Interval Scheduling", f"FAIL: {e}", 0, 20))
    score += p2

    # ── Problem 3: Interval Partitioning ─────────────────────────────────────
    p3 = 0
    try:
        part_ints = [(900, 1030), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)]
        num_rooms, assignments = interval_partitioning(part_ints)
        assert num_rooms == 3, f"Expected 3 rooms, got {num_rooms}"
        assert len(assignments) == len(part_ints), "room assigned to each interval"
        
        # Verify no overlaps in same room
        rooms = {}
        for idx, r_id in enumerate(assignments):
            assert 0 <= r_id < num_rooms, f"Room ID {r_id} out of bounds"
            rooms.setdefault(r_id, []).append(part_ints[idx])
        for r_id, assigned_ints in rooms.items():
            sorted_assigned = sorted(assigned_ints)
            for j in range(len(sorted_assigned) - 1):
                assert sorted_assigned[j][1] <= sorted_assigned[j+1][0], f"Overlapping intervals in room {r_id}"
                
        p3 = 20
        results.append(("Problem 3 - Interval Partitioning", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 3 - Interval Partitioning", f"FAIL: {e}", 0, 20))
    score += p3

    # ── Problem 4: Scheduling to Minimize Lateness ───────────────────────────
    p4 = 0
    try:
        jobs = [(3, 6), (2, 5), (1, 8)]
        max_lat, sched = minimize_lateness(jobs)
        assert max_lat == 0, f"Expected 0 lateness, got {max_lat}"
        assert len(sched) == 3, "All jobs scheduled"
        
        jobs2 = [(2, 2), (4, 3)]
        max_lat2, sched2 = minimize_lateness(jobs2)
        assert max_lat2 == 3, f"Expected max lateness 3, got {max_lat2}"
        
        # Verify schedule continuity
        curr = 0
        for orig_idx, start, end in sched2:
            assert start == curr, f"Schedule gap or overlap: expected start {curr}, got {start}"
            assert end == start + jobs2[orig_idx][0], "Incorrect duration"
            curr = end
            
        p4 = 20
        results.append(("Problem 4 - Minimize Lateness", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 4 - Minimize Lateness", f"FAIL: {e}", 0, 20))
    score += p4

    # ── Problem 5: Optimal Offline Caching ───────────────────────────────────
    p5 = 0
    try:
        reqs = ['a', 'b', 'c', 'd', 'a', 'b', 'e', 'a', 'd', 'b', 'c', 'd']
        misses = optimal_caching(reqs, 3)
        assert misses == 7, f"Expected 7 misses, got {misses}"
        
        reqs2 = [1, 2, 3, 4, 1, 2, 3, 4]
        assert optimal_caching(reqs2, 4) == 4, "no evictions needed for cache size == requests types"
        p5 = 20
        results.append(("Problem 5 - Optimal Caching", "PASS", 20, 20))
    except Exception as e:
        results.append(("Problem 5 - Optimal Caching", f"FAIL: {e}", 0, 20))
    score += p5

    # ── Report ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 62)
    print("  WEEK 5 AUTO-GRADER RESULTS")
    print("=" * 62)
    for name, status, pts, max_pts in results:
        mark = "[PASS]" if "PASS" in status else "[FAIL]"
        print(f"  {mark} {name:<35} {pts:>3}/{max_pts}")
        if "FAIL" in status:
            print(f"      -> {status[5:]}")
    print("-" * 62)
    print(f"  TOTAL SCORE: {score}/{total}  ({score}%)")
    if score == total:
        print("  Perfect score! Excellent work!")
    elif score >= 80:
        print("  Good job! Review the failed tests.")
    else:
        print("  Keep practicing. Re-read the lecture notes.")
    print("=" * 62 + "\n")
    return score


if __name__ == "__main__":
    _run_tests()
