"""Week 9 Demo — Week 9
Run this file to see demonstrations of the algorithms.
"""

# Longest palindromic subsequence length.
def longest_palindrome_subseq(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    for i in range(n): dp[i][i]=1
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2 if length>2 else 2
            else: dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    return dp[0][n-1]

# Word break DP. Return True if s can be segmented using wordDict.
def word_break(s,wordDict):
    wset=set(wordDict);n=len(s)
    dp=[False]*(n+1);dp[0]=True
    for i in range(1,n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wset: dp[i]=True;break
    return dp[n]

# Count unique paths in m x n grid (right or down only).
def unique_paths(m,n):
    dp=[[1]*n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]

# Best time buy/sell stock with at most k transactions.
def max_profit_stock(prices,k):
    n=len(prices)
    if n<=1 or k==0: return 0
    if k>=n//2:
        return sum(max(prices[i+1]-prices[i],0) for i in range(n-1))
    dp=[[0]*n for _ in range(k+1)]
    for t in range(1,k+1):
        max_so_far=-prices[0]
        for d in range(1,n):
            dp[t][d]=max(dp[t][d-1],prices[d]+max_so_far)
            max_so_far=max(max_so_far,dp[t-1][d]-prices[d])
    return dp[k][n-1]


def main():
    print("Week 9 Demo")
    print("="*50)
    # Demonstration runs
    print("All functions defined. See starter.py for exercises.")

if __name__ == "__main__":
    main()
