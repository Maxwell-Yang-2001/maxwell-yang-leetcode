class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        for i in range(1, 2 * n + 1):
            result *= i
        
        return (result // 2 ** n) % (10 ** 9 + 7)