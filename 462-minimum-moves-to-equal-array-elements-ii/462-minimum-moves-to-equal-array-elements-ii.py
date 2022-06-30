class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        
        result = 0
        for num in nums:
            result += abs(median - num)
        return result
        