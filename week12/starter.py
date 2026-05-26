"""Week 12 Starter — Implement the functions then run for your score."""

def kmp_failure(*args, **kwargs):
    """Build KMP failure function (prefix function) for pattern. Return list."""
    # TODO: implement
    pass

def kmp_search(*args, **kwargs):
    """KMP pattern matching. Return list of start indices."""
    # TODO: implement
    pass

def rabin_karp(*args, **kwargs):
    """Rabin-Karp pattern matching using rolling hash. Return list of indices."""
    # TODO: implement
    pass

def ford_fulkerson(*args, **kwargs):
    """Ford-Fulkerson max flow. cap=2D capacity list, src,sink. Return max flow."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────

def _run_tests():
    total_pts = 0
    earned_pts = 0
    print(f"\nWeek Tests")
    print("="*60)
    print("  Run each function and verify output manually.")
    print("  Functions defined:", [name for name in dir() if not name.startswith('_')])
    print("─"*60)
    print("  To test: call each function with sample inputs.")
    print("  See exercises.md for problem descriptions.")
    print("  See solution.py after the deadline for answers.")
    print("="*60+"\n")

if __name__ == "__main__":
    _run_tests()
