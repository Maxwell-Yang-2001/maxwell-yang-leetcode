class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        mem = [[1, 1] for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                mem[i][0] = mem[i - 1][1] + 1
                mem[i][1] = mem[i - 1][1]
            elif nums[i] < nums[i - 1]:
                mem[i][0] = mem[i - 1][0]
                mem[i][1] = mem[i - 1][0] + 1
            else:
                mem[i] = mem[i - 1]
        return max(mem[-1])
                