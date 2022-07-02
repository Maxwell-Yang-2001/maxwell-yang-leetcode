class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_height = 0
        prev = 0
        for curr_h in horizontalCuts:
            max_height = max(max_height, curr_h - prev)
            prev = curr_h
        max_height = max(max_height, h - prev)
        
        max_width = 0
        prev = 0
        for curr_w in verticalCuts:
            max_width = max(max_width, curr_w - prev)
            prev = curr_w
        max_width = max(max_width, w - prev)
        
        return (max_width * max_height) % (10 ** 9 + 7)