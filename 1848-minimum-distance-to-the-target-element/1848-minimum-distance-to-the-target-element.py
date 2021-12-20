class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        best = 1000
        i = start
        while i >= 0:
            if nums[i] == target:
                best = start - i
                break
            i -= 1
        i = start + 1
        while i < len(nums):
            if nums[i] == target:
                best = min(best, i - start)
                break
            i += 1
        return best