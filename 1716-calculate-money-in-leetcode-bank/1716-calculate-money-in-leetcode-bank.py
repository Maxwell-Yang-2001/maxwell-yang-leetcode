class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        return 28 * weeks + 7 * (weeks - 1) * weeks // 2 + weeks * days + (days + 1) * days // 2
        