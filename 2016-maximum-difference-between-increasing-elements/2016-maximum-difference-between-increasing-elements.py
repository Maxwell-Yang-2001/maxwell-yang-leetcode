class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = 0
        minSoFar = nums[0]
        
        for i in nums:
            diff = i - minSoFar
            if diff < 0:
                minSoFar = i
            elif diff > maxDiff:
                maxDiff = diff
        
        return maxDiff if maxDiff > 0 else -1