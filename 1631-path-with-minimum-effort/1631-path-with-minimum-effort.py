class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # binary search + dfs
        width = len(heights[0])
        height = len(heights)
        low = 0
        high = 1000000
        def dfs(x, y, limit):
            # end
            if x == height - 1 and y == width - 1:
                return True
            visited[x][y] = True
            for new_x, new_y in [[x, y + 1], [x + 1, y], [x, y - 1], [x - 1, y]]:
                if 0 <= new_x < height and 0 <= new_y < width and not visited[new_x][new_y]:
                    if abs(heights[new_x][new_y] - heights[x][y]) <= limit:
                        visited[new_x][new_y] = True
                        if dfs(new_x, new_y, limit):
                            return True
            return False
            
        while low < high:
            mid = (low + high) // 2
            # clear visited for next dfs
            visited = [[False] * width for _ in range(height)]
            if dfs(0, 0, mid):
                high = mid
            else:
                low = mid + 1
        return low