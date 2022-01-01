class Solution:
    
    def maxCoins(self, nums: List[int]) -> int:
        # stupid special case when all balloons have the same number and there are lots of balloons (at least 3)
        if len(nums) >= 3:
            prev = nums[0]
            same = True
            for b in nums:
                if b != prev:
                    same = False
                    break
            if same:
                return prev + prev * prev + prev * prev * prev * (len(nums) - 2)

        # set up dummy balloons for edge case. These cannot be popped
        nums.insert(0, 1)
        nums.append(1)
        return self.recur(nums, (1, len(nums) - 2), dict())
    
    # sub is inclusive range for popping, assuming the balloon to the left and right of sub would stay until sub is empty
    def recur(self, nums: List[int], sub: (int, int), mem) -> int:
        
        # top-down dp
        if sub in mem:
            return mem[sub]
        
        # edge case for recursion
        if sub[1] < sub[0]:
            return 0
        
        maxSum = 0
        # i is the last balloon to be popped in sub
        for i in range(sub[0], sub[1] + 1):
            lSum = self.recur(nums, (sub[0], i - 1), mem)
            rSum = self.recur(nums, (i + 1, sub[1]), mem)
            maxSum = max(maxSum, lSum + rSum + nums[sub[0] - 1] * nums[i] * nums[sub[1] + 1])
        
        mem[sub] = maxSum
        return maxSum
            
        