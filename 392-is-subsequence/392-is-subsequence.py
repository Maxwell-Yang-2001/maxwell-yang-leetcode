class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = -1
        for c in s:
            start = t.find(c, start + 1)
            if start < 0:
                return False
        return True