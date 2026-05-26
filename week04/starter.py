"""Week 4 Starter — Implement the functions then run for your score."""

def quick_sort(*args, **kwargs):
    """Quicksort with random pivot. Return NEW sorted list."""
    # TODO: implement
    pass

def power_dc(*args, **kwargs):
    """a^n in O(log n) using fast exponentiation."""
    # TODO: implement
    pass

def find_peak_element(*args, **kwargs):
    """Find peak element index in O(log n)."""
    # TODO: implement
    pass

def karatsuba(*args, **kwargs):
    """Karatsuba multiplication. O(n^1.585)."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────
def _run_tests():
    total = 6
    passed = 0
    print("\nWeek 4 Tests")
    print("="*60)

    # Test 1
    try:
        result = eval("quick_sort([5,2,4,6,1,3])", {"__builtins__": __builtins__}, globals())
        exp_val = [1,2,3,4,5,6]
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 1: quick_sort([5,2,4,6,1,3])")
        else:
            print(f"  ✗ Test 1: quick_sort([5,2,4,6,1,3])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 1: quick_sort([5,2,4,6,1,3]) → ERROR: {e}")

    # Test 2
    try:
        result = eval("quick_sort([])", {"__builtins__": __builtins__}, globals())
        exp_val = []
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 2: quick_sort([])")
        else:
            print(f"  ✗ Test 2: quick_sort([])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 2: quick_sort([]) → ERROR: {e}")

    # Test 3
    try:
        result = eval("power_dc(2,10)", {"__builtins__": __builtins__}, globals())
        exp_val = 1024
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 3: power_dc(2,10)")
        else:
            print(f"  ✗ Test 3: power_dc(2,10)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 3: power_dc(2,10) → ERROR: {e}")

    # Test 4
    try:
        result = eval("power_dc(3,0)", {"__builtins__": __builtins__}, globals())
        exp_val = 1
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 4: power_dc(3,0)")
        else:
            print(f"  ✗ Test 4: power_dc(3,0)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 4: power_dc(3,0) → ERROR: {e}")

    # Test 5
    try:
        result = eval("find_peak_element([1,2,3,1])", {"__builtins__": __builtins__}, globals())
        exp_val = 2
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 5: find_peak_element([1,2,3,1])")
        else:
            print(f"  ✗ Test 5: find_peak_element([1,2,3,1])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 5: find_peak_element([1,2,3,1]) → ERROR: {e}")

    # Test 6
    try:
        result = eval("karatsuba(1234,5678)", {"__builtins__": __builtins__}, globals())
        exp_val = 7006652
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 6: karatsuba(1234,5678)")
        else:
            print(f"  ✗ Test 6: karatsuba(1234,5678)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 6: karatsuba(1234,5678) → ERROR: {e}")

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
