"""Week 11 Starter — Implement the functions then run for your score."""

def topological_sort(*args, **kwargs):
    """Topological sort of DAG. graph={node:[neighbors]}. Return sorted list."""
    # TODO: implement
    pass

def count_scc(*args, **kwargs):
    """Count strongly connected components (Kosaraju's). graph={node:[neighbors]}. Return count."""
    # TODO: implement
    pass

def prim_mst_weight(*args, **kwargs):
    """Prim MST total weight. graph={node:[(neighbor,weight)]}. Return int."""
    # TODO: implement
    pass

def is_bipartite(*args, **kwargs):
    """Check if graph is bipartite using BFS 2-coloring. Return bool."""
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
