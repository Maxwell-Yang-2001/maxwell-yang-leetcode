class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = []
        saveN = n
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        total = 0
        for d in digits:
            total += d ** len(digits)
        
        return total == saveN