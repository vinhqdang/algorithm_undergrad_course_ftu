"""Week 3 SOLUTION — Do not distribute before deadline."""
import math, heapq, random

# Sort list using merge sort. Return NEW sorted list. O(n log n).
def merge_sort(arr):
    if len(arr)<=1: return list(arr)
    m=len(arr)//2
    L,R=merge_sort(arr[:m]),merge_sort(arr[m:])
    res,i,j=[],0,0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]: res.append(L[i]);i+=1
        else: res.append(R[j]);j+=1
    return res+L[i:]+R[j:]

# Count inversions using modified merge sort. O(n log n).
def count_inversions(arr):
    def sc(a):
        if len(a)<=1: return list(a),0
        m=len(a)//2
        L,lc=sc(a[:m]);R,rc=sc(a[m:])
        merged,cnt,i,j=[],lc+rc,0,0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]: merged.append(L[i]);i+=1
            else: merged.append(R[j]);cnt+=len(L)-i;j+=1
        return merged+L[i:]+R[j:],cnt
    _,c=sc(arr);return c

# Recursive binary search on sorted array. Return index or -1.
def binary_search_rec(arr,target,lo=0,hi=None):
    if hi is None: hi=len(arr)-1
    if lo>hi: return -1
    mid=(lo+hi)//2
    if arr[mid]==target: return mid
    elif arr[mid]<target: return binary_search_rec(arr,target,mid+1,hi)
    else: return binary_search_rec(arr,target,lo,mid-1)

# Max subarray sum using D&C. O(n log n).
def max_subarray_dc(arr):
    def f(a,lo,hi):
        if lo==hi: return a[lo]
        mid=(lo+hi)//2
        lm,rm=f(a,lo,mid),f(a,mid+1,hi)
        ls=a[mid];cur=a[mid]
        for i in range(mid-1,lo-1,-1): cur+=a[i];ls=max(ls,cur)
        rs=a[mid+1];cur=a[mid+1]
        for i in range(mid+2,hi+1): cur+=a[i];rs=max(rs,cur)
        return max(lm,rm,ls+rs)
    return f(arr,0,len(arr)-1) if arr else 0

if __name__=="__main__": print("Solution loaded.")
