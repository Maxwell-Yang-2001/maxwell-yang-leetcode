class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum += n
            nums[i] = curr_sum
        return nums