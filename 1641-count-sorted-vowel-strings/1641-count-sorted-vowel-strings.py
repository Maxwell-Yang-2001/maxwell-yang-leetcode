from math import comb

class Solution:
    def countVowelStrings(self, n: int) -> int:
        result = 0
        # up to 5 scenarios (A, AB, ABC, ABCD, ABCDE)
        for i in range(min(n, 5)):
            result += comb(5, i + 1) * comb(n - 1, i)
        return result