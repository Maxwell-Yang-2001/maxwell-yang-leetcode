class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # indicate the indice where different, or -2 if found a pair for swapping
        differentI = -1
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if differentI == -2:
                return False
            elif differentI == -1:
                differentI = i
            else:
                if s1[differentI] != s2[i] or s1[i] != s2[differentI]:
                    return False
                differentI = -2
        # only return true if identical (-1) or found a pair for swapping (-2)
        return differentI < 0