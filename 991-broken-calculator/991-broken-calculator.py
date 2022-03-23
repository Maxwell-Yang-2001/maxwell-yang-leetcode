class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # backwards: add 1 or divide by 2
        result = 0
        while startValue < target:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            result += 1
        return result + startValue - target