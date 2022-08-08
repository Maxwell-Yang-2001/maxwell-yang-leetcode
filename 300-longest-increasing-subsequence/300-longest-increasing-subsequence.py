class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for i in nums:
            pos = bisect_left(seq, i)
            
            if pos == len(seq):
                seq.append(i)
            else:
                seq[pos] = i
        
        return len(seq)