"""
Week 5 Demo: Classic Greedy Algorithms Visualization
======================================================
Demonstrates the 5 classic greedy algorithms:
  1. Coin Changing
  2. Interval Scheduling
  3. Interval Partitioning
  4. Scheduling to Minimize Lateness
  5. Optimal Offline Caching (Furthest-in-Future vs LRU/FIFO)

Generates beautiful visualization plots and saves them as PNGs.
"""
import matplotlib.pyplot as plt
import collections
import random
import heapq

# ── Import reference solutions ───────────────────────────────────────────────
try:
    from week05.solution import (
        coin_changing_greedy,
        interval_scheduling,
        interval_partitioning,
        minimize_lateness,
        optimal_caching
    )
except ImportError:
    # Fallback in case of local execution import differences
    from solution import (
        coin_changing_greedy,
        interval_scheduling,
        interval_partitioning,
        minimize_lateness,
        optimal_caching
    )

# ── 1. COIN CHANGING DEMO ─────────────────────────────────────────────────────

def run_coin_changing_demo():
    print("\n--- 1. Coin Changing Demo ---")
    coins = [25, 10, 5, 1]
    amounts = [41, 99, 13]
    for amt in amounts:
        res = coin_changing_greedy(amt, coins)
        print(f"Amount {amt}c with US coins {coins} -> {len(res)} coins: {res}")
        
    non_canonical_coins = [4, 3, 1]
    # For amount 6, greedy gives 4 + 1 + 1 (3 coins), optimal is 3 + 3 (2 coins)
    res_nc = coin_changing_greedy(6, non_canonical_coins)
    print(f"Amount 6c with Non-Canonical coins {non_canonical_coins} -> Greedy: {res_nc} (3 coins, Sub-optimal!)")

# ── 2. INTERVAL SCHEDULING VISUALIZATION ──────────────────────────────────────

def run_interval_scheduling_visual():
    print("\n--- 2. Interval Scheduling Visualizing ---")
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
    selected_indices = interval_scheduling(intervals)
    print(f"All intervals: {intervals}")
    print(f"Selected index subset: {selected_indices}")
    
    # Visualization setup
    plt.figure(figsize=(10, 5))
    colors = ['#E2E8F0'] * len(intervals) # default soft gray-blue
    for idx in selected_indices:
        colors[idx] = '#10B981' # emerald green for selected
        
    for idx, (start, end) in enumerate(intervals):
        # Plot interval bar
        plt.barh(idx, end - start, left=start, color=colors[idx], edgecolor='#475569', height=0.6, align='center')
        # Add labels
        label = f"Job {idx}: [{start}, {end}]"
        if idx in selected_indices:
            label += " (Selected)"
        plt.text(start + 0.1, idx - 0.1, label, fontsize=9, fontweight='bold' if idx in selected_indices else 'normal')
        
    plt.yticks(range(len(intervals)), [f"Index {i}" for i in range(len(intervals))])
    plt.xlabel("Timeline")
    plt.ylabel("Interval Index")
    plt.title("Interval Scheduling Optimization (Earliest Finish Time First)", fontsize=12, fontweight='bold')
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("week05/greedy_interval_scheduling.png", dpi=150)
    plt.close()
    print("Saved visual: week05/greedy_interval_scheduling.png")

# ── 3. INTERVAL PARTITIONING VISUALIZATION ────────────────────────────────────

def run_interval_partitioning_visual():
    print("\n--- 3. Interval Partitioning Visualizing ---")
    intervals = [(9, 10.5), (9.6, 12), (9.8, 11.3), (11, 11.5), (15, 19), (18, 20)]
    num_rooms, assignments = interval_partitioning(intervals)
    print(f"Intervals to partition: {intervals}")
    print(f"Rooms needed: {num_rooms}, Assignments: {assignments}")
    
    # Visualization setup
    plt.figure(figsize=(10, 5))
    room_colors = ['#3B82F6', '#EF4444', '#F59E0B', '#8B5CF6', '#10B981'] # Sleek modern palette
    
    for idx, (start, end) in enumerate(intervals):
        room_id = assignments[idx]
        color = room_colors[room_id % len(room_colors)]
        # Plot room placement
        plt.barh(room_id, end - start, left=start, color=color, edgecolor='#1E293B', height=0.5, alpha=0.85)
        plt.text(start + (end-start)/3, room_id - 0.05, f"Int {idx} ({start}-{end})", 
                 color='white', fontweight='bold', fontsize=8)
                 
    plt.yticks(range(num_rooms), [f"Classroom {r}" for r in range(num_rooms)])
    plt.xlabel("Timeline")
    plt.title("Interval Partitioning (Minimum Room Scheduling)", fontsize=12, fontweight='bold')
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.ylim(-0.5, num_rooms - 0.5)
    plt.tight_layout()
    plt.savefig("week05/greedy_interval_partitioning.png", dpi=150)
    plt.close()
    print("Saved visual: week05/greedy_interval_partitioning.png")

# ── 4. SCHEDULING TO MINIMIZE LATENESS VISUALIZATION ─────────────────────────

