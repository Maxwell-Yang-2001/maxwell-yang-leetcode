class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}
        curr_sum = 0
        result = 0
        for i in nums:
            curr_sum += i
            diff = curr_sum - k
            if diff in sum_dict:
                result += sum_dict[diff]
            if curr_sum in sum_dict:
                sum_dict[curr_sum] += 1
            else:
                sum_dict[curr_sum] = 1
        
        return result