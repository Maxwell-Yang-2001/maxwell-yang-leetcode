class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        # cannot capitalize everything except the first
        if word[0] >= 'a' and word[1] < 'a':
            return False
        
        cap = word[1] < 'a'
        
        for i in range(2, len(word)):
            curr_cap = word[i] < 'a'
            if (cap and not curr_cap) or (not cap and curr_cap):
                return False
        
        return True
                