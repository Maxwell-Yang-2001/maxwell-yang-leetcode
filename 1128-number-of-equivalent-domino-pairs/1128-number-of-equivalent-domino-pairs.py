class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        occur = dict()
        for domino in dominoes:
            if (domino[0], domino[1]) in occur:
                occur[(domino[0], domino[1])] += 1
            elif (domino[1], domino[0]) in occur:
                occur[(domino[1], domino[0])] += 1
            else:
                occur[(domino[0], domino[1])] = 1
        
        numPairs = 0
        for freq in occur.values():
            numPairs += freq * (freq - 1) // 2
        
        return numPairs
                