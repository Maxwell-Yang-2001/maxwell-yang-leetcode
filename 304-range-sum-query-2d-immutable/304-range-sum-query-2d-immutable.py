class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        # modify matrix so that matrix[i][j] is sumRegion(0, 0, i, j)
        width, height = len(matrix[0]), len(matrix)
        for i in range(height):
            curr_sum = 0
            for j in range(width):
                curr_sum += matrix[i][j]
                matrix[i][j] = curr_sum
            if i != 0:
                for j in range(width):
                    matrix[i][j] += matrix[i - 1][j]

    def access(self, x: int, y: int) -> int:
        return self.matrix[x][y] if (x >= 0 and y >= 0) else 0
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 -= 1
        col1 -= 1
        return self.access(row2, col2) + self.access(row1, col1) - self.access(row1, col2) - self.access(row2, col1)
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)