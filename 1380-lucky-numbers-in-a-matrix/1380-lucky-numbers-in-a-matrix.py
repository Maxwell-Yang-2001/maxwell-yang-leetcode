class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        for i, row in enumerate(matrix):
            smallestNum = row[0]
            smallestIndex = 0
            for j, ele in enumerate(row):
                if ele < smallestNum:
                    smallestNum = ele
                    smallestIndex = j
            lucky = True
            for j in range(i):
                if matrix[j][smallestIndex] > smallestNum:
                    lucky = False
                    break
            if not lucky:
                continue
            for j in range(i + 1, len(matrix)):
                if matrix[j][smallestIndex] > smallestNum:
                    lucky = False
                    break
            if lucky:
                result.append(smallestNum)
        return result