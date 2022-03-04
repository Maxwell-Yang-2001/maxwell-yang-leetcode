class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row, curr_row = [0] * (query_row + 1), [0] * (query_row + 1)
        curr_row[0] = poured
        for row in range(1, query_row + 1):
            tmp = prev_row
            prev_row = curr_row
            curr_row = tmp
            curr_row[0] = 0
            for col in range(0, row):
                to_add = max((prev_row[col] - 1) / 2, 0.0)
                curr_row[col] += to_add
                curr_row[col + 1] = to_add
        
        return min(curr_row[query_glass], 1.0)
