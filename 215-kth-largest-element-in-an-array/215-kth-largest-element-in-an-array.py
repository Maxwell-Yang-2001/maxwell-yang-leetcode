class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = []
        for i, n in enumerate(nums):
            heapq.heappush(k_largest, n)
            if i >= k:
                heapq.heappop(k_largest)
        return heapq.heappop(k_largest)