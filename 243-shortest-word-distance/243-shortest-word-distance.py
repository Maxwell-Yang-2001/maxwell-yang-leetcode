class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        maxWord1Index = -1
        maxWord2Index = -1
        result = 40000
        for i, word in enumerate(wordsDict):
            if word == word1:
                maxWord1Index = i
                if maxWord2Index != -1:
                    result = min(result, maxWord1Index - maxWord2Index)
            elif word == word2:
                maxWord2Index = i
                if maxWord1Index != -1:
                    result = min(result, maxWord2Index - maxWord1Index)
        return result