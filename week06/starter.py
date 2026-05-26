"""Week 6 Starter — Implement the functions then run for your score."""

def dijkstra(*args, **kwargs):
    """Dijkstra's algorithm. graph={node:[(neighbor,weight)]}, src. Return {node:dist}."""
    # TODO: implement
    pass

def kruskal_mst(*args, **kwargs):
    """Kruskal MST. edges=[(u,v,w)], n=nodes. Return (edges,total_weight)."""
    # TODO: implement
    pass

def prim_mst(*args, **kwargs):
    """Prim's MST. graph={node:[(neighbor,weight)]}. Return total weight."""
    # TODO: implement
    pass

def bellman_ford(*args, **kwargs):
    """Bellman-Ford. edges=[(u,v,w)], n=nodes, src. Return dist dict or 'NEGATIVE CYCLE'."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────
def _run_tests():
    total = 5
    passed = 0
    print("\nWeek 6 Tests")
    print("="*60)

    # Test 1
    try:
        result = eval("dijkstra({0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]},0)[3]", {"__builtins__": __builtins__}, globals())
        exp_val = 4
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 1: dijkstra({0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]},0)[3]")
        else:
            print(f"  ✗ Test 1: dijkstra({0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]},0)[3]")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 1: dijkstra({0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]},0)[3] → ERROR: {e}")

    # Test 2
    try:
        result = eval("kruskal_mst([(0,1,4),(0,2,3),(1,2,1),(1,3,2),(2,3,4)],4)[1]", {"__builtins__": __builtins__}, globals())
        exp_val = 6
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 2: kruskal_mst([(0,1,4),(0,2,3),(1,2,1),(1,3,2),(2,3,4)],4)[1]")
        else:
            print(f"  ✗ Test 2: kruskal_mst([(0,1,4),(0,2,3),(1,2,1),(1,3,2),(2,3,4)],4)[1]")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 2: kruskal_mst([(0,1,4),(0,2,3),(1,2,1),(1,3,2),(2,3,4)],4)[1] → ERROR: {e}")

    # Test 3
    try:
        result = eval("prim_mst({0:[(1,4),(2,3)],1:[(0,4),(2,1),(3,2)],2:[(0,3),(1,1),(3,4)],3:[(1,2),(2,4)]})", {"__builtins__": __builtins__}, globals())
        exp_val = 6
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 3: prim_mst({0:[(1,4),(2,3)],1:[(0,4),(2,1),(3,2)],2:[(0,3),(1,1),(3,4)],3:[(1,2),(2,4)]})")
        else:
            print(f"  ✗ Test 3: prim_mst({0:[(1,4),(2,3)],1:[(0,4),(2,1),(3,2)],2:[(0,3),(1,1),(3,4)],3:[(1,2),(2,4)]})")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 3: prim_mst({0:[(1,4),(2,3)],1:[(0,4),(2,1),(3,2)],2:[(0,3),(1,1),(3,4)],3:[(1,2),(2,4)]}) → ERROR: {e}")

    # Test 4
    try:
        result = eval("bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3]", {"__builtins__": __builtins__}, globals())
        exp_val = 4
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 4: bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3]")
        else:
            print(f"  ✗ Test 4: bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3]")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 4: bellman_ford([(0,1,4),(0,2,1),(2,1,2),(1,3,1)],4,0)[3] → ERROR: {e}")

    # Test 5
    try:
        result = eval("bellman_ford([(0,1,1),(1,2,-1),(2,0,-1)],3,0)", {"__builtins__": __builtins__}, globals())
        exp_val = 'NEGATIVE CYCLE'
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 5: bellman_ford([(0,1,1),(1,2,-1),(2,0,-1)],3,0)")
        else:
            print(f"  ✗ Test 5: bellman_ford([(0,1,1),(1,2,-1),(2,0,-1)],3,0)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 5: bellman_ford([(0,1,1),(1,2,-1),(2,0,-1)],3,0) → ERROR: {e}")

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
