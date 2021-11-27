class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        for i in range(homePos[0], startPos[0], -1) if startPos[0] < homePos[0] else range(homePos[0], startPos[0], 1):
            cost += rowCosts[i]

        for i in range(homePos[1], startPos[1], -1) if startPos[1] < homePos[1] else range(homePos[1], startPos[1], 1):
            cost += colCosts[i]

        return cost