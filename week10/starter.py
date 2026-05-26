"""Week 10 Starter — Implement the functions then run for your score."""

def bfs(*args, **kwargs):
    """BFS traversal. graph={node:[neighbors]}, start. Return visited order."""
    # TODO: implement
    pass

def dfs(*args, **kwargs):
    """DFS traversal iterative. graph={node:[neighbors]}, start. Return visited order."""
    # TODO: implement
    pass

def bellman_ford(*args, **kwargs):
    """Bellman-Ford. edges=[(u,v,w)], n, src. Return dist dict or 'NEGATIVE CYCLE'."""
    # TODO: implement
    pass

def has_cycle_directed(*args, **kwargs):
    """Detect cycle in directed graph using DFS coloring. Return bool."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────
def _run_tests():
    total = 5
    passed = 0
    print("\nWeek 10 Tests")
    print("="*60)

    # Test 1
    try:
        result = eval("bfs({0:[1,2],1:[0,3],2:[0,3],3:[1,2]},0)", {"__builtins__": __builtins__}, globals())
        exp_val = [0,1,2,3]
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 1: bfs({0:[1,2],1:[0,3],2:[0,3],3:[1,2]},0)")
        else:
            print(f"  ✗ Test 1: bfs({0:[1,2],1:[0,3],2:[0,3],3:[1,2]},0)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 1: bfs({0:[1,2],1:[0,3],2:[0,3],3:[1,2]},0) → ERROR: {e}")

    # Test 2
    try:
        result = eval("dfs({0:[1,2],1:[3],2:[3],3:[]},0)", {"__builtins__": __builtins__}, globals())
        exp_val = [0,1,3,2]
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 2: dfs({0:[1,2],1:[3],2:[3],3:[]},0)")
        else:
            print(f"  ✗ Test 2: dfs({0:[1,2],1:[3],2:[3],3:[]},0)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 2: dfs({0:[1,2],1:[3],2:[3],3:[]},0) → ERROR: {e}")

    # Test 3
    try:
        result = eval("bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3]", {"__builtins__": __builtins__}, globals())
        exp_val = 4
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 3: bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3]")
        else:
            print(f"  ✗ Test 3: bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3]")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 3: bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3] → ERROR: {e}")

    # Test 4
    try:
        result = eval("has_cycle_directed({0:[1],1:[2],2:[0]})", {"__builtins__": __builtins__}, globals())
        exp_val = True
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 4: has_cycle_directed({0:[1],1:[2],2:[0]})")
        else:
            print(f"  ✗ Test 4: has_cycle_directed({0:[1],1:[2],2:[0]})")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 4: has_cycle_directed({0:[1],1:[2],2:[0]}) → ERROR: {e}")

    # Test 5
    try:
        result = eval("has_cycle_directed({0:[1],1:[2],2:[3],3:[]})", {"__builtins__": __builtins__}, globals())
        exp_val = False
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 5: has_cycle_directed({0:[1],1:[2],2:[3],3:[]})")
        else:
            print(f"  ✗ Test 5: has_cycle_directed({0:[1],1:[2],2:[3],3:[]})")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 5: has_cycle_directed({0:[1],1:[2],2:[3],3:[]}) → ERROR: {e}")

    score = int(passed/total*100)
    print("─"*60)
    print(f"  SCORE: {passed}/{total} tests passed = {score}%")
    if score==100: print("  🎉 Perfect!")
    elif score>=70: print("  👍 Good progress!")
    else: print("  💪 Keep going!")
    print("="*60+"\n")
    return score

if __name__ == "__main__":
    _run_tests()
