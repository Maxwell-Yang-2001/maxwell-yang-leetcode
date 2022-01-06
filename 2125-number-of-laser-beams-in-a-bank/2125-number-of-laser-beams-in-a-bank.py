class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevCount = 0
        beams = 0
        for row in bank:
            currCount = 0 
            for c in row:
                if c == '1':
                    currCount += 1
            if currCount != 0:
                beams += prevCount * currCount
                prevCount = currCount
        return beams