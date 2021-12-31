class Solution:
    def minimumMoves(self, s: str) -> int:
        result = 0
        index = s.find('X', 0)
        while index != -1:
            result += 1
            index = s.find('X', index + 3)
        return result