class Solution:
    def integerBreak(self, n: int) -> int:
        dp = dp = [1] * (n + 1)
        for i in range(2,n+1):
            if i!=n:
                dp[i]=i
            for j in range(1,i):
                dp[i]=max(dp[i],dp[i-j] * j)
        return dp[n]