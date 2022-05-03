class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = nums.copy()
        sorted_nums.sort()
        
        start = len(nums)
        end = 0
        
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
        
        return max(end - start + 1, 0)
            