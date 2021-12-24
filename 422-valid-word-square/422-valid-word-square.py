class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        numWords = len(words)
        for i, row in enumerate(words):
            for j in range(i + 1, len(row)):
                if numWords <= j:
                    return False
                col = words[j]
                if len(col) <= i or row[j] != col[i]:
                    return False
            for j in range(max(i + 1, len(row)), numWords):
                if numWords <= j:
                    continue
                col = words[j]
                if len(col) > i:
                    return False
        return True
                