class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        positive = True
        
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            positive = False
        
        numOrd0 = ord('0')
        numOrd9 = ord('9')
        maxNum = 2 ** 31 - 1
        minNum = 2 ** 31
        
        result = 0
        for c in s:
            ordCurr = ord(c)
            # it is not a number
            if numOrd0 > ordCurr or ordCurr > numOrd9:
                break
            result = result * 10 + (ordCurr - numOrd0)
            if result > maxNum and positive:
                return maxNum
            elif result > minNum and not positive:
                return -minNum
        
        return result if positive else -result
                
            