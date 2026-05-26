"""Week 2 Demo: Asymptotic Notation & Empirical Complexity"""
import time, math, random
import matplotlib.pyplot as plt

def demo_growth_comparison():
    """Visually compare growth rates."""
    ns = list(range(1, 51))
    funcs = {
        "log n":    lambda n: math.log2(max(n,1)),
        "sqrt(n)":  lambda n: math.sqrt(n),
        "n":        lambda n: n,
        "n log n":  lambda n: n * math.log2(max(n,1)),
        "n^2":      lambda n: n**2,
    }
    plt.figure(figsize=(9,5))
    for label, fn in funcs.items():
        plt.plot(ns, [fn(n) for n in ns], label=label, linewidth=2)
    plt.legend(); plt.xlabel("n"); plt.ylabel("f(n)")
    plt.title("Growth Rate Comparison"); plt.grid(True, alpha=0.3)
    plt.savefig("week02_growth.png", dpi=120); plt.close()
    print("Saved week02_growth.png")

def demo_big_o_proof():
    """Visually show 2n^2+3n+1 = Theta(n^2)."""
    ns = range(1, 30)
    f   = [2*n**2 + 3*n + 1 for n in ns]
    lo  = [2*n**2 for n in ns]          # c1=2
    hi  = [6*n**2 for n in ns]          # c2=6
    plt.figure(figsize=(7,4))
    plt.plot(ns, f,  'b-', label='f(n)=2n²+3n+1', linewidth=2)
    plt.plot(ns, lo, 'g--', label='c₁·n²=2n²')
    plt.plot(ns, hi, 'r--', label='c₂·n²=6n²')
    plt.fill_between(ns, lo, hi, alpha=0.1, color='green')
    plt.legend(); plt.xlabel("n"); plt.title("Theta proof: c₁g ≤ f ≤ c₂g")
    plt.grid(True, alpha=0.3); plt.savefig("week02_theta.png", dpi=120); plt.close()
    print("Saved week02_theta.png")

def empirical_complexity_test():
    """Measure actual running times and fit to find empirical complexity."""
    def alg_on(n):
        arr = list(range(n, 0, -1))
        # simple insertion sort O(n^2)
        for j in range(1, len(arr)):
            key = arr[j]; i = j-1
            while i >= 0 and arr[i] > key:
                arr[i+1] = arr[i]; i -= 1
            arr[i+1] = key
    
    sizes  = [100, 200, 400, 800, 1600]
    times  = []
    for n in sizes:
        t0 = time.perf_counter()
        for _ in range(5): alg_on(n)
        times.append((time.perf_counter()-t0)/5)
    
    print("\nEmpirical Complexity (Insertion Sort, worst case):")
    print(f"{'n':>6}  {'time (ms)':>10}  {'time/n^2 (ns)':>15}")
    for n, t in zip(sizes, times):
        print(f"{n:>6}  {t*1000:>10.3f}  {t/n**2*1e9:>15.4f}")
    print("→ time/n² is roughly constant → O(n²) confirmed")

if __name__ == "__main__":
    demo_growth_comparison()
    demo_big_o_proof()
    empirical_complexity_test()
