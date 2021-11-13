class Solution:
    def solveEquation(self, equation: str) -> str:
        xCount, sum = 0, 0
        left = True
        add = True
        hasNum = False
        isX = False
        curr = 0
        for c in equation:
            if c == "=" or c == "+" or c == "-":
                if isX:
                    if curr == 0 and hasNum == False:
                        curr = 1
                    xCount += curr if add else -curr
                else:
                    sum += curr if add else -curr
                hasNum = False
                isX = False
                curr = 0
                if c == "=":
                    left = False
                add = not left if c == "-" else left
            elif c == "x":
                isX = True
            else:
                hasNum = True
                curr = curr * 10 + int(c)
        
        if isX:
            if curr == 0 and hasNum == False:
                curr = 1
            xCount += curr if add else -curr
        else:
            sum += curr if add else -curr
        
        # Now we have xCount * x + sum = 0
        
        if xCount == 0:
            return "Infinite solutions" if sum == 0 else "No solution"
        
        return "x=" + str(-sum // xCount)
                