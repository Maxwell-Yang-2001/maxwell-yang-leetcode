class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ord_a = ord('a')
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord_a] += 1
        
        for c in t:
            freq[ord(c) - ord_a] -=1
        
        return max(freq) == 0 and min(freq) == 0