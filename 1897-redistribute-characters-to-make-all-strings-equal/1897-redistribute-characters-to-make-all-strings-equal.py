class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        occur = dict()
        for w in words:
            for c in w:
                if c in occur:
                    occur[c] += 1
                else:
                    occur[c] = 1
        for l in occur:
            if occur[l] % len(words) != 0:
                return False
        return True