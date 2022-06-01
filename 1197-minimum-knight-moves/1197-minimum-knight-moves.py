class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x
        if x == 1 and y == 0:
            return 3
        if x == y == 2:
            return 4
        
        diff = x - y
        diff_y = diff - y
        return diff - 2 * (diff_y // 3 if diff_y < 0 else diff_y // 4)