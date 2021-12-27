class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chrMap = dict()
        
        # All occurrences of a character must be replaced with another character 
        for i in range(len(s)):
            if s[i] in chrMap:
                if t[i] != chrMap[s[i]]:
                    return False
            else:
                chrMap[s[i]] = t[i]
        
        # No two characters may map to the same character
        return len(set(chrMap.values())) == len(chrMap)
            