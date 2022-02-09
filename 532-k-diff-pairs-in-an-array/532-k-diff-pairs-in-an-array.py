class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        if (k == 0):
            num_dict = dict()
            for i in nums:
                if i in num_dict:
                    if num_dict[i] == 1:
                        result += 1
                    num_dict[i] += 1
                else:
                    num_dict[i] = 1
            return result
        
        num_set = set()
        for i in nums:
            num_set.add(i)
        
        for n in num_set:
            if (n + k) in num_set:
                result += 1
        
        return result