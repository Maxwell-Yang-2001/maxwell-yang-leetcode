class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyMap = dict()
        for i, c in enumerate(keyboard):
            keyMap[c] = i
        
        result = keyMap[word[0]]
        for i in range(len(word) - 1):
            result += abs(keyMap[word[i]] - keyMap[word[i+1]])
        
        return result
            