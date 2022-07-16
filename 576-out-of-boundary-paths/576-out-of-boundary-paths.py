class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0]* n for i in range(m)]
        next_dp = [[0] * n for i in range(m)]
        
        result = 0
        dp[startRow][startColumn] = 1
        for i in range(maxMove):
            for i in range(m):
                for j in range(n):
                    # up
                    if i > 0:
                        next_dp[i - 1][j] += dp[i][j]
                    else:
                        result += dp[i][j]
                    # down
                    if i < m - 1:
                        next_dp[i + 1][j] += dp[i][j]
                    else:
                        result += dp[i][j]
                    # left
                    if j > 0:
                        next_dp[i][j - 1] += dp[i][j]
                    else:
                        result += dp[i][j]
                    # down
                    if j < n - 1:
                        next_dp[i][j + 1] += dp[i][j]
                    else:
                        result += dp[i][j]
            tmp = next_dp
            next_dp = dp
            dp = tmp
            for i in range(m):
                for j in range(n):
                    next_dp[i][j] = 0
        
        return(result % (10**9 + 7))