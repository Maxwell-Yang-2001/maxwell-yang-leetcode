class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        if len(s) < 3:
            return result
        tup = (s[0], s[1], s[2])
        if tup[0] != tup[1] and tup[1] != tup[2] and tup[0] != tup[2]:
            result += 1
        for i in range(3, len(s)):
            tup = (tup[1], tup[2], s[i])
            if tup[0] != tup[1] and tup[1] != tup[2] and tup[0] != tup[2]:
                result += 1
        return result
                