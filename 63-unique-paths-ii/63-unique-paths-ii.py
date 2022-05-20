class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = obstacleGrid
        if dp[0][0] == 1:
            return 0
        
        width, height = len(dp[0]), len(dp)
        
        dp[0][0] = 1
        
        # first row
        for i in range(1, width):
            dp[0][i] = int(dp[0][i - 1] == 1 and dp[0][i] == 0)
        
        # first col
        for i in range(1, height):
            dp[i][0] = int(dp[i - 1][0] == 1 and dp[i][0] == 0)
        
        # start with (1, 1), fill in row major
        
        for i in range(1, height):
            for j in range(1, width):
                if dp[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[height - 1][width - 1]