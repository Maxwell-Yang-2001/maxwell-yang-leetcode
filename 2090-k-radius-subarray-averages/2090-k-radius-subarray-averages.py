class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        # -1 for boundary cases
        result = [-1 for i in range(0, len(nums))]
        
        if (2 * k + 1 > len(nums)):
            return result
        
        currentSum = 0
        for i in range(0, 2 * k + 1):
            currentSum += nums[i]
            
        result[k] = currentSum // (2 * k + 1)
        
        for i in range(k + 1, len(nums) - k):
            currentSum += (nums[i + k] - nums[i - k - 1])
            result[i] = currentSum // (2 * k + 1)
        
        return result