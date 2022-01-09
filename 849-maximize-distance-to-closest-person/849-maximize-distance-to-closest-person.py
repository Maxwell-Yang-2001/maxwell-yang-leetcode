class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxGap = 0
        firstP = -1
        prevP = -1
        for i, s in enumerate(seats):
            if s == 1:
                if firstP == -1:
                    firstP = i
                    maxGap = i
                else:
                    maxGap = max(maxGap, (i - prevP) // 2)
                prevP = i
        maxGap = max(maxGap, len(seats) - 1 - prevP)
        return maxGap