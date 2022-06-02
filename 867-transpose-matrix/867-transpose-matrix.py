class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        width, height = len(matrix[0]), len(matrix)
        result = [[0] * height for i in range(width)]
        
        for i in range(height):
            for j in range(width):
                result[j][i] = matrix[i][j]
        
        return result