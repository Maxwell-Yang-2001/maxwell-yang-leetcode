class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(200):
            currentC = '!'
            currentSet = False
            for s in strs:
                if len(s) < i + 1:
                    return s[:i]
                if s[i] != currentC:
                    if not currentSet:
                        currentSet = True
                        currentC = s[i]
                    else:
                        return s[:i]
        return strs[0]
                