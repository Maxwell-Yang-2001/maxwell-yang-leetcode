class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # greedy
        points.sort(key=lambda p: p[1])
        
        curr = points[0][0] - 1
        arrows = 0
        for p in points:
            if p[0] > curr:
                curr = p[1]
                arrows += 1
        return arrows
        
                