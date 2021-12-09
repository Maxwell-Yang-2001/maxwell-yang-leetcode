class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        xDiff0 = points[0][0] - points[1][0]
        yDiff0 = points[0][1] - points[1][1]
        xDiff1 = points[1][0] - points[2][0]
        yDiff1 = points[1][1] - points[2][1]
        # point 0 = point 1
        if xDiff0 == 0 and yDiff0 == 0:
            return False
        # point 1 = point 2
        if xDiff1 == 0 and yDiff1 == 0:
            return False
        # point 0 = point 2
        if xDiff0 + xDiff1 == 0 and yDiff0 + yDiff1 == 0:
            return False
        
        return xDiff0 * yDiff1 != xDiff1 * yDiff0
        