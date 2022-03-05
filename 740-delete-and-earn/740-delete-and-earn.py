class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_dict = dict()
        for n in nums:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1
        
        num_list = list(num_dict)
        num_list.sort()
        
        l = len(num_list)
        
        # dp[a][0] is best sum at a if earning a
        # dp[a][1] is best sum at a if not earning a
        dp = [[0] * 2 for i in range(l)]
        
        dp[l - 1][0] = num_list[l - 1] * num_dict[num_list[l - 1]]
        
        for i in range(l - 2, -1, -1):
            curr_earnings = num_list[i] * num_dict[num_list[i]]
            max_after_earnings = max(dp[i + 1][0], dp[i + 1][1])
            # connected
            if num_list[i] + 1 == num_list[i + 1]:
                dp[i][0] = dp[i + 1][1] + curr_earnings
            else:
                dp[i][0] = curr_earnings + max_after_earnings
            dp[i][1] = max_after_earnings
        
        return max(dp[0][0], dp[0][1])