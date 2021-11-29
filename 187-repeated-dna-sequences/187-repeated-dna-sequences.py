class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        occurDict = {}
        
        for i in range(len(s) - 9):
            currStr = s[i : i + 10]
            if currStr in occurDict:
                if occurDict[currStr] == 1:
                    result.append(currStr)
                    occurDict[currStr] = 2
            else:
                occurDict[currStr] = 1
        
        return result