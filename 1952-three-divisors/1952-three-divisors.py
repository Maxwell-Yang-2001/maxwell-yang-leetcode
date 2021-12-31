class Solution:
    def isThree(self, n: int) -> bool:
        # question is the same as if n is a square of a prime number
        prime = int(n ** 0.5)
        if prime * prime != n or n == 1:
            return False
        
        for i in range(2, floor(prime ** 0.5) + 1):
            if prime % i == 0:
                return False
        return True