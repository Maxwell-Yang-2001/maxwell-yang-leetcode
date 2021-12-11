class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        currentZeroCount = 0
        for f in flowerbed:
            if f == 0:
                currentZeroCount += 1
            else:
                currentZeroCount -= 1
                if currentZeroCount > 0:
                    n -= (currentZeroCount + 1) // 2
                    if n <= 0:
                        return True
                currentZeroCount = -1
        
        if currentZeroCount > 0:
            n -= (currentZeroCount + 1) // 2
        return n <= 0