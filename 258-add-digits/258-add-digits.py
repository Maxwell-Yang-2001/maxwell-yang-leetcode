class Solution:
    def addDigits(self, num: int) -> int:
        rem = num % 9
        return 9 if (rem == 0 and num != 0) else rem
        