class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in map:
                return [map[remaining], i]
            else:
                map[num] = i