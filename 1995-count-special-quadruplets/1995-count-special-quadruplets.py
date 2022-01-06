class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        sumDict = dict()
        for i in range(3, len(nums)):
            if nums[i] in sumDict:
                sumDict[nums[i]].insert(0, i)
            else:
                sumDict[nums[i]] = [i]
        
        result = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums) - 1):
                    s = nums[i] + nums[j] + nums[k]
                    if s in sumDict:
                        for sumIndex in sumDict[s]:
                            if sumIndex > k:
                                result += 1
        return result
                    