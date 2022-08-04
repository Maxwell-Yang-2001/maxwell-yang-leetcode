class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # math problem: p / q oddity 3 cases:
        # odd / odd: corner 1
        # odd / even: corner 0
        # even / odd: corner 2
        
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
        
        if p % 2 == 1:
            if q % 2 == 1:
                return 1
            else:
                return 0
        else:
            return 2
                