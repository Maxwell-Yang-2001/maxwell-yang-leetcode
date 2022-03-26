class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start: int, end: int) -> int:
            if start >= end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(start, mid)
            else:
                return binarySearch(mid + 1, end)
        return binarySearch(0, len(nums))