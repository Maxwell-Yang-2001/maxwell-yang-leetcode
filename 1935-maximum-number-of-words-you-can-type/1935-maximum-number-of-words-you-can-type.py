class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        count = 0
        for w in words:
            broken = False
            for bl in brokenLetters:
                if w.find(bl) >= 0:
                    broken = True
                    break
            if not broken:
                count += 1
        return count