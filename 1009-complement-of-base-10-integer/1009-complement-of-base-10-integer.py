class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        digits = floor(log(n) / log(2)) + 1
        return 2 ** digits - 1 - n