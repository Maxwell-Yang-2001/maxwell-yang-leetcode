class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        mem = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if mem[i - j * j] == False:
                    mem[i] = True
                    break
    
        return mem[n]