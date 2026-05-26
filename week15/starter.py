"""Week 15 Starter — Implement the functions then run for your score."""

def simulated_annealing(*args, **kwargs):
    """SA for maximising f(x) on interval [a,b]. Return best x found."""
    # TODO: implement
    pass

def genetic_algorithm_onemax(*args, **kwargs):
    """GA for OneMax (maximise 1-bits in bitstring of length n). Return best fitness."""
    # TODO: implement
    pass

def hill_climbing(*args, **kwargs):
    """Hill climbing for f maximisation. f=callable, x0=start, step=0.1. Return best x found."""
    # TODO: implement
    pass

def particle_swarm_1d(*args, **kwargs):
    """1D Particle Swarm Optimisation to minimise f. Return best position."""
    # TODO: implement
    pass


# ── AUTO-GRADER ───────────────────────────────────────────────────────────────
def _run_tests():
    total = 4
    passed = 0
    print("\nWeek 15 Tests")
    print("="*60)

    # Test 1
    try:
        result = eval("abs(simulated_annealing(lambda x: -(x-3)**2, 0, -10, 10) - 3) < 1", {"__builtins__": __builtins__}, globals())
        exp_val = True
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 1: abs(simulated_annealing(lambda x: -(x-3)**2, 0, -10, 10) - 3) < 1")
        else:
            print(f"  ✗ Test 1: abs(simulated_annealing(lambda x: -(x-3)**2, 0, -10, 10) - 3) < 1")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 1: abs(simulated_annealing(lambda x: -(x-3)**2, 0, -10, 10) - 3) < 1 → ERROR: {e}")

    # Test 2
    try:
        result = eval("genetic_algorithm_onemax(20) >= 15", {"__builtins__": __builtins__}, globals())
        exp_val = True
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 2: genetic_algorithm_onemax(20) >= 15")
        else:
            print(f"  ✗ Test 2: genetic_algorithm_onemax(20) >= 15")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 2: genetic_algorithm_onemax(20) >= 15 → ERROR: {e}")

    # Test 3
    try:
        result = eval("abs(hill_climbing(lambda x: -(x**2), 1) - 0) < 0.2", {"__builtins__": __builtins__}, globals())
        exp_val = True
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 3: abs(hill_climbing(lambda x: -(x**2), 1) - 0) < 0.2")
        else:
            print(f"  ✗ Test 3: abs(hill_climbing(lambda x: -(x**2), 1) - 0) < 0.2")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 3: abs(hill_climbing(lambda x: -(x**2), 1) - 0) < 0.2 → ERROR: {e}")

    # Test 4
    try:
        result = eval("abs(particle_swarm_1d(lambda x: (x-2)**2, -10, 10) - 2) < 0.5", {"__builtins__": __builtins__}, globals())
        exp_val = True
        if result == exp_val or (isinstance(exp_val, bool) and exp_val):
            passed += 1
            print(f"  ✓ Test 4: abs(particle_swarm_1d(lambda x: (x-2)**2, -10, 10) - 2) < 0.5")
        else:
            print(f"  ✗ Test 4: abs(particle_swarm_1d(lambda x: (x-2)**2, -10, 10) - 2) < 0.5")
            print(f"    Expected: {exp_val}, Got: {result}")
    except Exception as e:
        print(f"  ✗ Test 4: abs(particle_swarm_1d(lambda x: (x-2)**2, -10, 10) - 2) < 0.5 → ERROR: {e}")

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
