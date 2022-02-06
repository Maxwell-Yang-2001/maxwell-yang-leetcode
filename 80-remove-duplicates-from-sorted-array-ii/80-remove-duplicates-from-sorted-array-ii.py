class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dst = 0
        prev, freq = nums[0] - 1, 0
        for src in range(len(nums)):
            if nums[src] == prev:
                freq += 1
            else:
                prev = nums[src]
                freq = 1
            if freq <= 2:
                nums[dst] = prev
                dst += 1
        return dst
        