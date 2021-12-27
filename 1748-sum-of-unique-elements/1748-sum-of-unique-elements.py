class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        occur = dict()
        result = 0
        for n in nums:
            if n not in occur:
                occur[n] = True
                result += n
            elif occur[n]:
                occur[n] = False
                result -= n
        return result