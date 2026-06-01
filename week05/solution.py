"""
Week 5 SOLUTION — Reference implementations for the 5 classic greedy algorithms.
Do not distribute to students before the deadline.
"""
import heapq

# ── 1. COIN CHANGING ──────────────────────────────────────────────────────────

def coin_changing_greedy(amount: int, coins: list) -> list:
    """
    Greedy coin changing algorithm.
    Selects the largest coin denomination less than or equal to the remaining amount.
    Returns: list of coins selected (sorted descending).
    Raises ValueError if the amount cannot be represented exactly with the given system.
    """
    sorted_coins = sorted(coins, reverse=True)
    result = []
    rem = amount
    for c in sorted_coins:
        while rem >= c:
            result.append(c)
            rem -= c
    if rem > 0:
        raise ValueError("Cannot represent the amount with the given coin denominations.")
    return result

# ── 2. INTERVAL SCHEDULING ──────────────────────────────────────────────────

def interval_scheduling(intervals: list) -> list:
    """
    Solves the Interval Scheduling Problem to maximize mutually compatible intervals.
    Input: list of tuples (start, end)
    Returns: list of indices of the selected intervals in their original input order.
    """
    if not intervals:
        return []
    # Sort by earliest finish time (end)
    sorted_intervals = sorted(enumerate(intervals), key=lambda x: x[1][1])
    selected_indices = []
    last_end = -float('inf')
    for idx, (start, end) in sorted_intervals:
        if start >= last_end:
            selected_indices.append(idx)
            last_end = end
    return sorted(selected_indices)

# ── 3. INTERVAL PARTITIONING ────────────────────────────────────────────────

def interval_partitioning(intervals: list) -> tuple:
    """
    Solves the Interval Partitioning Problem to schedule all intervals in minimum rooms.
    Input: list of tuples (start, end)
    Returns: tuple (num_rooms, assignment)
      where num_rooms is the minimum number of rooms needed,
      and assignment is a list of room IDs assigned to each interval (matching input index).
    """
    if not intervals:
        return (0, [])
    
    # Sort intervals by start time, keeping track of original index
    indexed_intervals = sorted(enumerate(intervals), key=lambda x: x[1][0])
    
    # Min-heap stores tuples of (end_time, room_id)
    heap = []
    room_count = 0
    assignment = [0] * len(intervals)
    
    for orig_idx, (start, end) in indexed_intervals:
        if heap and heap[0][0] <= start:
            # We can re-use the room that finishes earliest
            earliest_end, room_id = heapq.heappop(heap)
            heapq.heappush(heap, (end, room_id))
            assignment[orig_idx] = room_id
        else:
            # Allocate a new room
            room_id = room_count
            room_count += 1
            heapq.heappush(heap, (end, room_id))
            assignment[orig_idx] = room_id
            
    return (room_count, assignment)

# ── 4. SCHEDULING TO MINIMIZE LATENESS ──────────────────────────────────────

def minimize_lateness(jobs: list) -> tuple:
    """
    Schedules jobs to minimize the maximum lateness.
    Input: list of tuples (duration, deadline)
    Returns: tuple (max_lateness, schedule)
      where max_lateness is the maximum lateness of any job,
      and schedule is a list of tuples (orig_idx, start_time, finish_time) in execution order.
    """
    if not jobs:
        return (0, [])
    
    # Sort jobs by deadline (Earliest Deadline First - EDF)
    sorted_jobs = sorted(enumerate(jobs), key=lambda x: x[1][1])
    
    current_time = 0
    max_lateness = 0
    schedule = []
    
    for orig_idx, (duration, deadline) in sorted_jobs:
        start_time = current_time
        finish_time = current_time + duration
        lateness = max(0, finish_time - deadline)
        max_lateness = max(max_lateness, lateness)
        schedule.append((orig_idx, start_time, finish_time))
        current_time = finish_time
        
    return (max_lateness, schedule)

# ── 5. OPTIMAL OFFLINE CACHING ──────────────────────────────────────────────

