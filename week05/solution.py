"""Week 5 SOLUTION — Do not distribute before deadline."""
import math, heapq, random

# Max non-overlapping activities. Input: list of (start,end). Return list of selected indices.
def activity_selection(activities):
    acts=sorted(enumerate(activities),key=lambda x:x[1][1])
    sel=[acts[0][0]];last=acts[0][1][1]
    for i,(s,e) in acts[1:]:
        if s>=last: sel.append(i);last=e
    return sorted(sel)

# Fractional knapsack. items=[(weight,value)], capacity. Return max float value.
def fractional_knapsack(items,capacity):
    si=sorted(items,key=lambda x:x[1]/x[0] if x[0]>0 else 0,reverse=True)
    total=0.0;rem=capacity
    for w,v in si:
        if rem<=0: break
        take=min(w,rem);total+=take*(v/w);rem-=take
    return total

# Greedy coin change. Return list of coins used (sorted desc).
def coin_change_greedy(amount,coins):
    coins=sorted(coins,reverse=True)
    result=[]
    for c in coins:
        while amount>=c: result.append(c);amount-=c
    return result if amount==0 else []

# Min train platforms needed. arrivals,departures as sorted lists.
def min_platforms(arrivals,departures):
    arr=sorted(arrivals);dep=sorted(departures)
    plat=1;res=1;i=1;j=0
    while i<len(arr) and j<len(dep):
        if arr[i]<=dep[j]: plat+=1;i+=1
        else: plat-=1;j+=1
        res=max(res,plat)
    return res

if __name__=="__main__": print("Solution loaded.")
