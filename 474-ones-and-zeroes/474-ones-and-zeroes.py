class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for s in strs:
            zero_count = one_count = 0
            for c in s:
                if c == '0':
                    zero_count += 1
                else:
                    one_count += 1
            for zeroes in range(m, zero_count - 1, -1):
                for ones in range(n, one_count - 1, -1):
                    dp[zeroes][ones] = max(1 + dp[zeroes - zero_count][ones - one_count], dp[zeroes][ones])
        return dp[m][n]

                