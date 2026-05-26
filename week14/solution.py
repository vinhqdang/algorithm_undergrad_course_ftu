"""Week 14 SOLUTION — Do not distribute before deadline."""
import math, heapq, random

# Randomised quicksort. Return NEW sorted list. Expected O(n log n).
def randomised_quicksort(arr):
    import random
    a=list(arr)
    def qs(lo,hi):
        if lo>=hi: return
        ri=random.randint(lo,hi);a[ri],a[hi]=a[hi],a[ri]
        p=a[hi];i=lo-1
        for j in range(lo,hi):
            if a[j]<=p: i+=1;a[i],a[j]=a[j],a[i]
        a[i+1],a[hi]=a[hi],a[i+1];m=i+1
        qs(lo,m-1);qs(m+1,hi)
    qs(0,len(a)-1);return a

# Find k-th smallest element (1-indexed). Expected O(n).
def quickselect(arr,k):
    import random
    a=list(arr);lo,hi=0,len(a)-1;k-=1
    while lo<=hi:
        ri=random.randint(lo,hi);a[ri],a[hi]=a[hi],a[ri]
        p=a[hi];i=lo-1
        for j in range(lo,hi):
            if a[j]<=p: i+=1;a[i],a[j]=a[j],a[i]
        a[i+1],a[hi]=a[hi],a[i+1];m=i+1
        if m==k: return a[m]
        elif m<k: lo=m+1
        else: hi=m-1
    return a[lo]

# Estimate pi using n Monte Carlo samples. Return float.
def monte_carlo_pi(n):
    import random
    inside=sum(1 for _ in range(n) if random.random()**2+random.random()**2<=1)
    return 4*inside/n

# Reservoir sampling: pick k random elements from stream list. Return list of k items.
def reservoir_sampling(stream,k):
    import random
    reservoir=stream[:k]
    for i in range(k,len(stream)):
        j=random.randint(0,i)
        if j<k: reservoir[j]=stream[i]
    return reservoir

if __name__=="__main__": print("Solution loaded.")
