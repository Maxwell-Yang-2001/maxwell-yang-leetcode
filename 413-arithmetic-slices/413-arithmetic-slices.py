class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        prevDiff = 3000
        currentCount = 0
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff == prevDiff:
                currentCount += 1
            else:
                result += currentCount * (currentCount - 1) // 2
                currentCount = 1
                prevDiff = diff
                
        result += currentCount * (currentCount - 1) // 2
        return result