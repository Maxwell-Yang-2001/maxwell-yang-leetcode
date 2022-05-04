from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dict = defaultdict(lambda: 0)
        for n in nums:
            num_dict[n] += 1
        num_list = list(num_dict)
        
        result = 0
        mid = k // 2
        # deal with the edge case for even number
        if mid * 2 == k and num_dict[mid]:
            result -= ceil(num_dict[mid] / 2)
        for i in num_list:
            if i <= mid:
                result += min(num_dict[i], num_dict[k - i])
        
        return result