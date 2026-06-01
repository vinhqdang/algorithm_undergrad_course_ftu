"""
Week 3 Demo: Divide and Conquer Algorithms Visualization
=========================================================
Demonstrates and visualizes key Divide and Conquer algorithms:
  1. Bubble Sort (Quadratic Benchmark) vs. Merge Sort & Quick Sort
  2. Maximum Subarray Sum (Split and Crossing Visual)
  3. Divide & Conquer Recurrence Complexity Curves (Master Theorem Cases)

Generates beautiful visualization plots and saves them as PNGs.
"""
import time
import math
import random
import matplotlib.pyplot as plt

# ── Import reference solutions ───────────────────────────────────────────────
try:
    from week03.solution import (
        merge_sort,
        quicksort,
        count_inversions,
        binary_search_rec,
        max_subarray_dc
    )
except ImportError:
    # Fallback in case of local execution import differences
    from solution import (
        merge_sort,
        quicksort,
        count_inversions,
        binary_search_rec,
        max_subarray_dc
    )

# ── 1. BUBBLE SORT BENCHMARK ──────────────────────────────────────────────────

def bubble_sort(arr):
    n = len(arr)
    res = list(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    return res

# ── 2. SORTING BENCHMARK SIMULATION ──────────────────────────────────────────

def run_sorting_comparison_visual():
    print("\n--- 1. Sorting Algorithms Benchmark & Visualizing ---")
    sizes = [50, 100, 200, 400, 800, 1200]
    bubble_times = []
    merge_times = []
    quick_times = []
    
    print(f"{'Size (n)':^10} | {'Bubble Sort (ms)':^18} | {'Merge Sort (ms)':^18} | {'Quick Sort (ms)':^18}")
    print("-" * 72)
    
    for n in sizes:
        # Generate random array
        arr = [random.randint(1, 10000) for _ in range(n)]
        
        # Benchmark Bubble Sort
        t0 = time.perf_counter()
        _ = bubble_sort(arr)
        t_bubble = (time.perf_counter() - t0) * 1000
        bubble_times.append(t_bubble)
        
        # Benchmark Merge Sort
        t0 = time.perf_counter()
        _ = merge_sort(arr)
        t_merge = (time.perf_counter() - t0) * 1000
        merge_times.append(t_merge)
        
        # Benchmark Quick Sort (in-place, so we copy first)
        arr_copy = list(arr)
        t0 = time.perf_counter()
        _ = quicksort(arr_copy)
        t_quick = (time.perf_counter() - t0) * 1000
        quick_times.append(t_quick)
        
        print(f"{n:^10} | {t_bubble:^18.2f} | {t_merge:^18.2f} | {t_quick:^18.2f}")
        
    # Generate visual plot
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, bubble_times, 'o--', color='#EF4444', label='Bubble Sort (O(n^2))', linewidth=1.8)
    plt.plot(sizes, merge_times, 's-', color='#10B981', label='Merge Sort (O(n log n))', linewidth=2.2)
    plt.plot(sizes, quick_times, '^:', color='#3B82F6', label='Quick Sort (Average O(n log n))', linewidth=2.2)
    
    plt.xlabel("Input Size (n)", fontweight='bold')
    plt.ylabel("Time (milliseconds)", fontweight='bold')
    plt.title("Quadratic Sort vs. Divide and Conquer Sorts Performance Comparison", fontsize=11, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig("week03/dc_sorting_comparison.png", dpi=150)
    plt.close()
    print("Saved visual: week03/dc_sorting_comparison.png")

# ── 3. MAXIMUM SUBARRAY SUM VISUALIZATION ─────────────────────────────────────

def run_max_subarray_visual():
    print("\n--- 2. Maximum Subarray Sum Visualizing ---")
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_dc(arr)
    
    # We know the maximum subarray is [4, -1, 2, 1] starting at index 3 and ending at index 6
    start_idx, end_idx = 3, 6
    print(f"Input Array: {arr}")
    print(f"Maximum Contiguous Subarray Sum: {max_sum} (Subarray indices: {start_idx} to {end_idx})")
    
    # Visualization setup
    plt.figure(figsize=(9, 4.5))
    colors = ['#E2E8F0'] * len(arr) # default soft gray-blue
    for idx in range(start_idx, end_idx + 1):
        colors[idx] = '#3B82F6' # Vibrant blue for the max subarray window
        
    bars = plt.bar(range(len(arr)), arr, color=colors, edgecolor='#475569', width=0.6)
    
    # Annotate bar values
    for idx, rect in enumerate(bars):
        height = rect.get_height()
        va_dir = 'bottom' if height >= 0 else 'top'
        offset = 0.15 if height >= 0 else -0.4
        plt.text(rect.get_x() + rect.get_width()/2.0, height + offset, f"{arr[idx]}",
                 ha='center', va=va_dir, fontweight='bold', 
                 color='#1E293B' if (idx < start_idx or idx > end_idx) else '#1E3A8A')

    plt.axvspan(start_idx - 0.4, end_idx + 0.4, color='#EFF6FF', alpha=0.4, label='Max Subarray Window')
    plt.xlabel("Array Index", fontweight='bold')
    plt.ylabel("Value", fontweight='bold')
    plt.title(f"Maximum Contiguous Subarray Sum (Divide & Conquer) | Max Sum = {max_sum}", fontsize=11, fontweight='bold')
    plt.xticks(range(len(arr)))
    plt.axhline(0, color='black', linewidth=0.8, alpha=0.7)
    plt.grid(True, axis='y', linestyle=':', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig("week03/max_subarray_visualization.png", dpi=150)
    plt.close()
    print("Saved visual: week03/max_subarray_visualization.png")

# ── 4. RECURRENCE COMPLEXITY CURVES ───────────────────────────────────────────

def run_recurrence_curves_visual():
    print("\n--- 3. Recurrence Complexity Curves (Master Theorem) ---")
    ns = list(range(1, 101))
    
    funcs = {
        "log n (e.g. Binary Search)":               lambda n: math.log2(n),
        "n (e.g. Linear Scan)":                     lambda n: n,
        "n log n (e.g. Merge / Quick Sort)":        lambda n: n * math.log2(n) if n > 1 else 0,
        "n^2.81 (e.g. Strassen's Matrix Mult)":    lambda n: n**2.807,
        "n^3 (e.g. Naive Matrix Mult)":             lambda n: n**3
    }
    
    plt.figure(figsize=(9, 5))
    for label, fn in funcs.items():
        plt.plot(ns, [fn(n) for n in ns], label=label, linewidth=2)
        
    plt.yscale('log')
    plt.xlabel("Input Size (n)", fontweight='bold')
    plt.ylabel("Operations count (log scale)", fontweight='bold')
    plt.title("D&C Growth Complexity Classes (Master Theorem Cases)", fontsize=11, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("week03/recurrence_curves.png", dpi=150)
    plt.close()
    print("Saved visual: week03/recurrence_curves.png")


# ── MAIN RUNNER ───────────────────────────────────────────────────────────────

def main():
    print("======================================================")
    print("  WEEK 3 DIVIDE AND CONQUER VISUAL RUNTIME DEMO")
    print("======================================================")
    
    # 1. Simple algorithms check
    print("\n--- Basic D&C Solvers Smoke Tests ---")
    arr = [4, 1, 9, 3, 5]
    print(f"Unsorted arr: {arr}")
    print(f"Sorted using merge_sort: {merge_sort(arr)}")
    print(f"Total array inversions: {count_inversions(arr)}")
    
    # 2. Simulations and Visualizations
    run_sorting_comparison_visual()
    run_max_subarray_visual()
    run_recurrence_curves_visual()
    
    print("\n" + "=" * 54)
    print("  WEEK 3 DEMO COMPLETED. ALL VISUAL ASSETS GENERATED.")
    print("=" * 54)

if __name__ == "__main__":
    main()
