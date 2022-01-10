class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB = len(b)
        result = ''
        carry = 0
        for i in range(max(lenA, lenB)):
            digitA = 1 if i < lenA and a[lenA - 1 - i] == '1' else 0
            digitB = 1 if i < lenB and b[lenB - 1 - i] == '1' else 0
            curr = digitA + digitB + carry
            carry = curr // 2
            result = ('1' if curr % 2 == 1 else '0') + result
        
        return result if carry == 0 else '1' + result