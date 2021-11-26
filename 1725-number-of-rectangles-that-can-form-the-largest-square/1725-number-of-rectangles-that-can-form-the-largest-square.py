class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count, largest = 0, 0
        for rect in rectangles:
            curr = min(rect[0], rect[1])
            if curr == largest:
                count += 1
            elif curr > largest:
                largest = curr
                count = 1
        return count