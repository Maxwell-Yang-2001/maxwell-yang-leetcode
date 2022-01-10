class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        currLen = 0
        longest = 0
        prev = nums[0] - 1
        for i in nums:
            if i > prev:
                currLen += 1
            else:
                longest = max(longest, currLen)
                currLen = 1
            prev = i
        
        return max(currLen, longest)