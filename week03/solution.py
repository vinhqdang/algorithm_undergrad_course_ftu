"""
Week 3 SOLUTION — Reference implementations for the 5 classic Divide and Conquer algorithms.
Do not distribute to students before the deadline.
"""

# ── 1. MERGE SORT ─────────────────────────────────────────────────────────────

def merge_sort(arr: list) -> list:
    """
    Sorts a list in ascending order using Merge Sort.
    Returns: a NEW sorted list (does not mutate the input array).
    Stability: Preserves relative order of equal elements.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: # <= preserves stability
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result.extend(L[i:])
    result.extend(R[j:])
    return result

# ── 2. QUICK SORT (IN-PLACE) ──────────────────────────────────────────────────

def quicksort(arr: list, lo: int = 0, hi: int = None) -> list:
    """
    Sorts a list in ascending order in-place using Quick Sort.
    Input:
      arr: list of elements to be sorted (mutated in-place)
      lo: starting index (default: 0)
      hi: ending index (default: len(arr) - 1)
    Returns:
      the sorted list reference.
    Time Complexity: O(n log n) average, O(n^2) worst case
    Space Complexity: O(log n) call stack space
    """
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = _partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)
    return arr

def _partition(arr: list, lo: int, hi: int) -> int:
    """Helper Lomuto partition function."""
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

# ── 3. INVERSION COUNTING ─────────────────────────────────────────────────────

def count_inversions(arr: list) -> int:
    """
    Counts the number of inversions in an array in O(n log n) time.
    An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].
    Returns: integer inversion count.
    """
    def merge_and_count(a):
        if len(a) <= 1:
            return list(a), 0
        mid = len(a) // 2
        L, left_count = merge_and_count(a[:mid])
        R, right_count = merge_and_count(a[mid:])
        
        merged = []
        cross_count = left_count + right_count
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                merged.append(L[i])
                i += 1
            else:
                merged.append(R[j])
                # Since L is sorted, if L[i] > R[j], then all remaining elements
                # in L (from index i to the end) form inversions with R[j].
                cross_count += len(L) - i
                j += 1
        merged.extend(L[i:])
        merged.extend(R[j:])
        return merged, cross_count

    _, total_inversions = merge_and_count(arr)
    return total_inversions

# ── 4. RECURSIVE BINARY SEARCH ────────────────────────────────────────────────

def binary_search_rec(arr: list, target, lo: int = 0, hi: int = None) -> int:
    """
    Recursively searches for a target in a sorted list.
    Returns: the 0-indexed position of target if found, else -1.
    Time Complexity: O(log n)
    Space Complexity: O(log n) recursion stack
    """
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, hi)
    else:
        return binary_search_rec(arr, target, lo, mid - 1)

# ── 5. MAXIMUM SUBARRAY SUM ───────────────────────────────────────────────────

def max_subarray_dc(arr: list) -> int:
    """
    Finds the contiguous subarray within arr which has the largest sum.
    Solves using a Divide and Conquer approach in O(n log n) time.
    Returns: integer max subarray sum. Returns 0 if arr is empty.
    """
    if not arr:
        return 0

    def find_max_subarray(a, lo, hi):
        if lo == hi:
            return a[lo]
        mid = (lo + hi) // 2
        
        # Left and Right max subarray sums recursively
        left_max = find_max_subarray(a, lo, mid)
        right_max = find_max_subarray(a, mid + 1, hi)
        
        # Cross max subarray sum: must cross the mid boundary
        # Find maximum sum starting at mid and going left
        left_sum = -float('inf')
        current_sum = 0
        for i in range(mid, lo - 1, -1):
            current_sum += a[i]
            left_sum = max(left_sum, current_sum)
            
        # Find maximum sum starting at mid+1 and going right
        right_sum = -float('inf')
        current_sum = 0
        for i in range(mid + 1, hi + 1):
            current_sum += a[i]
            right_sum = max(right_sum, current_sum)
            
        cross_max = left_sum + right_sum
        return max(left_max, right_max, cross_max)

    return find_max_subarray(arr, 0, len(arr) - 1)

# ── Self-check tests ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 1. Merge Sort
    orig = [5, 2, 4, 6, 1, 3]
    res1 = merge_sort(orig)
    assert res1 == [1, 2, 3, 4, 5, 6]
    assert orig == [5, 2, 4, 6, 1, 3], "merge_sort modified the input array!"
    
    # 2. Quick Sort
    orig2 = [5, 2, 4, 6, 1, 3]
    res2 = quicksort(orig2)
    assert res2 == [1, 2, 3, 4, 5, 6]
    assert orig2 == [1, 2, 3, 4, 5, 6], "quicksort failed to sort in-place!"
    
    # 3. Inversion Counting
    assert count_inversions([2, 1, 3]) == 1
    assert count_inversions([3, 2, 1]) == 3
    assert count_inversions([1, 2, 3]) == 0
    assert count_inversions([1, 3, 5, 2, 4, 6]) == 3 # Inversions: (3,2), (5,2), (5,4)
    
    # 4. Recursive Binary Search
    arr = [1, 2, 3, 4, 5]
    assert binary_search_rec(arr, 3) == 2
    assert binary_search_rec(arr, 6) == -1
    assert binary_search_rec(arr, 1) == 0
    assert binary_search_rec(arr, 5) == 4
    
    # 5. Maximum Subarray Sum
    assert max_subarray_dc([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6 # [4, -1, 2, 1]
    assert max_subarray_dc([5, 4, -1, 7, 8]) == 23
    assert max_subarray_dc([-1, -2, -3]) == -1
    
    print("All reference solutions and self-checks passed successfully.")
