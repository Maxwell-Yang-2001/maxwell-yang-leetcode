class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        last = defaultdict(lambda: -k-1)
        for i, n in enumerate(nums):
            if i - last[n] <= k:
                return True
            last[n] = i
        
        return False