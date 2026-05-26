"""Week 13 Starter — Implement the functions then run for your score."""

def z_function(*args, **kwargs):
    """Compute Z-function of string. z[i]=length of longest substring starting at i that is a prefix."""
    # TODO: implement
    pass

def vertex_cover_approx(*args, **kwargs):
    """2-approx vertex cover. graph={node:set_of_neighbors}. Return cover set."""
    # TODO: implement
    pass

def tsp_nearest_neighbor(*args, **kwargs):
    """TSP nearest neighbor heuristic. cities=list of (x,y). Return tour length."""
    # TODO: implement
    pass

def string_match_z(*args, **kwargs):
    """Find all occurrences of pattern in text using Z-algorithm. Return indices."""
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
