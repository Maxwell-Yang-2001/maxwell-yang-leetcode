class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                curr, count = num, 1
                
                while curr + 1 in num_set:
                    curr += 1
                    count += 1
                
                highest = max(highest, count)
        
        return highest