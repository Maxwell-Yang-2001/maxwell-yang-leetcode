class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        multiplier = 10 ** 5 + 1
        envelopes.sort(key=lambda n: n[0] * multiplier - n[1])
        
        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([i[1] for i in envelopes])
                