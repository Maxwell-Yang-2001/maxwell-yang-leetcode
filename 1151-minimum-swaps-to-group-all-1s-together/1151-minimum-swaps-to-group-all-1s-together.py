class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        curr_one = max_one = 0
        
        for i in range(ones):
            curr_one += data[i]
        max_one = curr_one
        
        for i in range(ones, len(data)):
            curr_one += (data[i] - data[i - ones])
            max_one = max(curr_one, max_one)
        
        return ones - max_one
        
        