def optimal_caching(requests: list, cache_size: int) -> int:
    """
    Simulates cache replacement using the optimal Furthest-in-Future (FIF) policy.
    Input: requests (list of requested pages), cache_size (int)
    Returns: number of cache misses.
    """
    cache = set()
    misses = 0
    
    for i, req in enumerate(requests):
        if req in cache:
            # Cache hit
            continue
        
        # Cache miss
        misses += 1
        if len(cache) < cache_size:
            cache.add(req)
        else:
            # Evict furthest-in-future
            furthest_idx = -1
            evict_item = None
            
            for item in cache:
                try:
                    # Find next occurrence of item in remaining requests
                    next_occurrence = requests.index(item, i + 1)
                except ValueError:
                    # Item will never be requested again (infinity index)
                    next_occurrence = float('inf')
                
                if next_occurrence > furthest_idx:
                    furthest_idx = next_occurrence
                    evict_item = item
                    
            cache.remove(evict_item)
            cache.add(req)
            
    return misses

# ── Self-check tests ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 1. Coin Changing
    assert coin_changing_greedy(41, [25, 10, 5, 1]) == [25, 10, 5, 1]
    assert coin_changing_greedy(11, [5, 1]) == [5, 5, 1]
    
    # 2. Interval Scheduling
    ints = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
    # Selected should be index: 0: (1,4), 3: (5,7), 7: (8,11)
    assert interval_scheduling(ints) == [0, 3, 7]
    
    # 3. Interval Partitioning
    part_ints = [(900, 1030), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)]
    num_rooms, assignments = interval_partitioning(part_ints)
    assert num_rooms == 3, f"Expected 3 rooms, got {num_rooms}"
    # Verify no overlaps in same room
    rooms = {}
    for idx, r_id in enumerate(assignments):
        rooms.setdefault(r_id, []).append(part_ints[idx])
    for r_id, assigned_ints in rooms.items():
        sorted_assigned = sorted(assigned_ints)
        for j in range(len(sorted_assigned)-1):
            assert sorted_assigned[j][1] <= sorted_assigned[j+1][0], "Overlapping intervals assigned to same room!"
            
    # 4. Minimize Lateness
    jobs = [(3, 6), (2, 5), (1, 8)] # Durations and deadlines
    # EDF Order: Job 1 (2, 5), Job 0 (3, 6), Job 2 (1, 8)
    # Job 1 starts at 0, finishes at 2. Lateness = max(0, 2 - 5) = 0
    # Job 0 starts at 2, finishes at 5. Lateness = max(0, 5 - 6) = 0
    # Job 2 starts at 5, finishes at 6. Lateness = max(0, 6 - 8) = 0
    max_lat, sched = minimize_lateness(jobs)
    assert max_lat == 0, f"Expected 0 lateness, got {max_lat}"
    
    jobs2 = [(2, 2), (4, 3)]
    # EDF: Job 0 (2, 2), Job 1 (4, 3)
    # Job 0 finishes at 2. Lateness = 0.
    # Job 1 finishes at 6. Lateness = 6 - 3 = 3.
    # EDF max lateness is 3.
    # Alt: Job 1 finishes at 4. Lateness = 1.
    # Job 0 finishes at 6. Lateness = 4. Max is 4.
    max_lat2, _ = minimize_lateness(jobs2)
    assert max_lat2 == 3, f"Expected 3 lateness, got {max_lat2}"
    
    # 5. Optimal Caching
    reqs = ['a', 'b', 'c', 'd', 'a', 'b', 'e', 'a', 'd', 'b', 'c', 'd']
    # Cache size 3.
    # Misses:
    # 'a' (miss, cache [a])
    # 'b' (miss, cache [a,b])
    # 'c' (miss, cache [a,b,c])
    # 'd' (miss, evict 'c' because 'a' and 'b' requested next, cache [a,b,d])
    # 'a' (hit)
    # 'b' (hit)
    # 'e' (miss, evict 'd' because 'a' is requested next and 'b' next, cache [a,b,e])
    # 'a' (hit)
    # 'd' (miss, evict 'e', cache [a,b,d])
    # 'b' (hit)
    # 'c' (miss, evict 'd', cache [a,b,c])
    # 'd' (miss, cache [a,b,d] or similar)
    # Total misses: 7
    misses = optimal_caching(reqs, 3)
    assert misses == 7, f"Expected 7 misses, got {misses}"
    
    print("All reference solutions and self-checks passed successfully.")
