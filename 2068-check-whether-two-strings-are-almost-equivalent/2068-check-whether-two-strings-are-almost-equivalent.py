class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        occ = dict()
        for c in word1:
            if c in occ:
                occ[c] += 1
            else:
                occ[c] = 1
        for c in word2:
            if c in occ:
                occ[c] -= 1
            else:
                occ[c] = -1
        for c in occ:
            if occ[c] > 3 or occ[c] < -3:
                return False
        return True