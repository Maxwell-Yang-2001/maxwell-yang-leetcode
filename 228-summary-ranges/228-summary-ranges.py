class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        
        curr_start = nums[0]
        curr_end = nums[0]
        
        result = []
        for num in nums[1:]:
            if num == curr_end + 1:
                curr_end += 1
            else:
                result.append((str(curr_start) + '->' + str(curr_end)) if curr_start != curr_end else str(curr_start))
                curr_start = num
                curr_end = num
        
        result.append((str(curr_start) + '->' + str(curr_end)) if curr_start != curr_end else str(curr_start))
        return result