"""
Week 1 Demo: Introduction to Algorithms & Efficiency
=====================================================
Run this file to see live comparisons of algorithm efficiencies.
"""

import time
import math
import random
import sys
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────────────────────
# DEMO 1: Linear Search vs Binary Search
# ─────────────────────────────────────────────────────────────────────────────

def linear_search(arr, target):
    """O(n) search — checks each element sequentially."""
    comparisons = 0
    for i, x in enumerate(arr):
        comparisons += 1
        if x == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, target):
    """O(log n) search — exploits sorted order to halve search space."""
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    while lo <= hi:
        comparisons += 1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comparisons


def demo_search_comparison():
    print("=" * 60)
    print("DEMO 1: Linear Search vs Binary Search")
    print("=" * 60)
    sizes = [100, 1_000, 10_000, 100_000, 1_000_000]
    print(f"{'n':>10} {'Linear (worst)':>16} {'Binary (worst)':>16} {'Speedup':>10}")
    print("-" * 56)
    for n in sizes:
        arr = list(range(n))
        # Worst case: target not in array
        _, lin = linear_search(arr, n + 1)
        _, bin_ = binary_search(arr, n + 1)
        print(f"{n:>10,} {lin:>16,} {bin_:>16,} {lin/bin_:>10.1f}x")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# DEMO 2: Insertion Sort — counting operations
# ─────────────────────────────────────────────────────────────────────────────

def insertion_sort(arr):
    """O(n²) sorting — good for small or nearly-sorted arrays."""
    arr = arr[:]
    comparisons = 0
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            comparisons += 1
            arr[i + 1] = arr[i]
            i -= 1
        if i >= 0:
            comparisons += 1          # the failed while condition
        arr[i + 1] = key
    return arr, comparisons


def demo_insertion_sort():
    print("=" * 60)
    print("DEMO 2: Insertion Sort — Best, Average, Worst Case")
    print("=" * 60)
    n = 20
    best  = list(range(n))
    worst = list(range(n, 0, -1))
    avg   = random.sample(range(n), n)

    _, c_best  = insertion_sort(best)
    _, c_worst = insertion_sort(worst)
    _, c_avg   = insertion_sort(avg)

    print(f"n = {n}")
    print(f"  Best case  (sorted):          {c_best:>5} comparisons  ≈ {n-1}")
    print(f"  Worst case (reverse sorted):  {c_worst:>5} comparisons  ≈ {n*(n-1)//2}")
    print(f"  Average case (random):        {c_avg:>5} comparisons")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# DEMO 3: Growth Rate Visualisation
# ─────────────────────────────────────────────────────────────────────────────

def demo_growth_rates():
    print("=" * 60)
    print("DEMO 3: Growth Rates at Different Scales")
    print("=" * 60)
    n_values = [10, 50, 100, 500, 1000]
    functions = {
        "log(n)":     lambda n: math.log2(n),
        "n":          lambda n: n,
        "n log(n)":   lambda n: n * math.log2(n),
        "n²":         lambda n: n ** 2,
        "n³":         lambda n: n ** 3,
    }
    header = f"{'n':>6} " + "".join(f"{k:>12}" for k in functions)
    print(header)
    print("-" * len(header))
    for n in n_values:
        row = f"{n:>6} "
        for fn in functions.values():
            val = fn(n)
            row += f"{val:>12.1f}"
        print(row)
    print()


# ─────────────────────────────────────────────────────────────────────────────
# DEMO 4: Fibonacci — Exponential vs Linear
# ─────────────────────────────────────────────────────────────────────────────

def fib_recursive(n, calls=[0]):
    calls[0] += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1, calls) + fib_recursive(n - 2, calls)


def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def demo_fibonacci():
    print("=" * 60)
    print("DEMO 4: Fibonacci — Recursive O(2ⁿ) vs Iterative O(n)")
    print("=" * 60)
    for n in [5, 10, 20, 30, 35]:
        # Recursive
        calls = [0]
        t0 = time.perf_counter()
        val_r = fib_recursive(n, calls)
        t_rec = time.perf_counter() - t0

        # Iterative
        t0 = time.perf_counter()
        val_i = fib_iterative(n)
        t_iter = time.perf_counter() - t0

        print(f"  fib({n:2d}) = {val_r:10,}  |  "
              f"Recursive: {calls[0]:8,} calls {t_rec*1000:8.3f} ms  |  "
              f"Iterative: {t_iter*1_000_000:.2f} µs")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# DEMO 5: Timing experiments — plotting
# ─────────────────────────────────────────────────────────────────────────────

def time_algorithm(func, inputs):
    """Time a function over a list of inputs, return list of durations."""
    times = []
    for inp in inputs:
        t0 = time.perf_counter()
        func(inp)
        times.append(time.perf_counter() - t0)
    return times


def demo_timing_plot():
    print("=" * 60)
    print("DEMO 5: Timing Insertion Sort on Different Input Sizes")
    print("=" * 60)
    sizes = list(range(100, 3001, 200))

    times_worst = []
    times_best  = []

    for n in sizes:
        worst = list(range(n, 0, -1))
        best  = list(range(n))

        t0 = time.perf_counter()
        insertion_sort(worst)
        times_worst.append(time.perf_counter() - t0)

        t0 = time.perf_counter()
        insertion_sort(best)
        times_best.append(time.perf_counter() - t0)

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times_worst, 'r-o', markersize=4, label='Worst case (reverse sorted)')
    plt.plot(sizes, times_best,  'g-s', markersize=4, label='Best case (sorted)')
    plt.xlabel('Input size n')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort: Best vs Worst Case Running Time')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('week01_timing.png', dpi=120)
    print("  Plot saved to week01_timing.png")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║  WEEK 1 DEMO: Algorithms & Efficiency                   ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    demo_search_comparison()
    demo_insertion_sort()
    demo_growth_rates()
    demo_fibonacci()
    demo_timing_plot()

    print("All demos complete!")
