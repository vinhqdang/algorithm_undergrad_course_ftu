"""
Week 2 — Starter Code with Auto-Grader
Implement the functions, then run to see your score.
"""
import math

# ── Problem 1 (20 pts): Classify complexity ───────────────────────────────────
def classify_complexity(expression: str) -> str:
    """
    Given a string describing a function, return its Theta class.
    Supported inputs: 'n^2 + n', '3*n*log(n)', '2^n + n^5', 'n^3/3 + 100'
    Return one of: 'O(1)', 'O(log n)', 'O(n)', 'O(n log n)',
                   'O(n^2)', 'O(n^3)', 'O(2^n)', 'O(n!)'
    Hint: think about which term dominates.
    Map:
      '5n^2 + 3n + 1'  ->  'O(n^2)'
      'n*log(n) + n'   ->  'O(n log n)'
      '2^n + n^5'      ->  'O(2^n)'
      'log(n) + 1'     ->  'O(log n)'
    """
    # TODO: implement (use simple if/elif matching on the string or compute)
    pass


# ── Problem 2 (25 pts): Big-O verifier ───────────────────────────────────────
def verify_big_o(f_values: list, g_values: list) -> dict:
    """
    Given two lists of function values at n=1,2,...,len(f_values),
    empirically check if f(n) = O(g(n)).

    Return dict:
      {
        'is_O': True/False,       # True if ratio f/g is bounded
        'max_ratio': float,       # max f(n)/g(n) for all n
        'c_estimate': float       # estimated constant c
      }

    Consider f = O(g) if f(n)/g(n) stays bounded (< 100) for all n.
    Handle g(n) == 0 gracefully.
    """
    # TODO: implement
    pass


# ── Problem 3 (25 pts): Recurrence Solver (Master Theorem) ───────────────────
def master_theorem(a: int, b: int, k: int) -> str:
    """
    Apply the Master Theorem to T(n) = a*T(n/b) + O(n^k).
    a >= 1, b > 1, k >= 0.

    Return the Theta bound as a string:
      'Theta(n^log_b(a))'  -- Case 1: log_b(a) > k
      'Theta(n^k log n)'   -- Case 2: log_b(a) == k
      'Theta(n^k)'         -- Case 3: log_b(a) < k

    Examples:
      master_theorem(4, 2, 1) -> 'Theta(n^2)'      [log2(4)=2 > 1]
      master_theorem(2, 2, 1) -> 'Theta(n log n)'  [log2(2)=1 == 1]
      master_theorem(2, 4, 1) -> 'Theta(n)'        [log4(2)=0.5 < 1]
    """
    # TODO: implement
    pass


# ── Problem 4 (30 pts): Empirical Complexity Detector ─────────────────────────
def detect_complexity(times: list, sizes: list) -> str:
    """
    Given measured running times for input sizes, detect the likely
    complexity class by fitting ratios.

    times[i] = measured time for sizes[i]
    sizes must be powers of 2: [8, 16, 32, 64, 128, 256]

    When size doubles, time multiplies by:
      O(1):       1x
      O(log n):   ~1 (very slowly)
      O(n):       2x
      O(n log n): ~2.1x
      O(n^2):     4x
      O(n^3):     8x

    Return one of: 'O(1)', 'O(log n)', 'O(n)', 'O(n log n)', 'O(n^2)', 'O(n^3)'
    """
    # TODO: compute ratios between consecutive measurements and classify
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# AUTO-GRADER
# ═══════════════════════════════════════════════════════════════════════════════
def _run_tests():
    score = 0; results = []

    # P1: classify_complexity
    p1 = 0
    try:
        cases = [
            ('5*n^2 + 3*n + 1', 'O(n^2)'),
            ('n*log(n) + n',    'O(n log n)'),
            ('2^n + n^5',       'O(2^n)'),
            ('log(n) + 1',      'O(log n)'),
            ('100',             'O(1)'),
        ]
        for expr, expected in cases:
            got = classify_complexity(expr)
            assert got == expected, f"classify_complexity('{expr}') = {got!r}, expected {expected!r}"
        p1 = 20; results.append(("P1 – classify_complexity", "PASS", 20, 20))
    except Exception as e:
        results.append(("P1 – classify_complexity", f"FAIL: {e}", 0, 20))
    score += p1

    # P2: verify_big_o
    p2 = 0
    try:
        import math
        n_vals = list(range(1,21))
        f_n2 = [n**2 for n in n_vals]
        g_n2 = [n**2 for n in n_vals]
        r = verify_big_o(f_n2, g_n2)
        assert r['is_O'] == True
        assert abs(r['max_ratio'] - 1.0) < 0.01

        f_n  = [n for n in n_vals]
        g_n3 = [n**3 for n in n_vals]
        r2 = verify_big_o(f_n, g_n3)
        assert r2['is_O'] == True   # n = O(n^3)

        f_n3 = [n**3 for n in n_vals]
        g_n  = [n for n in n_vals]
        r3 = verify_big_o(f_n3, g_n)
        assert r3['is_O'] == False  # n^3 != O(n)

        p2 = 25; results.append(("P2 – verify_big_o", "PASS", 25, 25))
    except Exception as e:
        results.append(("P2 – verify_big_o", f"FAIL: {e}", 0, 25))
    score += p2

    # P3: master_theorem
    p3 = 0
    try:
        assert master_theorem(4, 2, 1) == 'Theta(n^2)',     "case 1"
        assert master_theorem(2, 2, 1) == 'Theta(n log n)', "case 2"
        assert master_theorem(2, 4, 1) == 'Theta(n)',       "case 3"
        assert master_theorem(1, 2, 0) == 'Theta(log n)' or master_theorem(1,2,0) == 'Theta(n^0 log n)', "T=T/2+1"
        assert master_theorem(8, 2, 2) == 'Theta(n^3)',     "n^log2(8)=n^3 > n^2"
        p3 = 25; results.append(("P3 – master_theorem", "PASS", 25, 25))
    except Exception as e:
        results.append(("P3 – master_theorem", f"FAIL: {e}", 0, 25))
    score += p3

    # P4: detect_complexity
    p4 = 0
    try:
        # O(n): times double when sizes double
        sizes = [8,16,32,64,128,256]
        times_n   = [s * 1.0 for s in sizes]
        times_n2  = [s**2 * 1.0 for s in sizes]
        times_n3  = [s**3 * 1.0 for s in sizes]
        times_log = [math.log2(s) for s in sizes]
        assert detect_complexity(times_n,  sizes) == 'O(n)',   "linear"
        assert detect_complexity(times_n2, sizes) == 'O(n^2)', "quadratic"
        assert detect_complexity(times_n3, sizes) == 'O(n^3)', "cubic"
        p4 = 30; results.append(("P4 – detect_complexity", "PASS", 30, 30))
    except Exception as e:
        results.append(("P4 – detect_complexity", f"FAIL: {e}", 0, 30))
    score += p4

    print("\n" + "═"*62)
    print("  WEEK 2 AUTO-GRADER RESULTS")
    print("═"*62)
    for name, status, pts, mx in results:
        mark = "✓" if "PASS" in status else "✗"
        print(f"  {mark} {name:<38} {pts:>3}/{mx}")
        if "FAIL" in status: print(f"      → {status[5:]}")
    print("─"*62)
    print(f"  TOTAL SCORE: {score}/100  ({score}%)")
    print("═"*62+"\n")

if __name__ == "__main__":
    _run_tests()
