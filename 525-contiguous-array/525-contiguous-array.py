class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        num_dict = dict()
        
        counter = 0
        num_dict[counter] = (-1, 0)
        for i, n in enumerate(nums):
            if n == 1:
                counter += 1
            else:
                counter -= 1
            
            if counter in num_dict:
                num_dict[counter] = (num_dict[counter][0], i + 1)
            else:
                num_dict[counter] = (i, i + 1)
        
        result = 0
        for interval in num_dict.values():
            result = max(interval[1] - interval[0] - 1, result)
        
        return result