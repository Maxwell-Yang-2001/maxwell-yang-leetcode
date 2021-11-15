class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minimum = 0
        sum = 0
        for num in nums:
            if num < minimum:
                sum += (minimum - num)
                minimum += 1
            else:
                minimum = num + 1
        
        return sum