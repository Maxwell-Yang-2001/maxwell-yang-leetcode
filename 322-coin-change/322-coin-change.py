class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                possible_min = dp[i - coin] + 1
                if possible_min == 0:
                    continue
                dp[i] = possible_min if (dp[i] == -1 or dp[i] > possible_min) else dp[i]
        
        return dp[amount]
                    