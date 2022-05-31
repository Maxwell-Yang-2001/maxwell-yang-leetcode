class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        multiplier = 2 ** k
        ord_0 = ord('0')
        collection = [0] * multiplier
        val = 0
        for i in range(0, k):
            val = (val << 1) + ord(s[i]) - ord_0
        
        collection[val] = 1
        
        for i in range(k, len(s)):
            val = (val << 1) % multiplier + ord(s[i]) - ord_0
            collection[val] = 1
        
        return sum(collection) == multiplier
            