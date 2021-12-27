class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minVal = 101
        for n in nums:
            if n < minVal:
                minVal = n
                
        s = 0
        while minVal > 0:
            s += minVal % 10
            minVal //= 10
        
        return (s + 1) % 2