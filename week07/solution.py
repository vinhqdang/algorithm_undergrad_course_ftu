"""Week 7 SOLUTION — Do not distribute before deadline."""
import math, heapq, random

# Fibonacci using memoisation. O(n) time.
def fibonacci_dp(n,memo={}):
    if n in memo: return memo[n]
    if n<=1: return n
    memo[n]=fibonacci_dp(n-1,memo)+fibonacci_dp(n-2,memo)
    return memo[n]

# 0/1 knapsack DP. weights,values,capacity. Return max value.
def knapsack_01(weights,values,capacity):
    n=len(weights)
    dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(capacity+1):
            dp[i][w]=dp[i-1][w]
            if weights[i-1]<=w:
                dp[i][w]=max(dp[i][w],dp[i-1][w-weights[i-1]]+values[i-1])
    return dp[n][capacity]

# LCS length of two strings.
def lcs_length(s,t):
    m,n=len(s),len(t)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]: dp[i][j]=dp[i-1][j-1]+1
            else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

# Return actual LCS string.
def lcs_string(s,t):
    m,n=len(s),len(t)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]: dp[i][j]=dp[i-1][j-1]+1
            else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    res='';i,j=m,n
    while i>0 and j>0:
        if s[i-1]==t[j-1]: res=s[i-1]+res;i-=1;j-=1
        elif dp[i-1][j]>dp[i][j-1]: i-=1
        else: j-=1
    return res

if __name__=="__main__": print("Solution loaded.")
