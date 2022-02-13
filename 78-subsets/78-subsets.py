class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[] for i in range(2**len(nums))]
        for i, n in enumerate(nums):
            for j in range(2**i, 2**(i+1)):
                result[j] = result[j - 2**i].copy()
                result[j].append(n)
        
        return result