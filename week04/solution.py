"""Week 4 SOLUTION — Do not distribute before deadline."""
import math, heapq, random

# Quicksort with random pivot. Return NEW sorted list.
def quick_sort(arr):
    import random
    a=list(arr)
    def qs(a,lo,hi):
        if lo>=hi: return
        ri=random.randint(lo,hi);a[ri],a[hi]=a[hi],a[ri]
        p=a[hi];i=lo-1
        for j in range(lo,hi):
            if a[j]<=p: i+=1;a[i],a[j]=a[j],a[i]
        a[i+1],a[hi]=a[hi],a[i+1];q=i+1
        qs(a,lo,q-1);qs(a,q+1,hi)
    qs(a,0,len(a)-1);return a

# a^n in O(log n) using fast exponentiation.
def power_dc(a,n):
    if n==0: return 1
    if n%2==0: h=power_dc(a,n//2);return h*h
    return a*power_dc(a,n-1)

# Find peak element index in O(log n).
def find_peak_element(arr):
    lo,hi=0,len(arr)-1
    while lo<hi:
        mid=(lo+hi)//2
        if arr[mid]<arr[mid+1]: lo=mid+1
        else: hi=mid
    return lo

# Karatsuba multiplication. O(n^1.585).
def karatsuba(x,y):
    if x<10 or y<10: return x*y
    n=max(len(str(x)),len(str(y)));m=n//2
    a,b=x//(10**m),x%(10**m);c,d=y//(10**m),y%(10**m)
    ac=karatsuba(a,c);bd=karatsuba(b,d)
    ad_bc=karatsuba(a+b,c+d)-ac-bd
    return ac*10**(2*m)+ad_bc*10**m+bd

if __name__=="__main__": print("Solution loaded.")
