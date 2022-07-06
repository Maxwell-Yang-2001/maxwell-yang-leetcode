class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev = 0
        curr = 1
        for i in range(n - 1):
            new = prev + curr
            prev = curr
            curr = new
        
        return curr
        