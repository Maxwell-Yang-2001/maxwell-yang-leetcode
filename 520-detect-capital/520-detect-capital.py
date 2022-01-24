class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0] >= 'a':
            return word[1:].lower() == word[1:]
        
        return word[1:].lower() == word[1:] or word[1:].upper() == word[1:]
                