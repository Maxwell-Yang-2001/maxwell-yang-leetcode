class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(0, length - 3):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2] or nums[i] == nums[i + 3]:
                return nums[i]
        
        if nums[length - 3] == nums[length - 2] or nums[length - 3] == nums[length - 1]:
            return nums[length - 3]
        return nums[length - 2]