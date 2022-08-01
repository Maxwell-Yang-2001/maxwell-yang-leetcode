class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # minize dp size (possible due to synmmetry of the question)
        if m < n:
            m, n = n, m
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        
        return dp[-1]
        
        