# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        # if has no ship, just return
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        heightRange = topRight.y - bottomLeft.y + 1
        widthRange = topRight.x - bottomLeft.x + 1
        
        # recursion base case
        if widthRange == 1 and heightRange == 1:
            return 1 if sea.hasShips(topRight, bottomLeft) else 0
        
        if widthRange >= heightRange:
            midX = (topRight.x + bottomLeft.x) // 2
            return self.countShips(sea, topRight, Point(midX + 1, bottomLeft.y)) + self.countShips(sea, Point(midX, topRight.y), bottomLeft)
        
        midY = (topRight.y + bottomLeft.y) // 2
        return self.countShips(sea, topRight, Point(bottomLeft.x, midY + 1)) + self.countShips(sea, Point(topRight.x, midY), bottomLeft)
            