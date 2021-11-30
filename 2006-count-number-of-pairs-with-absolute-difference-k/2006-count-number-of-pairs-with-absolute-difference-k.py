class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        occurenceDict = dict()
        for n in nums:
            if n in occurenceDict:
                occurenceDict[n] += 1
            else:
                occurenceDict[n] = 1
        
        result = 0
        for i in occurenceDict:
            j = i + k
            if j <= 100 and j in occurenceDict:
                result += occurenceDict[i] * occurenceDict[j]
        
        return result
                