class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        # odd length ones
        for i in range(0, length):
            count += 1
            for j in range(1, min(i + 1, length - i)):
                if s[i - j] == s[i + j]:
                    count += 1
                else:
                    break
        
        # even length ones
        for i in range(0, length - 1):
            if s[i] != s[i + 1]:
                continue
            count += 1
            for j in range(1, min(i + 1, length - i - 1)):
                if s[i - j] == s[i + 1 + j]:
                    count += 1
                else:
                    break
        
        return count