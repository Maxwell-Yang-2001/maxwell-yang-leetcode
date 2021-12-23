class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(len(s) // 2, 0, -1):
            if l % i != 0:
                continue
            save = s[0:i]
            satisfied = True
            for j in range(1, l // i):
                if s[j * i: (j + 1) * i] != save:
                    satisfied = False
                    break
            if satisfied:
                return True
            
                    