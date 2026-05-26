"""Week 2 SOLUTION"""
import math

def classify_complexity(expression: str) -> str:
    e = expression.lower().replace(' ','')
    if '2^n' in e or 'n!' in e: return 'O(2^n)' if '2^n' in e else 'O(n!)'
    if 'n^3' in e: return 'O(n^3)'
    if 'n^2' in e: return 'O(n^2)'
    if 'n*log' in e or 'nlog' in e or 'n log' in e: return 'O(n log n)'
    if re_has_n(e): return 'O(n)'
    if 'log' in e: return 'O(log n)'
    return 'O(1)'

def re_has_n(e):
    import re
    return bool(re.search(r'(?<!\^)\bn\b', e))

def verify_big_o(f_values, g_values):
    ratios = []
    for f, g in zip(f_values, g_values):
        if g == 0: continue
        ratios.append(f / g)
    if not ratios: return {'is_O': True, 'max_ratio': 0.0, 'c_estimate': 0.0}
    max_r = max(ratios)
    return {'is_O': max_r < 100, 'max_ratio': max_r, 'c_estimate': max_r}

def master_theorem(a, b, k):
    log_b_a = math.log(a) / math.log(b)
    if abs(log_b_a - k) < 1e-9:
        if k == 0: return 'Theta(log n)'
        return f'Theta(n^{k} log n)' if k != 1 else 'Theta(n log n)'
    elif log_b_a > k:
        exp = round(log_b_a, 6)
        exp_str = str(int(exp)) if exp == int(exp) else str(exp)
        return f'Theta(n^{exp_str})'
    else:
        return 'Theta(n)' if k == 1 else f'Theta(n^{k})'

def detect_complexity(times, sizes):
    ratios = [times[i+1]/times[i] for i in range(len(times)-1) if times[i] > 0]
    avg = sum(ratios)/len(ratios)
    if avg < 1.05: return 'O(1)'
    if avg < 1.2:  return 'O(log n)'
    if avg < 2.5:  return 'O(n)'
    if avg < 3.0:  return 'O(n log n)'
    if avg < 6.0:  return 'O(n^2)'
    return 'O(n^3)'

if __name__ == "__main__":
    assert classify_complexity('5*n^2 + 3*n + 1') == 'O(n^2)'
    assert master_theorem(2,2,1) == 'Theta(n log n)'
    assert detect_complexity([8,16,32,64,128,256],[8,16,32,64,128,256]) == 'O(n)'
    print("All solution checks passed.")
