class Solution:
    def largestOddNumber(self, num: str) -> str:
        ord_1 = ord('1')
        
        for i in range(len(num) - 1, -1, -1):
            if (ord(num[i]) - ord_1) % 2 == 0:
                return num[:i + 1]
        return ''