class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_list = [0] * 26
        ord_a = ord('a')
        for c in s:
            freq_list[ord(c) - ord_a] += 1
        
        for c in t:
            ind = ord(c) - ord_a
            freq_list[ind] -= 1
            if freq_list[ind] == -1:
                return chr(ind + ord_a)
        
        return ''
            
            