class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pals = [[] for i in range(len(s))]
        for l in range(1, len(s) + 1):
            for i in range(len(s)):
                if i + l <= len(s):
                    isPal = True
                    for j in range(l // 2):
                        if s[i + j] != s[i + l - 1 - j]:
                            isPal = False
                            break
                    if isPal:
                        pals[i].append(l)
        return self.recur(s, pals, 0)
    
    def recur(self, s: str, pals: List[List[int]], start: int) -> List[List[str]]:
        if start >= len(s):
            return []
        
        result = []
        for pal in pals[start]:
            if pal + start == len(s):
                result.append([s[start : start + pal]])
            else:
                nexts = self.recur(s, pals, start + pal)
                for n in nexts:
                    n.insert(0, s[start : start + pal])
                    result.append(n)
        return result