def run_minimize_lateness_visual():
    print("\n--- 4. Minimize Lateness Visualizing ---")
    jobs = [(3, 6), (2, 5), (1, 8), (4, 9)] # duration, deadline
    max_lat, sched = minimize_lateness(jobs)
    print(f"Jobs: {jobs}")
    print(f"Max lateness: {max_lat}, Execution timeline: {sched}")
    
    # Visualization setup
    plt.figure(figsize=(10, 5))
    
    # Plotting scheduled job execution blocks
    for order, (orig_idx, start, end) in enumerate(sched):
        duration, deadline = jobs[orig_idx]
        lateness = max(0, end - deadline)
        
        # Plot job execution bar
        plt.barh(0, end - start, left=start, color='#60A5FA', edgecolor='#1E3A8A', height=0.4, align='center')
        plt.text(start + 0.1, 0, f"Job {orig_idx}\n(d={duration})", color='white', fontsize=8, fontweight='bold', ha='left', va='center')
        
        # Plot deadline marker
        plt.axvline(x=deadline, color='#EF4444', linestyle='--', linewidth=1.5, alpha=0.8)
        plt.text(deadline, 0.25, f"d_{orig_idx} ({deadline})", color='#EF4444', rotation=45, fontsize=8, fontweight='bold')
        
        # Highlight lateness region
        if lateness > 0:
            plt.barh(-0.15, lateness, left=deadline, color='#FCA5A5', edgecolor='#B91C1C', height=0.1, align='center')
            plt.text(deadline + lateness/2, -0.25, f"Late {lateness}", color='#B91C1C', fontsize=8, fontweight='bold', ha='center')
            
    plt.yticks([0], ["Machine"])
    plt.xlabel("Timeline")
    plt.title(f"Scheduling to Minimize Lateness (EDF Optimization) | Max Lateness = {max_lat}", fontsize=11, fontweight='bold')
    plt.grid(True, axis='x', linestyle=':', alpha=0.7)
    plt.ylim(-0.4, 0.4)
    plt.tight_layout()
    plt.savefig("week05/greedy_minimize_lateness.png", dpi=150)
    plt.close()
    print("Saved visual: week05/greedy_minimize_lateness.png")

# ── 5. OPTIMAL OFFLINE CACHING SIMULATION & GRAPH ───────────────────────────

def fifo_caching(requests: list, cache_size: int) -> int:
    """FIFO replacement policy."""
    cache = set()
    queue = collections.deque()
    misses = 0
    for req in requests:
        if req in cache:
            continue
        misses += 1
        if len(cache) < cache_size:
            cache.add(req)
            queue.append(req)
        else:
            oldest = queue.popleft()
            cache.remove(oldest)
            cache.add(req)
            queue.append(req)
    return misses

def lru_caching(requests: list, cache_size: int) -> int:
    """LRU replacement policy."""
    cache = set()
    history = [] # Tracks usage order
    misses = 0
    for req in requests:
        if req in cache:
            # Move to end of history
            history.remove(req)
            history.append(req)
            continue
        misses += 1
        if len(cache) < cache_size:
            cache.add(req)
            history.append(req)
        else:
            lru_item = history.pop(0)
            cache.remove(lru_item)
            cache.add(req)
            history.append(req)
    return misses

def run_optimal_caching_simulation():
    print("\n--- 5. Caching Simulation & Performance Graphs ---")
    
    # Generate requests with locality of reference (e.g. repeated patterns)
    random.seed(42)
    pages = ['A', 'B', 'C', 'D', 'E', 'F']
    requests = []
    # Generate 100 patterned page requests
    for _ in range(20):
        # Choose a sub-working set
        working_set = random.sample(pages, 3)
        for _ in range(5):
            requests.append(random.choice(working_set))
            
    print(f"First 30 page requests: {requests[:30]}")
    
    cache_sizes = [2, 3, 4, 5]
    opt_misses = []
    fifo_misses = []
    lru_misses = []
    
    print(f"\n{'Size':^6} | {'OPT (FIF)':^10} | {'LRU':^10} | {'FIFO':^10}")
    print("-" * 46)
    for k in cache_sizes:
        opt = optimal_caching(requests, k)
        fifo = fifo_caching(requests, k)
        lru = lru_caching(requests, k)
        opt_misses.append(opt)
        fifo_misses.append(fifo)
        lru_misses.append(lru)
        print(f"{k:^6} | {opt:^10} | {lru:^10} | {fifo:^10}")
        
    # Plot comparison chart
    plt.figure(figsize=(8, 5))
    plt.plot(cache_sizes, opt_misses, 'o-', color='#10B981', label='Optimal (Furthest-in-Future)', linewidth=2.5)
    plt.plot(cache_sizes, lru_misses, 's--', color='#3B82F6', label='LRU (Least Recently Used)', linewidth=1.8)
    plt.plot(cache_sizes, fifo_misses, '^:', color='#EF4444', label='FIFO (First In First Out)', linewidth=1.8)
    
    plt.xlabel("Cache Size (k)", fontweight='bold')
    plt.ylabel("Cache Misses", fontweight='bold')
    plt.title("Cache Replacement Policy Performance Comparison", fontsize=11, fontweight='bold')
    plt.xticks(cache_sizes)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig("week05/greedy_optimal_caching.png", dpi=150)
    plt.close()
    print("\nSaved visual comparison: week05/greedy_optimal_caching.png")


# ── MAIN DEMONSTRATOR ────────────────────────────────────────────────────────

def main():
    print("======================================================")
    print("  WEEK 5 CLASSIC GREEDY ALGORITHMS RUNTIME DEMO")
    print("======================================================")
    
    run_coin_changing_demo()
    run_interval_scheduling_visual()
    run_interval_partitioning_visual()
    run_minimize_lateness_visual()
    run_optimal_caching_simulation()
    
    print("\n" + "=" * 54)
    print("  DEMO RUNS COMPLETED. ALL VISUALIZATIONS GENERATED.")
    print("=" * 54)

if __name__ == "__main__":
    main()
