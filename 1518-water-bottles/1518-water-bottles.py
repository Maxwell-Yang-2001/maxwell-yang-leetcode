class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        numEmptyBottles = 0
        while numBottles != 0:
            result += numBottles
            numEmptyBottles += numBottles
            numBottles = numEmptyBottles // numExchange
            numEmptyBottles %= numExchange
        return result