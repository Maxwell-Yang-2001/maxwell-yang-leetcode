class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # basic BFS
        curr_list = [(0, 0)]
        next_list = []
        level = 1
        visited = {(0, 0)}
        
        while curr_list:
            for row, col in curr_list:
                if (row, col) == (max_row, max_col):
                    return level
                # go through valid neighbors with 0
                for row_diff, col_diff in directions:
                    new_row = row + row_diff
                    new_col = col + col_diff
                    if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                        continue
                    if grid[new_row][new_col] != 0:
                        continue
                    
                    neighbor = (new_row, new_col)
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    next_list.append(neighbor)
            
            level += 1
            curr_list = next_list
            next_list = []
        
        return -1