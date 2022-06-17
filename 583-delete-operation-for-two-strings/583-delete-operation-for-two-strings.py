class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (1 + len(word2))
        tmp = [0] * (1 + len(word2))
        for i in range(1 + len(word1)):
            for j in range(1 + len(word2)):
                if i == 0 or j == 0:
                    tmp[j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    tmp[j] = dp[j - 1]
                else:
                    tmp[j] = 1 + min(dp[j], tmp[j - 1])
            dp, tmp = tmp, dp
        return dp[-1]