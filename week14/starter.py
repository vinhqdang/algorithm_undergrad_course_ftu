"""Week 14 Starter — Implement the functions then run for your score."""

def randomised_quicksort(*args, **kwargs):
    """Randomised quicksort. Return NEW sorted list. Expected O(n log n)."""
    # TODO: implement
    pass

def quickselect(*args, **kwargs):
    """Find k-th smallest element (1-indexed). Expected O(n)."""
    # TODO: implement
    pass

def monte_carlo_pi(*args, **kwargs):
    """Estimate pi using n Monte Carlo samples. Return float."""
    # TODO: implement
    pass

def reservoir_sampling(*args, **kwargs):
    """Reservoir sampling: pick k random elements from stream list. Return list of k items."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────
def _run_tests():
    total = 5
    passed = 0
    print("\nWeek 14 Tests")
    print("="*60)

    # Test 1
    try:
        result = eval("randomised_quicksort([5,2,4,6,1,3])", {"__builtins__": __builtins__}, globals())
        exp_val = [1,2,3,4,5,6]
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 1: randomised_quicksort([5,2,4,6,1,3])")
        else:
            print(f"  ✗ Test 1: randomised_quicksort([5,2,4,6,1,3])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 1: randomised_quicksort([5,2,4,6,1,3]) → ERROR: {e}")

    # Test 2
    try:
        result = eval("randomised_quicksort([])", {"__builtins__": __builtins__}, globals())
        exp_val = []
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 2: randomised_quicksort([])")
        else:
            print(f"  ✗ Test 2: randomised_quicksort([])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 2: randomised_quicksort([]) → ERROR: {e}")

    # Test 3
    try:
        result = eval("quickselect([3,1,4,1,5,9,2,6],3)", {"__builtins__": __builtins__}, globals())
        exp_val = 2
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 3: quickselect([3,1,4,1,5,9,2,6],3)")
        else:
            print(f"  ✗ Test 3: quickselect([3,1,4,1,5,9,2,6],3)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 3: quickselect([3,1,4,1,5,9,2,6],3) → ERROR: {e}")

    # Test 4
    try:
        result = eval("abs(monte_carlo_pi(100000)-3.14159) < 0.05", {"__builtins__": __builtins__}, globals())
        exp_val = True
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 4: abs(monte_carlo_pi(100000)-3.14159) < 0.05")
        else:
            print(f"  ✗ Test 4: abs(monte_carlo_pi(100000)-3.14159) < 0.05")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 4: abs(monte_carlo_pi(100000)-3.14159) < 0.05 → ERROR: {e}")

    # Test 5
    try:
        result = eval("len(reservoir_sampling(list(range(100)),10))", {"__builtins__": __builtins__}, globals())
        exp_val = 10
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 5: len(reservoir_sampling(list(range(100)),10))")
        else:
            print(f"  ✗ Test 5: len(reservoir_sampling(list(range(100)),10))")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 5: len(reservoir_sampling(list(range(100)),10)) → ERROR: {e}")

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
