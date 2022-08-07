class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp: list of 5 numbers, representing numbers of permutations starting with a, e, i, o or u
        vowel_count = 5
        dp = [1] * vowel_count
        new_dp = [0] * vowel_count
        
        for i in range(n - 1):
            # a:
            new_dp[0] = dp[1]
            new_dp[1] = dp[0] + dp[2]
            new_dp[2] = dp[0] + dp[1] + dp[3] + dp[4]
            new_dp[3] = dp[2] + dp[4]
            new_dp[4] = dp[0]
        
            dp, new_dp = new_dp, dp
        
        return sum(dp) % (10 ** 9 + 7)
            
                
        