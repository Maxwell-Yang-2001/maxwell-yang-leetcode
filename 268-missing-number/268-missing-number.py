class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n * (n + 1) // 2
        for i in nums:
            result -= i
        
        return result