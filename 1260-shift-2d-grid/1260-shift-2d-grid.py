class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        result = copy.deepcopy(grid)
        width, gridSize = len(grid[0]), len(grid) * len(grid[0])
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                pos = (j + i * width + k) % gridSize
                result[pos // width][pos % width] = val
        return result