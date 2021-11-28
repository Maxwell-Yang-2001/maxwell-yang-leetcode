import bisect

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        list.sort(nums)
        first = bisect.bisect_left(nums, target)
        
        if first == len(nums) or target != nums[first]:
            return []
        else:
            result = []
            for i in range(first, len(nums)):
                if nums[i] == target:
                    result.append(i)
            return result
            