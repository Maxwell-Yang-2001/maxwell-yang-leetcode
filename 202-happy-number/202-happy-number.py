class Solution:
    def isHappy(self, n: int) -> bool:
        prev = set()
        prev.add(n)
        
        curr = n
        while True:
            newCurr = 0
            while curr > 0:
                newCurr += (curr % 10) ** 2
                curr //= 10
            if newCurr == 1:
                return True
            elif newCurr in prev:
                return False
            curr = newCurr
            prev.add(curr)
            