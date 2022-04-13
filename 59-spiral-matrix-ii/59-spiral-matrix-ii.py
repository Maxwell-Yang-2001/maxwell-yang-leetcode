class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom, left, right = 0, n - 1, 0, n - 1
        matrix = [[0] * n for i in range(n)]
        limit = n * n
        # direction: 0 right, 1 down, 2 left, 3 up
        direction = 0
        curr_x, curr_y = 0, 0
        for i in range(limit):
            matrix[curr_x][curr_y] = i + 1
            if direction == 0:
                curr_y += 1
                if curr_y == right:
                    direction = 1
                    top += 1
            elif direction == 1:
                curr_x += 1
                if curr_x == bottom:
                    direction = 2
                    right -= 1
            elif direction == 2:
                curr_y -= 1
                if curr_y == left:
                    direction = 3
                    bottom -= 1
            else:
                curr_x -= 1
                if curr_x == top:
                    direction = 0
                    left += 1
        
        return matrix