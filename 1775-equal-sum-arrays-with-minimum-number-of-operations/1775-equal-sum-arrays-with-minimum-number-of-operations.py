class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:        
        diff = 0
        freq1 = [0] * 7
        freq2 = [0] * 7
        for n in nums1:
            diff += n
            freq1[n] += 1
        for n in nums2:
            diff -= n
            freq2[n] += 1
        
        # make sure nums1 is the one with a higher sum
        if diff <= 0:
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
            diff = -diff
            tmp = freq1
            freq1 = freq2
            freq2 = tmp
        
        # freq is a list of potential additions to be used
        freq = [0] * 6
        
        for i in range(6):
            freq[i] += freq1[i + 1] + freq2[6 - i]
        
        result = 0
        # start with biggest additions
        for i in range(5, -1, -1):
            if i * freq[i] < diff:
                result += freq[i]
                diff -= i * freq[i]
            else:
                return result + ceil(diff / i)
        return -1
        
        
        
        