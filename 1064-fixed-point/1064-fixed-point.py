class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        def binary_search(start: int, end: int) -> int:
            if start > end:
                return -1
            elif start == end:
                return start if arr[start] == start else -1
            mid = (start + end) // 2
            if arr[mid] == mid:
                return binary_search(start, mid)
            elif arr[mid] > mid:
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)
        return binary_search(0, len(arr) - 1)
        