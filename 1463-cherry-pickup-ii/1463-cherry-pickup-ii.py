class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        width, height = len(grid[0]), len(grid)
        
        # saving for the row below (with col1, col2 being the column of r1 and r2, col1 <= col2)
        nextRowSaving = [[0 for i in range(width)] for j in range(width)]
        currRowSaving = [[0 for i in range(width)] for j in range(width)]
        for col1 in range(width):
            nextRowSaving[col1][col1] = grid[height - 1][col1]
            for col2 in range(col1 + 1, width):
                nextRowSaving[col1][col2] = grid[height - 1][col1] + grid[height - 1][col2]
        
        for row in range(height - 2, 0, -1):
            for col1 in range(width):
                for col2 in range(col1, width):
                    best = 0
                    for nextRowCol1 in range(max(col1 - 1, 0), min(col1 + 2, width)):
                        for nextRowCol2 in range(max(col2 - 1, 0), min(col2 + 2, width)):
                            best = max(best, nextRowSaving[min(nextRowCol1, nextRowCol2)][max(nextRowCol1, nextRowCol2)])
                    currRowSaving[col1][col2] = best + grid[row][col1] + grid[row][col2] if col1 != col2 else 0
            
            # swap curr and next row for next iteration
            tmpRowSaving = currRowSaving
            currRowSaving = nextRowSaving
            nextRowSaving = tmpRowSaving
        
        best = 0
        for nextRowCol1 in range(2):
            for nextRowCol2 in range(width - 2, width):
                best = max(best, nextRowSaving[min(nextRowCol1, nextRowCol2)][max(nextRowCol1, nextRowCol2)])
        return best + grid[0][0] + grid[0][width - 1]