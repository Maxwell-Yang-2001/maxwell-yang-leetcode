class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        prev = nums[0]
        index = -1
        # should only have at most 1 decreasing pattern
        for i, n in enumerate(nums):
            if nums[i] < prev:
                if index >= 0:
                    return False
                index = i - 1
            prev = nums[i]
        
        # all non-decreasing
        if index == -1:
            return True
    
        # try to either remove nums[index] or nums[index + 1]
        if index == 0 or nums[index - 1] <= nums[index + 1]:
            return True
        
        if index >= len(nums) - 2 or nums[index] <= nums[index + 2]:
            return True
        
        return False
            