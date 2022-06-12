class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        end = 0
        num_set = set()
        l_nums = len(nums)
        curr_sum = max_sum = 0
        while l_nums != end and nums[end] not in num_set:
            num_set.add(nums[end])
            curr_sum += nums[end]
            end += 1
        
        max_sum = curr_sum
        
        # if the whole array has only unique elements
        if l_nums == end:
            return max_sum
        
        end -= 1
        
        start = 0
        
        for end in range(end + 1, l_nums):
            if nums[end] not in num_set:
                num_set.add(nums[end])
                curr_sum += nums[end]
                max_sum = max(curr_sum, max_sum)
                continue
            
            while nums[start] != nums[end]:
                num_set.remove(nums[start])
                curr_sum -= nums[start]
                start += 1
            start += 1
        return max_sum
        
        
            
            