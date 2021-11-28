class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        minimum = 10 ** 6
        maximum = -10 ** 6
        minIndex = 0
        maxIndex = 0
        for i, n in enumerate(nums):
            if n > maximum:
                maximum = n
                maxIndex = i
            if n < minimum:
                minimum = n
                minIndex = i
        
        # 3 ways to remove
        smallIndex = min(minIndex, maxIndex)
        bigIndex = max(minIndex, maxIndex)
        
        bestResult = len(nums)
        
        # remove from both front and back
        bestResult = min(bestResult, smallIndex + len(nums) - bigIndex + 1)
        
        # remove from front
        bestResult = min(bestResult, bigIndex + 1)
        
        # remove from back
        bestResult = min(bestResult, len(nums) - smallIndex)
        
        return bestResult
        