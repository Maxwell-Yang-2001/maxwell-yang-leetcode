class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestSoFar = prices[0]
        result = 0
        for p in prices:
            diff = p - lowestSoFar
            if diff < 0:
                lowestSoFar = p
            elif result < diff:
                result = diff
        return result