class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        width, height = len(box[0]), len(box)
        result = [["."] * height for i in range(width)]
        
        for i, row in enumerate(box):
            stoneCounter = 0
            currCol = height - i - 1
            for j, c in enumerate(row):
                if c == "*":
                    result[j][currCol] = "*"
                    while stoneCounter > 0:
                        result[j - stoneCounter][currCol] = "#"
                        stoneCounter -= 1
                elif c == "#":
                    stoneCounter += 1
            while stoneCounter > 0:
                result[width - stoneCounter][currCol] = "#"
                stoneCounter -= 1
        return result