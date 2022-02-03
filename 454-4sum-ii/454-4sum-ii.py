class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # sum up nums1, nums2 and nums3, nums4
        sum1 = dict()
        for i in nums1:
            for j in nums2:
                s = i + j
                if s in sum1:
                    sum1[s] += 1
                else:
                    sum1[s] = 1
        
        sum2 = dict()
        for i in nums3:
            for j in nums4:
                s = i + j
                if s in sum2:
                    sum2[s] += 1
                else:
                    sum2[s] = 1
        
        result = 0
        for i in sum1:
            if -i in sum2:
                result += sum1[i] * sum2[-i]
                
        return result
                