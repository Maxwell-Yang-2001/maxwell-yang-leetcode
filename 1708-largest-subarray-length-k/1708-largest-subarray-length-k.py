class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        largestI = 0
        largestNum = 0
        for i in range(len(nums) - k + 1):
            if nums[i] > largestNum:
                largestNum, largestI = nums[i], i
        return nums[largestI:largestI+k]