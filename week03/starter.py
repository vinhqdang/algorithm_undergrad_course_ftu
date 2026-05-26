"""Week 3 Starter — Implement the functions then run for your score."""

def merge_sort(*args, **kwargs):
    """Sort list using merge sort. Return NEW sorted list. O(n log n)."""
    # TODO: implement
    pass

def count_inversions(*args, **kwargs):
    """Count inversions using modified merge sort. O(n log n)."""
    # TODO: implement
    pass

def binary_search_rec(*args, **kwargs):
    """Recursive binary search on sorted array. Return index or -1."""
    # TODO: implement
    pass

def max_subarray_dc(*args, **kwargs):
    """Max subarray sum using D&C. O(n log n)."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────
def _run_tests():
    total = 7
    passed = 0
    print("\nWeek 3 Tests")
    print("="*60)

    # Test 1
    try:
        result = eval("merge_sort([5,2,4,6,1,3])", {"__builtins__": __builtins__}, globals())
        exp_val = [1,2,3,4,5,6]
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 1: merge_sort([5,2,4,6,1,3])")
        else:
            print(f"  ✗ Test 1: merge_sort([5,2,4,6,1,3])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 1: merge_sort([5,2,4,6,1,3]) → ERROR: {e}")

    # Test 2
    try:
        result = eval("merge_sort([])", {"__builtins__": __builtins__}, globals())
        exp_val = []
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 2: merge_sort([])")
        else:
            print(f"  ✗ Test 2: merge_sort([])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 2: merge_sort([]) → ERROR: {e}")

    # Test 3
    try:
        result = eval("count_inversions([2,1,3])", {"__builtins__": __builtins__}, globals())
        exp_val = 1
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 3: count_inversions([2,1,3])")
        else:
            print(f"  ✗ Test 3: count_inversions([2,1,3])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 3: count_inversions([2,1,3]) → ERROR: {e}")

    # Test 4
    try:
        result = eval("count_inversions([3,2,1])", {"__builtins__": __builtins__}, globals())
        exp_val = 3
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 4: count_inversions([3,2,1])")
        else:
            print(f"  ✗ Test 4: count_inversions([3,2,1])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 4: count_inversions([3,2,1]) → ERROR: {e}")

    # Test 5
    try:
        result = eval("binary_search_rec([1,2,3,4,5],3)", {"__builtins__": __builtins__}, globals())
        exp_val = 2
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 5: binary_search_rec([1,2,3,4,5],3)")
        else:
            print(f"  ✗ Test 5: binary_search_rec([1,2,3,4,5],3)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 5: binary_search_rec([1,2,3,4,5],3) → ERROR: {e}")

    # Test 6
    try:
        result = eval("binary_search_rec([1,2,3,4,5],6)", {"__builtins__": __builtins__}, globals())
        exp_val = -1
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 6: binary_search_rec([1,2,3,4,5],6)")
        else:
            print(f"  ✗ Test 6: binary_search_rec([1,2,3,4,5],6)")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 6: binary_search_rec([1,2,3,4,5],6) → ERROR: {e}")

    # Test 7
    try:
        result = eval("max_subarray_dc([-2,1,-3,4,-1,2,1,-5,4])", {"__builtins__": __builtins__}, globals())
        exp_val = 6
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 7: max_subarray_dc([-2,1,-3,4,-1,2,1,-5,4])")
        else:
            print(f"  ✗ Test 7: max_subarray_dc([-2,1,-3,4,-1,2,1,-5,4])")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 7: max_subarray_dc([-2,1,-3,4,-1,2,1,-5,4]) → ERROR: {e}")

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
