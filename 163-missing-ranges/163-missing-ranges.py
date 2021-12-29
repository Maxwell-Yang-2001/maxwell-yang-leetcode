class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        result = []
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 2:
                result.append(str(nums[i] + 1))
            elif nums[i + 1] > nums[i] + 2:
                result.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))
        return result
                