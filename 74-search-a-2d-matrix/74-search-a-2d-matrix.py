class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width, height = len(matrix[0]), len(matrix)
        def search(start: int, end: int) -> bool:
            if start >= end:
                return False
            mid = (start + end) // 2
            mid_value = matrix[mid // width][mid % width]
            if mid_value == target:
                return True
            elif mid_value > target:
                return search(0, mid)
            else:
                return search(mid + 1, end)
                
        return search(0, width * height)