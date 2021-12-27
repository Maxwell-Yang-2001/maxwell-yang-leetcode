class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Map = dict()
        for i, n in enumerate(nums2):
            nums2Map[n] = i
        
        result = [0] * len(nums1)
        for i, n in enumerate(nums1):
            result[i] = nums2Map[n]
        
        return result