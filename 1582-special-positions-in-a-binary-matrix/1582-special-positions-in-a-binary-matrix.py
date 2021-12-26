class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        numRows = len(mat)
        numCols = len(mat[0])
        rows = [-1]*numRows
        cols = [-1]*numCols
        
        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                if col == 1:
                    if rows[i] >= 0:
                        rows[i] = -1
                        break
                    rows[i] = j
        
        for j in range(numCols):
            for i in range(numRows):
                if mat[i][j] == 1:
                    if cols[j] >= 0:
                        cols[j] = -1
                        break
                    cols[j] = i
        
        result = 0
        for row in rows:
            if row >= 0 and cols[row] >= 0:
                result += 1
        return result