class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0] * 26
        ord_a = ord('a')
        mismatch = 0
        for c in s1:
            diff = ord(c) - ord_a
            freq[diff] += 1
            if freq[diff] == 1:
                mismatch += 1
        
        k = len(s1)
        for c in s2[:k]:
            diff = ord(c) - ord_a
            freq[diff] -= 1
            if freq[diff] == 0:
                mismatch -= 1
            elif freq[diff] == -1:
                mismatch += 1
        
        if mismatch == 0:
            return True
            
        for i in range(k, len(s2)):
            diff = ord(s2[i]) - ord_a
            freq[diff] -= 1
            if freq[diff] == 0:
                mismatch -= 1
            elif freq[diff] == -1:
                mismatch += 1
            
            diff = ord(s2[i - k]) - ord_a
            freq[diff] += 1
            if freq[diff] == 0:
                mismatch -= 1
            elif freq[diff] == 1:
                mismatch += 1
            
            if mismatch == 0:
                return True
        
        return False
            
            
            
            
        
        