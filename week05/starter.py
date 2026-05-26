"""Week 5 Starter — Implement the functions then run for your score."""

def activity_selection(*args, **kwargs):
    """Max non-overlapping activities. Input: list of (start,end). Return list of selected indices."""
    # TODO: implement
    pass

def fractional_knapsack(*args, **kwargs):
    """Fractional knapsack. items=[(weight,value)], capacity. Return max float value."""
    # TODO: implement
    pass

def coin_change_greedy(*args, **kwargs):
    """Greedy coin change. Return list of coins used (sorted desc)."""
    # TODO: implement
    pass

def min_platforms(*args, **kwargs):
    """Min train platforms needed. arrivals,departures as sorted lists."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────
def _run_tests():
    total = 4
    passed = 0
    print("\nWeek 5 Tests")
    print("="*60)

    # Test 1
    try:
        result = eval("activity_selection([(1,4),(3,5),(0,6),(5,7),(8,11),(8,12),(12,14)])", {"__builtins__": __builtins__}, globals())
        exp_val = [0,3,4,6]
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 1: activity_selection([(1,4),(3,5),(0,6),(5,7),(8,11),(8,12),(12,14)])")
        else:
            print(f"  ✗ Test 1: activity_selection([(1,4),(3,5),(0,6),(5,7),(8,11),(8,12),(12,14)])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 1: activity_selection([(1,4),(3,5),(0,6),(5,7),(8,11),(8,12),(12,14)]) → ERROR: {e}")

    # Test 2
    try:
        result = eval("fractional_knapsack([(10,60),(20,100),(30,120)],50)", {"__builtins__": __builtins__}, globals())
        exp_val = 240.0
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 2: fractional_knapsack([(10,60),(20,100),(30,120)],50)")
        else:
            print(f"  ✗ Test 2: fractional_knapsack([(10,60),(20,100),(30,120)],50)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 2: fractional_knapsack([(10,60),(20,100),(30,120)],50) → ERROR: {e}")

    # Test 3
    try:
        result = eval("coin_change_greedy(41,[25,10,5,1])", {"__builtins__": __builtins__}, globals())
        exp_val = [25,10,5,1]
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 3: coin_change_greedy(41,[25,10,5,1])")
        else:
            print(f"  ✗ Test 3: coin_change_greedy(41,[25,10,5,1])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 3: coin_change_greedy(41,[25,10,5,1]) → ERROR: {e}")

    # Test 4
    try:
        result = eval("min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000])", {"__builtins__": __builtins__}, globals())
        exp_val = 3
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 4: min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000])")
        else:
            print(f"  ✗ Test 4: min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 4: min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000]) → ERROR: {e}")

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
