"""Week 8 Demo — Week 8
Run this file to see demonstrations of the algorithms.
"""

# Length of Longest Increasing Subsequence. O(n^2) DP.
def lis_length(arr):
    if not arr: return 0
    n=len(arr);dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i]: dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

# Levenshtein edit distance between two strings.
def edit_distance(s,t):
    m,n=len(s),len(t)
    dp=list(range(n+1))
    for i in range(1,m+1):
        prev=dp[0];dp[0]=i
        for j in range(1,n+1):
            temp=dp[j]
            if s[i-1]==t[j-1]: dp[j]=prev
            else: dp[j]=1+min(prev,dp[j],dp[j-1])
            prev=temp
    return dp[n]

# Coin change DP. Return min coins or -1.
def coin_change_dp(coins,amount):
    dp=[float('inf')]*(amount+1);dp[0]=0
    for a in range(1,amount+1):
        for c in coins:
            if c<=a: dp[a]=min(dp[a],dp[a-c]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

# Matrix chain multiplication min cost. dims=[d0,d1,...,dn].
def matrix_chain(dims):
    n=len(dims)-1
    dp=[[0]*n for _ in range(n)]
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1;dp[i][j]=float('inf')
            for k in range(i,j):
                cost=dp[i][k]+dp[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                dp[i][j]=min(dp[i][j],cost)
    return dp[0][n-1]


def main():
    print("Week 8 Demo")
    print("="*50)
    # Demonstration runs
    print("All functions defined. See starter.py for exercises.")

if __name__ == "__main__":
    main()
